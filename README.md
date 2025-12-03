# Deep Research System

A comprehensive AI research assistant that plans, searches, and summarizes topics, with optional email reporting.

## Features
- **Planning Agent**: Breaks down queries into search tasks
- **Search Agent**: Executes web searches using multiple models
- **Writer Agent**: Synthesizes information into reports
- **Email Integration**: Sends formatted HTML reports via SendGrid
- **Web UI**: Built with Gradio for easy interaction

## Setup & Run

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   Create a `.env` file:
   ```env
   OPENROUTER_API_KEY=your_key
   SENDGRID_API_KEY=your_key  # Optional
   ```

3. **Run the Application**
   
   **Web Interface (Recommended):**
   ```bash
   # Run the batch file (Windows)
   start_gradio.bat
   
   # OR using python
   python gradio_app.py
   ```

   **Command Line:**
   ```bash
   python deep_research.py
   ```

## Technologies Used

- **Python 3.10+**
- **OpenAI SDK** (via OpenRouter)
- **Gradio** (Web Interface)
- **AsyncIO** (Parallel processing)
- **SendGrid** (Email delivery)
