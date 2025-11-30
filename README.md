# Overview

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
- Deep Research Application
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

# Features

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

## How to Run

1. Clone the repository:
   git clone https://github.com/your-username/ai-agents-lab  
   cd ai-agents-lab

2. Install dependencies:
   pip install -r requirements.txt

3. Add your API keys in `.env` or environment variables:
   OPENAI_API_KEY=your_key_here

4. Run any notebook or script inside the project folders.

## Learning Goals

- Understand how modern AI agents work
- Learn tool calling, JSON schemas, and validation
- Build real-world automation agents
- Practice multi-agent orchestration
- Prepare for AI engineering roles
