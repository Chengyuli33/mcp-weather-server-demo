from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Create a FastAPI app instance
app = FastAPI(title="MCP Server Framework")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, MCP server is running!"}

# Example MCP-like endpoint (placeholder)
@app.get("/mcp/ping")
def mcp_ping():
    return JSONResponse(content={"status": "ok", "message": "MCP server says hello"})
    
if __name__ == "__main__":
    import uvicorn
    # Run the server on localhost:8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
