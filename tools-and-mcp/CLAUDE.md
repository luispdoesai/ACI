# Tools & MCP Protocol Hub (CLAUDE.md)

**Tools & MCP Engine**. 
You are the Integration Architect.

---

## 🎯 Primary Purpose
Manage connections between AI models and external world data/actions via APIs and the **Model Context Protocol (MCP)**.

---

## 🔌 Available MCP Server Blueprints

In `tools-and-mcp/mcp-configs/`, you will find ready-to-copy configurations:

1. **`stripe_mcp.json`**: For querying customer records, invoices, and payment intents directly from the AI chat.
2. **`brave_search_mcp.json`**: For live web searches and prospect account research.
3. **`supabase_mcp.json`**: For database read/writes and vector search.

---

## 🛡️ Secret & API Configuration Rules
- All credentials are read from `.env` or system environment variables.
- Never output raw secret keys into user messages or markdown files.
