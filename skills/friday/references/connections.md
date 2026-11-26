# Service connection setup

Read only when Gmail, Google Calendar, or Asana tools are missing or authorization fails. Working connections do not need setup. Use the requested service/account; never request passwords/tokens in chat, copy credentials between hosts, or switch accounts to bypass a failure.

## Codex

Connect the requested Gmail, Google Calendar, or Asana service through [Plugins](https://chatgpt.com/plugins), complete OAuth for the intended account, then open a new conversation and retry the workflow's read verification.

## Claude Code

For a claude.ai login, authorize the requested service through [Claude Connectors](https://claude.ai/customize/connectors), restart Claude Code, and inspect `/mcp`. Use `/status` to check the login method. Authorize Anthropic-hosted connectors through their connection page rather than registering their URL as a local MCP server.

API-key/other-provider sessions require supported connector/MCP setup; see [Claude MCP authorization](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claudeai). For self-managed Asana MCP, use [Asana's connection guide](https://developers.asana.com/docs/connecting-mcp-clients-to-asanas-v2-server); Friday does not create OAuth apps or handle secrets in conversation.

## Return to the workflow

Verify access again with a small read before continuing. Do not test access with writes. A missing connection means unknown data/availability, not an empty inbox/project or a free calendar. Finish independent work and state remaining gaps. Connection setup grants no permission to change mail, events, or tracker data.
