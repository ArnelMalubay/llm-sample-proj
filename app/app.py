# Personal Assistant Chatbot - A simple AI assistant for trial purposes

import gradio as gr
from funcs import chat_with_assistant, SYSTEM_MESSAGE

# Main chat function that handles the conversation
def respond(message, history):
    """
    Handle user messages and return streaming responses
    """
    if not message.strip():
        yield "Please enter a message."
        return
    
    # Get the streaming generator and yield each response
    for partial_response in chat_with_assistant(message, history):
        yield partial_response

# Create the chatbot interface
demo = gr.ChatInterface(
    fn = respond,
    type = "messages",
    title = "Personal Assistant",
    description = "A helpful AI assistant for general questions and tasks. I can help with information, writing, analysis, and more!",
    examples = [
        "What's the weather like today?",
        "Help me write a professional email",
        "Explain quantum physics in simple terms",
        "Give me some productivity tips",
        "What are some healthy breakfast ideas?"
    ]
)

if __name__ == "__main__":
    # Enable queuing for streaming support
    demo.queue().launch(server_name = "0.0.0.0", server_port = 7860)

