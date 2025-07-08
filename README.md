# Personal Assistant Chatbot

A modern AI-powered personal assistant built with Gradio and Groq API, featuring real-time streaming responses for natural conversations. 

## Features

- 🤖 **AI-Powered Assistant**: Uses Groq's lightning-fast LLM (llama-3.1-8b-instant) for intelligent responses
- 💬 **Streaming Chat**: Real-time response streaming for natural conversation flow
- 🌐 **Web Interface**: Clean, modern chat interface built with Gradio ChatInterface
- 🐳 **Docker Ready**: Containerized for easy deployment and scalability

## Prerequisites

- Python 3.9+ 
- Docker (optional, for containerized deployment)
- Groq API key ([Get one here](https://console.groq.com/))

## Quick Start

### 1. Clone the repository
```bash
git clone <repository-url>
cd sample-personal-assistant-chatbot
```

### 2. Set up environment variables
Create a `.env` file in the project root:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run with Python
```bash
cd app
pip install -r requirements.txt
python app.py
```

### 4. Run with Docker
```bash
# Build the image
docker build -t personal-assistant-chatbot:latest .

# Run the container
docker run -p 7860:7860 --env-file .env personal-assistant-chatbot:latest
```

The application will be available at `http://localhost:7860`

## Usage

1. Open your browser and navigate to `http://localhost:7860`
2. Start chatting with your AI assistant
3. Try the example prompts or ask any general questions
4. Enjoy real-time streaming responses!

## Access via HuggingFace spaces
You can also access a hosted version of this app in Huggingface Spaces via this ([link](https://huggingface.co/spaces/arnel8888/sample-personal-assistant-chatbot)). 

### Example Interactions

- "Help me write a professional email"
- "Explain quantum physics in simple terms" 
- "Give me some productivity tips"
- "What are some healthy breakfast ideas?"

## Project Structure

```
sample-personal-assistant-chatbot/
├── app/
│   ├── app.py           # Main Gradio application
│   ├── funcs.py         # Chat logic and Groq API integration
│   └── requirements.txt # Python dependencies
├── Dockerfile           # Docker configuration
├── .dockerignore       # Docker ignore rules
├── .env                # Environment variables (create this)
├── gitignore           # Git ignore rules
└── README.md           # This file
```

## Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key (required)

### Customization

You can customize the assistant by modifying the `SYSTEM_MESSAGE` in `app/funcs.py`:

```python
SYSTEM_MESSAGE = "Your custom system prompt here..."
```

## API Configuration

This application uses the Groq API for ultra-fast AI responses:

1. **Sign up**: Create account at [console.groq.com](https://console.groq.com/)
2. **API Key**: Generate your API key from the console
3. **Environment**: Add `GROQ_API_KEY=your_key_here` to your `.env` file

## Dependencies

- `gradio==5.33.0` - Modern web interface framework
- `groq==0.28.0` - Groq API client for fast LLM inference
- `python-dotenv==1.0.0` - Environment variable management

## Development

### Running in Development Mode

For faster development with auto-reload:

```bash
cd app
gradio app.py
```

This enables hot-reload when you make changes to your code.

### Docker Development

```bash
# Build and run in one command
docker build -t personal-assistant-chatbot:latest . && docker run -p 7860:7860 --env-file .env personal-assistant-chatbot:latest
```

## Deployment Options

- **Local**: Run directly with Python
- **Docker**: Use provided Dockerfile for containerized deployment
- **Cloud**: Deploy to any cloud platform supporting Docker containers
- **HuggingFace Spaces**: Use `gradio deploy` for easy cloud deployment

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions:

1. Check the [Gradio documentation](https://gradio.app/)
2. Review the [Groq API docs](https://console.groq.com/docs/)
3. Open an issue in this repository
