# PDF Chat Interface

A Gradio-based web application that allows users to upload PDF files and ask questions about their content using an AI-powered chat interface.

## Features

- Upload PDF files through a user-friendly web interface
- Ask questions about the uploaded PDF content
- AI-powered responses using Groq's LLM
- Clean, modern chat interface built with Gradio

## Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerized deployment)
- Groq API key

## Setup

### 1. Clone the repository
```bash
git clone <repository-url>
cd tbd
```

### 2. Install dependencies
```bash
cd app
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file in the project root:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the application
```bash
python app.py
```

The application will be available at `http://localhost:7860`

## Docker Deployment

### Build the Docker image
```bash
docker build -t pdf-chat-app .
```

### Run the container
```bash
docker run -p 7860:7860 --env-file .env pdf-chat-app
```

The application will be available at `http://localhost:7860`

## Usage

1. Open the web interface in your browser
2. Upload a PDF file using the file upload button
3. Type your question about the PDF content in the chat box
4. Receive AI-powered responses based on the PDF content

## Project Structure

```
tbd/
├── app/
│   ├── app.py          # Gradio interface
│   ├── funcs.py        # PDF processing and chat logic
│   └── requirements.txt # Python dependencies
├── Dockerfile          # Docker configuration
├── .env               # Environment variables (create this)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## API Configuration

This application uses the Groq API for AI responses. You'll need to:

1. Sign up for a Groq account at https://console.groq.com/
2. Generate an API key
3. Add the API key to your `.env` file

## Dependencies

- `gradio==5.34.1` - Web interface framework
- `groq==0.28.0` - Groq API client
- `PyPDF2==3.0.1` - PDF text extraction
- `transformers==4.52.4` - Machine learning utilities
- `dotenv==0.9.9` - Environment variable management

## License

This project is open source and available under the MIT License.