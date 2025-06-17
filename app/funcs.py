from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

system_prompt = """
You are a helpful IT support chatbot for 'Tech Solutions'.
Your role is to assist employees with common IT issues, provide guidance on using company software, and help troubleshoot basic technical problems.
Respond clearly and patiently. If an issue is complex, explain that you will create a support ticket for a human technician.
Keep responses brief and ask a maximum of one question at a time.
"""

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": "My monitor isn't turning on.",
        },
        {
            "role": "assistant",
            "content": "Let's try to troubleshoot. Is the monitor properly plugged into a power source?",
        },
        {
            "role": "user",
            "content": "Yes, it's plugged in."
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
