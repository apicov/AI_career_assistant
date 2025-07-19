from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)


# Load the API keys from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')

if not groq_api_key:
    print("Groq API Key not set (and this is optional)")


class Agent:
    def __init__(self, tools_dict, tools_json, system_prompt, model="llama-3.3-70b-versatile"):
        self.tools = tools_dict
        self.tools_json = tools_json
        self.system_prompt = {"role": "system", "content": system_prompt}

        self.model = model    
        self.client = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1")

    def get_response(self, user_input, history):
        input_messages =  [self.system_prompt] + history + [{"role": "user", "content": user_input}]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=input_messages,
            tools=self.tools_json,
            tool_choice="required"
        )
        return response

    