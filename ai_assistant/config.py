import os
from typing import Optional

class Config:
    # Load all environment variables
    GROQ_API_KEY: Optional[str] = os.getenv('GROQ_API_KEY')
    PUSHOVER_USER: Optional[str] = os.getenv('PUSHOVER_USER')  
    PUSHOVER_TOKEN: Optional[str] = os.getenv('PUSHOVER_TOKEN')
    MY_NAME: Optional[str] = os.getenv('MY_NAME')
    MY_LAST_NAME: Optional[str] = os.getenv('MY_LAST_NAME')


    @classmethod
    def validate(cls):
        """Validate all required environment variables"""
        missing_vars = []

        # Check each required variable
        if not cls.GROQ_API_KEY:
            missing_vars.append('GROQ_API_KEY')

        if not cls.PUSHOVER_USER:
            missing_vars.append('PUSHOVER_USER')

        if not cls.PUSHOVER_TOKEN:
            missing_vars.append('PUSHOVER_TOKEN')

        if not cls.MY_NAME:
            missing_vars.append('MY_NAME')

        if not cls.MY_LAST_NAME:
            missing_vars.append('MY_LAST_NAME')

        # Raise error if any are missing
        if missing_vars:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing_vars)}. "
                f"Please set them in your environment or .env file."
            )


Config.validate()
