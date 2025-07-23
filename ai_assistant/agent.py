from openai import OpenAI
import os
import json
from ai_assistant.tools import *
from ai_assistant import Config

class Agent:
    """
    Base agent class for LLM-powered assistants. Handles message flow, tool usage, and LLM interaction.
    """
    def __init__(self, tools_dict, tools_json, system_prompt, model="llama-3.3-70b-versatile"):
        """
        Initialize the Agent with tools, prompt, and model configuration.

        Args:
            tools_dict (dict): Mapping of tool names to callable functions.
            tools_json (list): List of tool schemas for LLM function calling.
            system_prompt (str or dict): System prompt for the LLM.
            model (str): Model name to use for completions.
        """
        self.tools = tools_dict
        self.tools_json = tools_json
        self.system_prompt = {"role": "system", "content": system_prompt}

        self.model = model    
        self.client = OpenAI(api_key=Config.GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")

    def get_response(self, messages):
        """
        Generate a response from the LLM, handling tool calls as needed.

        Args:
            messages (list): List of message dicts (role/content) for the conversation history.
        Returns:
            list: List of response message dicts from the LLM and tools.
        """
        input_messages =  [self.system_prompt] + messages
        output_messages = []
        done = False
        while not done:
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=input_messages,
                    tools=self.tools_json,
                    tool_choice="auto"
                )
                output_messages.append(response.choices[0].message)

                finish_reason = response.choices[0].finish_reason
                if finish_reason == "tool_calls":
                    tool_calls = response.choices[0].message.tool_calls
                    results = self.handle_tool_calls(tool_calls)
                    output_messages.extend(results)
                    # Add the response to the input messages so that the model can see the context
                    input_messages.append(response.choices[0].message)
                    input_messages.extend(results)
                else:
                    done = True
            except Exception as e:
                print(f"An error occurred: {e}")
                return []
        return output_messages

    def handle_tool_calls(self, tool_calls):
        """
        Handle tool calls requested by the LLM, invoking the appropriate functions.

        Args:
            tool_calls (list): List of tool call objects from the LLM response.
        Returns:
            list: List of tool response message dicts.
        """
        results = []
        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            print(f"Tool called: {tool_name}", flush=True)
            print(f"Arguments: {arguments}", flush=True)
            tool = self.tools[tool_name]
            result = tool(**arguments) if tool else {}
            results.append({"role": "tool","content": json.dumps(result),"tool_call_id": tool_call.id})
        return results
