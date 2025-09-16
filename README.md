# mcp-server-framework
A framework for experimenting with Model Context Protocol (MCP) server implementations. This repository provides a basic structure and example code for setting up an MCP server in Python. Ready to integrate with tunneling tools (e.g., ngrok) for external access.

## 🛠️ Getting Started
Clone the repository
```bash
git clone git@github.com:Chengyuli33/mcp-server-framework.git
cd mcp-server-framework
```

Create and activate a independent Python virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install dependencies
```bash
pip install -r requirements.txt

Run the server
```bash
python server/main.py

```
Expose with ngrok (optional)
```bash
ngrok http 8000
```

open `http://localhost:8000/docs` or the ngrok URL in your browser to see the interactive API documentation.

open browser 
http://127.0.0.1:8000/
 → {"message": "Hello, MCP server is running!"}

http://127.0.0.1:8000/mcp/ping
 → {"status":"ok","message":"MCP server says hello"}


## 📂 Project Structure
```
mcp-server-framework/
├── server/          # Core MCP server implementation
│   └── main.py      # Entry point for the server
├── client/          # Example clients for testing
├── docs/            # Documentation and notes
├── experiments/     # Prototyping different ideas
├── requirements.txt # Dependencies
└── README.md
```

## 📘 Goals
- This project helps to understand the fundamentals of Model Context Protocol (MCP)
- Practice designing APIs that models can call
- Explore how to connect MCP servers with real-world data sources

