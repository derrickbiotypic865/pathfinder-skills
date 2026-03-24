# MCP Servers — Hands-On Exercises

MCP (Model Context Protocol) lets Claude connect to external tools and services — databases, file systems, browsers, APIs, and custom tooling. Think of MCP servers as plugins that give Claude new abilities.

---

## Exercise 1: List Your MCP Servers

**What you'll learn:** How to see what MCP servers are configured.

1. In your terminal:
```bash
claude mcp list
```
2. Or inside a Claude session, type `/mcp`
3. You'll see a list of configured servers, their status (connected/disconnected), and available tools

**What to expect:** If you haven't configured any, the list is empty. That's fine — we'll add one next.

**Pro tip:** MCP servers can be configured globally (for all projects) or per-project.

---

## Exercise 2: Add an MCP Server

**What you'll learn:** How to connect an MCP server to Claude.

```bash
# Add a filesystem server (gives Claude access to a specific directory)
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem /path/to/directory

# Add a server with a custom name
claude mcp add my-tools -- npx my-mcp-server

# Add a server with environment variables
claude mcp add my-api --env API_KEY=your-key-here -- npx my-api-server

# Add for just this project (not global)
claude mcp add --scope project my-tools -- npx my-mcp-server
```

**What to expect:** The server starts and its tools appear alongside Claude's built-in tools. You can see them with `/mcp`.

**Pro tip:** Use `--scope project` to keep servers project-specific. Use `--scope user` (default) for servers you want everywhere.

---

## Exercise 3: Use MCP Tools

**What you'll learn:** How to use tools provided by MCP servers.

1. After adding a server, start a Claude session
2. The server's tools are available automatically
3. Just ask Claude to do something the server enables

For example, with a filesystem server:
- "List the files in /path/to/directory"
- "Read the contents of config.yaml"

MCP tool names follow the pattern `mcp__<server-name>__<tool-name>`.

**Pro tip:** You don't need to know the exact tool names — just ask Claude what you want to do and it will find the right MCP tool.

---

## Exercise 4: Load from Config File

**What you'll learn:** How to configure multiple MCP servers from a JSON file.

1. Create a file called `mcp-config.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"],
      "env": {}
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-token"
      }
    }
  }
}
```

2. Launch Claude with the config:
```bash
claude --mcp-config ./mcp-config.json
```

3. Use `--strict-mcp-config` to ONLY use servers from this file:
```bash
claude --strict-mcp-config --mcp-config ./mcp-config.json
```

**Pro tip:** Config files are great for team setups — commit the config (without secrets) and everyone gets the same MCP servers.

---

## Exercise 5: MCP Permissions

**What you'll learn:** How to control which MCP tools Claude can use.

Add to your settings.json:

```json
{
  "permissions": {
    "allow": [
      "mcp__filesystem__read_file",
      "mcp__filesystem__list_directory"
    ],
    "deny": [
      "mcp__filesystem__write_file",
      "mcp__filesystem__delete_file"
    ]
  }
}
```

**Permission patterns:**

| Pattern | What it matches |
|:--------|:---------------|
| `mcp__server-name` | All tools from that server |
| `mcp__server-name__*` | Same — all tools (wildcard) |
| `mcp__server-name__tool-name` | One specific tool |

**Pro tip:** Allow read operations, deny destructive ones. This lets Claude explore and analyze without modifying external systems.

---

## Exercise 6: Remove an MCP Server

**What you'll learn:** How to disconnect a server you no longer need.

```bash
# Remove a server
claude mcp remove filesystem

# List to confirm it's gone
claude mcp list
```

**Pro tip:** Removing a server doesn't uninstall the package — it just disconnects it from Claude.

---

## Quick Reference

| Command | What it does |
|:--------|:-------------|
| `claude mcp add <name> -- <command>` | Add an MCP server |
| `claude mcp remove <name>` | Remove an MCP server |
| `claude mcp list` | List all configured servers |
| `/mcp` | Manage servers in a session |
| `--mcp-config file.json` | Load servers from a config file |
| `--strict-mcp-config` | Only use servers from the config file |

### Permission Patterns

```
mcp__server              — all tools from server
mcp__server__*           — same (wildcard)
mcp__server__tool        — one specific tool
```
