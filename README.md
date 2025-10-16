# MCP Weather Server Demo Overview

🌦️ This project implements a lightweight Model Context Protocol (MCP) server that provides real-time weather data through the National Weather Service API. Built in Python using **FastMCP** and `httpx`, it can be locally connected to **Claude Desktop** for tool execution and context-aware interactions.

It consists of two main phases:

**⚙️ Development Phase:**  
You will create an MCP server (`weather.py`) using Python. The environment and dependencies (`mcp[cli]`, `httpx`) are managed with `uv`. The server is implemented using FastMCP.

**📦 Integration Phase:**  
You will configure Claude Desktop to connect to and launch your MCP server. This is done by editing the `claude_desktop_config.json` file, specifying how Claude Desktop should start and communicate with your MCP server.

This project is guided by the [Model Context Protocol](https://modelcontextprotocol.io/docs/develop/build-server) and the source code comes from [MCP quickstart for Python](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-python).


## 🚀 Build an MCP server

### 🛠️ Developer tools required
- macOS
- Python 3.10 or higher
- Python MCP SDK 1.2.0 or higher
- Claude for Desktop

### 1. Set up environment

We first need to install the `uv` tool and use it as your Python environment manager.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
You will need to restart your terminal to make the `uv` command available. Please check if `uv` is installed correctly by running:

```bash
uv --version
```


### 2. Initialize a new Python project with uv

Use `uv` to create a new project named `weather`. This will initialize a `weather/` folder containing a `pyproject.toml` configuration file.
```bash
uv init weather
cd weather
```



### 3. Create virtual environment and activate it
```bash
uv venv
source .venv/bin/activate
```



### 4. Install dependencies

Install the required dependencies MCP library with CLI support and automatically add them to `pyproject.toml`. Now the `weather` project includes both the MCP library and an HTTP client library.

```bash
uv add "mcp[cli]" httpx
```

### 5. Create the local MCP server file

Create an empty MCP server file named `weather.py` in your current directory. This file will contain your MCP server logic.

```bash
touch weather.py
```

Then, in the `weather.py` you need to import the necessary packages and set up the instance; add helper functions; and implement the MCP tool execution; and finally, run the server.

### 6. Configure Claude for Desktop to connect to MCP server
To configure Claude for Desktop to connect to your MCP server, open the configuration file located at `~/Library/Application Support/Claude/claude_desktop_config.json` in a text editor. If the file does not exist, create it. Add your MCP server details as shown below and save the file:


```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
        "run",
        "weather.py"
      ]
    }
  }
}
```
Remember to replace `"/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather"` with the absolute path to your own `weather` project directory. You can get this path by running `pwd` in your terminal while inside the project folder.

The `"uv"` value should be the absolute path to the `uv` executable on your machine. To find it, run `which uv` in your terminal.

### 7. Start the MCP server and connect from Claude

After fully quitting and reopening Claude for Desktop (not just closing the chat window), you should see the weather server available and ready to connect in the MCP panel.

![MCP Panel1](./images/mcp_panel1.png)
![MCP Panel2](./images/mcp_panel2.png)