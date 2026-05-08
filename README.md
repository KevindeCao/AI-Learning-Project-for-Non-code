AI Chatbot with Claude API
A super simple Python AI chatbot using the Claude API from Anthropic Claude.
This project is beginner-friendly and made for people who are not coders.

1. Install Python and VS Code
Download Python
Go to:
Python Official Website
IMPORTANT:
When installing Python, make sure you tick:
✅ "Add Python to PATH"
before clicking Install.

Download VS Code
Go to:
Visual Studio Code
Install normally.

2. Create Your Project Folder
Create a folder anywhere on your PC.
Example:
AI_Chatbot
Open this folder in VS Code.

3. Create These Files
Inside your folder or open folder with VSCODE, create:
main.py
history_chat.py
.env

5. Get Your Claude API Key
Go to:
Claude Console


Create account


Login


Generate API Key



5. Paste API Key into .env
Inside .env file:
ANTHROPIC_API_KEY=your_api_key_here
IMPORTANT:
⚠️ NEVER share your .env file publicly.
⚠️ NEVER upload your API key to GitHub.
⚠️ Your API key is private like a password.

6. Install Required Libraries
Open VS Code terminal.
Run:
pip install anthropic python-dotenv

7. Paste Your Code
main.py
Paste your main Python code here.

history_chat.py
Example:
history_chat = """Important information or previous conversation goes here."""
This file is used to manually store memory/chat history.

8. Run the AI Chatbot
Open terminal in VS Code and run:
python main.py
If successful:
You:
Now start chatting with your AI.

9. Exit Chat
Type:
exit
to stop the chatbot.

10. How Memory Works
This chatbot stores conversation manually.
Current chat memory:
Stored temporarily inside:
Fus.history

Permanent memory:
Stored manually inside:
history_chat.py
Example:
history_chat = """- User likes business strategy- User works in plastic resin sales- User prefers simple answers"""
You can update this file anytime before starting a new chat.

11. Change AI Personality
Inside main.py:
Fus = AI_bot(    "You are a caveman...")
Change this text to create different AI personalities.
Example:
"You are a professional business consultant""You are a funny anime girl""You are a coding teacher"

12. Change AI Model
Inside:
model="claude-sonnet-4-6"
You can replace with newer Claude models later.
Check available models here:
Claude API Documentation

Simple Project Structure
AI_Chatbot/│├── main.py├── history_chat.py├── .env

Done
You now have your own local AI chatbot powered by Claude API.
