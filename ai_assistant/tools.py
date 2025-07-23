import os
import requests
from ai_assistant import Config


pushover_url = "https://api.pushover.net/1/messages.json"


def push(message):
    """
    Send a push notification with the given message using Pushover.

    Args:
        message (str): The message to send.
    """
    print(f"Push: {message}")
    payload = {"user": Config.PUSHOVER_USER, "token": Config.PUSHOVER_TOKEN, "message": message}
    requests.post(pushover_url, data=payload, timeout=10)


def record_user_details(email, name="Name not provided", notes="not provided"):
    """
    Record a user's contact details and interest, sending a push notification.

    Args:
        email (str): The user's email address.
        name (str, optional): The user's name. Defaults to "Name not provided".
        notes (str, optional): Additional notes or context. Defaults to "not provided".
    Returns:
        dict: Confirmation of recording.
    """
    push(f"name:{name},email:{email},notes:{notes}")
    return {"recorded": "ok"}

def record_unanswerable_question(question):
    """
    Record a question that cannot be answered, sending a push notification.

    Args:
        question (str): The unanswerable question text.
    Returns:
        dict: Confirmation of recording.
    """
    push(f"no_answer:{question}")
    return {"recorded": "ok"}


record_user_details_json = {
    "type": "function", 
    "function": {
        "name": "record_user_details",
        "description": "Use this tool to record that a user is interested in being in touch and provided an email address",
        "parameters": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "description": "The email address of this user"
                },
                "name": {
                    "type": "string",
                    "description": "The user's name, if they provided it"
                }
                ,
                "notes": {
                    "type": "string",
                    "description": "Any additional information about the conversation that's worth recording to give context"
                }
            },
            "required": ["email"],
            "additionalProperties": False
        }
    }
}

record_unanswerable_question_json = {
    "type": "function", 
    "function": {
        "name": "record_unanswerable_question",
        "description": "Precisely record questions that cannot and must not be answered",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "Exact text of the question"
                }
            },
            "required": ["question"],
            "additionalProperties": False
        }
    }
}

tools_dict = {
    "record_user_details": record_user_details,
    "record_unanswerable_question": record_unanswerable_question
}

tools_json = [record_unanswerable_question_json, record_user_details_json]
