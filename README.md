# AI Career Assistant

AI Career Assistant is a professional AI-powered assistant designed to represent a candidate in professional interactions, facilitate initial conversations with potential employers or collaborators, and manage inquiries transparently and efficiently. The assistant leverages LLMs and custom tools to provide accurate, document-based responses and facilitate meaningful connections.

## Features

- **Professional AI Representation:** Acts as a candidate's assistant, handling inquiries and screening opportunities.
- **Document-Based Responses:** Only shares information directly from the provided summary and resume.
- **Contact Facilitation:** Collects contact details and messages from interested parties, ensuring privacy and professionalism.
- **Unanswerable Question Logging:** Records questions that require the candidate's direct input.
- **Customizable Prompts:** Adapts to any candidate by loading their summary and resume.
- **Gradio Chat Interface:** Easy-to-use web chat for interactive conversations.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/AI_career_assistant.git
   cd AI_career_assistant
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # Or, if using pyproject.toml:
   pip install .
   ```
3. **Set up environment variables:**
   Create a `.env` file in the project root with the following variables:
   ```env
   GROQ_API_KEY=your_groq_api_key
   PUSHOVER_USER=your_pushover_user_key
   PUSHOVER_TOKEN=your_pushover_token
   MY_NAME=YourFirstName
   MY_LAST_NAME=YourLastName
   ```

## Usage

1. **Prepare your summary and resume:**
   - Place your professional summary in `data/summary.txt`.
   - Place your resume in `data/resume.md` (Markdown format recommended).

2. **Run the Gradio chat interface:**
   You can use the provided Jupyter notebook for interactive development:
   ```python
   # In ai_assistant/my_ai_assistant.ipynb
   from ai_assistant import Assistant
   # Load summary and resume
   with open("../data/summary.txt", "r", encoding="utf-8") as f:
       summary = f.read()
   with open("../data/resume.md", "r", encoding="utf-8") as f:
       resume = f.read()
   assistant = Assistant(name, last_name, summary, resume)
   # Launch Gradio chat
   gr.ChatInterface(chat, type="messages").launch()
   ```
   Or adapt the code to your own script.

3. **Interact with the assistant:**
   - The assistant will answer questions about your background, experience, and skills using only the provided documents.
   - For questions it cannot answer, it will log them for your review.
   - Interested parties can leave their contact details and a message for you.

## Project Structure

```
AI_career_assistant/
├── ai_assistant/
│   ├── __init__.py
│   ├── agent.py         # Core agent logic and LLM interaction
│   ├── assistant.py     # Assistant persona and prompt logic
│   ├── config.py        # Environment variable and config management
│   ├── tools.py         # Custom tools for logging and contact collection
│   └── my_ai_assistant.ipynb  # Example notebook for running the assistant
├── data/
│   ├── summary.txt      # Your professional summary
│   ├── resume.md        # Your resume (Markdown)
│   └── interview_questions.txt # Example interview questions
├── pyproject.toml       # Project metadata and dependencies
├── README.md            # Project documentation
```

## Configuration

The assistant requires several environment variables to function. These are validated at startup:
- `GROQ_API_KEY`: API key for the LLM provider (Groq/OpenAI-compatible).
- `PUSHOVER_USER` and `PUSHOVER_TOKEN`: For push notifications/logging (optional, but recommended).
- `MY_NAME` and `MY_LAST_NAME`: The candidate's name for prompt personalization.

## Contributing

Contributions are welcome! Please open issues or pull requests for bug fixes, new features, or improvements.

## License

This project is licensed under the MIT License.
