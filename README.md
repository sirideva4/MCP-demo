# 🧠 MCP-Demo — A Minimal Message Communication Protocol over HTTP

This project is a simple but powerful **Message Communication Protocol (MCP)** demo using Python. It showcases how a **client** can communicate with a **server** over **HTTP** using clean, safe, and industry-friendly techniques.

---

## 🧩 What is MCP (Message Communication Protocol)?

**MCP** is a pattern or method that defines how two programs (usually a client and a server) exchange **messages** — such as data, commands, or requests — to perform tasks.

In simple terms:

> 🗣️ Client: “Hey server, here’s a math expression like `5+7`. What’s the result?”  
> 🤖 Server: “Here you go, the answer is `12`.”

### MCP in the real world:

- Microservices talk via MCPs (HTTP, gRPC, message queues)
- Multiplayer games use MCP to sync state between players and server
- Any automation tool (CLI ↔ API) uses some form of MCP under the hood

This demo focuses on using **HTTP and JSON** as the message format — one of the most common and industry-standard protocols.

---

## 🚀 What This Project Does

✅ Implements a **Python server (`server.py`)** using FastAPI  
✅ Implements a **Python client (`client.py`)** that sends messages (math expressions)  
✅ Demonstrates how **MCP** works using HTTP requests and JSON responses  
✅ Safely evaluates expressions like `5+7`, `8/2`, `2**4`  
✅ Shows error handling for invalid math or division by zero

---

## 📁 File Overview

MCP-demo/
├── server.py # FastAPI server that evaluates math expressions
├── client.py # CLI client that sends expressions to the server
├── requirements.txt
└── README.md # This file — explains it all

## Implementation
1. Clone the Repository
git clone https://github.com/your-username/MCP-demo.git
cd MCP-demo

2. Install Requirements
pip install -r requirements.txt

Or manually:

pip install fastapi uvicorn requests

3. Start the Server
uvicorn server:app --reload

Visit http://127.0.0.1:8000/docs
 to test the API in the browser!

4. Run the CLI Client

In a new terminal window:

python client.py


Then enter expressions:

>> 2+3
Result: 5

>> 10/0
[Server Error] Division by zero

>> exit
