# 🔌 Tools & MCP Protocol Hub (`tools-and-mcp/`)

> **Your External World Connectivity: Model Context Protocol (MCP) Blueprints.**

The `tools-and-mcp/` directory provides ready-to-use blueprints for connecting your AI assistant to databases, search engines, and third-party APIs using the open **Model Context Protocol (MCP)**.

---

## 📂 Directory Structure

```text
tools-and-mcp/
├── CONTEXT.md                 # This guided context file
├── CLAUDE.md                  # Integration architecture and tool calling rules
└── mcp-configs/               # Ready-to-copy MCP configuration blueprints
    ├── mcp_settings.json      # Multi-server MCP template (Brave Search, GitHub, Filesystem)
    ├── stripe_mcp.json        # Stripe customer, invoice & charge queries
    ├── brave_search_mcp.json  # Real-time web search for account research
    └── supabase_mcp.json      # Postgres / Supabase database read & writes
```

---

## ⚡ How to Connect MCP Tools

Because modern AI tools (**Claude Code**, **Antigravity**, **Cursor**) manage MCPs natively at the client level, you can connect these tools directly:

### 1. In Claude Code
Add an MCP server directly in your terminal using the Claude CLI:
```bash
claude mcp add brave-search npx -y @modelcontextprotocol/server-brave-search
claude mcp add stripe npx -y @stripe/mcp
```

### 2. In Cursor
Go to **Settings** $\rightarrow$ **Features** $\rightarrow$ **MCP Servers** $\rightarrow$ **Add New MCP Server**, and paste the command arguments from the relevant blueprint in `tools-and-mcp/mcp-configs/`.

### 3. In Antigravity / Gemini
Configured MCP servers are loaded lazily or eagerly via your client configuration and appear directly as executable tools in your chat context.

---

## 💡 What Tools & MCP Enable
- **Live Competitor Research**: Search the live web to get fresh pricing and feature changes.
- **Direct Database Access**: Query Postgres/Supabase tables without exporting CSV files.
- **Payment & Invoice Auditing**: Check Stripe subscription tiers or customer records on demand.
