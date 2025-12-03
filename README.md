# Agent Automation Framework

This project is a hands-on lab where I build, test, and experiment with:
- OpenAI Function Calling Agents
- Multi-agent systems
- Tool-based agents (APIs, search tools, custom tools)
- CrewAI task delegation
- LangGraph workflow-based agents
- Autonomous decision-making
- Memory and stateful agents
- Error handling and tool orchestration

## Projects Included

This repository implements a collection of practical and well-known AI Agent projects, built using the frameworks included in this lab:  
OpenAI Agents SDK, CrewAI, LangGraph, AutoGen, and MCP.

### Using OpenAI Agents SDK
- SDR Agent (Sales Development Representative)
- Deep Research Agent
- **Deep Research Application** (See setup below)
- Tools vs Agents Guardrails Demo

### Using CrewAI Framework
- Stock Picker Agent
- Developer Agent
- Engineering Team Agent

### Using LangGraph Framework
- Sidekick Agent
- Enhanced Sidekick (Improved Version)
- Agents with tools, memory, and web-search workflows

### Using AutoGen Framework
- Agent Creator
- AutoGen Chat
- AutoGen Core Workflows
- Distributed AutoGen Agents

### Using MCP (Model Context Protocol)
- AI Equity Trader
- AI Equity Traders In Action
- Local MCP Server
- Remote MCP Server
- Full MCP Server + Client Implementation

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
   python gradio_app.py
   # OR run the batch file:
   start_gradio.bat
   ```

   **Command Line:**
   ```bash
   python deep_research.py
   ```

# General Framework Features

- Built with real working Python agent code
- Supports OpenAI’s new agent SDK
- Includes JSON schema definitions for structured tool calls
- Demonstrates effective agent-to-tool-to-agent loops
- Shows how to build multi-agent collaboration
- Covers error recovery, retries, and state tracking
- Easy to extend with your own tools and APIs

## Technologies Used

- Python 3.10+
- OpenAI SDK
- CrewAI Framework
- LangGraph
- AutoGen
- MCP
- Requests and API tools
- YAML / JSON Schema

## How to Run (General)

1. `git clone https://github.com/MaiM0hamed/agent-automation-framework.git`
   `cd agent-automation-framework`

2. Install dependencies:
   `pip install -r requirements.txt`

3. Add your API keys in `.env` or environment variables:
   `OPENAI_API_KEY=your_key_here`

4. Run any notebook or script inside the project folders.
