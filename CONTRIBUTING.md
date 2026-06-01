# Contributing to founder-os

Thanks for being here. founder-os is a system you *fork and make yours* — so "contributing" means two different things, and both are welcome.

## 1. Improving your own copy
This is the main use. Clone it, run `/setup`, and adapt the agents, skills, and protocols to how *your* company actually works. You don't need permission for that — it's the point. If you build something genuinely reusable (a new agent, a sharper skill), consider sending it back upstream.

## 2. Contributing back to the template
Good candidates:
- **New agents or skills** that generalize to most B2B SaaS companies (not your-company-specific).
- **Fixes** to commands, protocols, or docs.
- **Translations** (the system core is Italian; English help is welcome).
- **Examples** beyond `examples/acme-demo/`.

### Ground rules
- **Keep it generic.** Anything merged into the template must be free of real company data, names, customers, or credentials. Use `{{PLACEHOLDERS}}` and neutral examples (`Acme`, `Partner X`).
- **No secrets.** Never commit `.env`, API keys, tokens, workspace IDs, or personal data. `.mcp.json` uses `${ENV_VAR}` only.
- **Respect the structure.** New outputs go to the folders defined in `CLAUDE.md` (§ Output rules). New agents follow the `.agents/<role>/AGENT.md` + `commands/` + `templates/` pattern.
- **Log system changes.** Edits to `.agents/`, `.skills/`, `.workflows/`, `CLAUDE.md`, or `system/protocols/` need a `system/CHANGELOG.md` entry in the same PR (see `system/protocols/system-changelog.md`).
- **Markdown only.** This is a docs-as-code system. No build step, no runtime — just files Claude reads.

### Workflow
1. Fork → branch (`feat/<thing>` or `fix/<thing>`).
2. Make the change, keep it generic, add a CHANGELOG entry if it's a system file.
3. Run a quick leak check before pushing:
   ```bash
   git ls-files -z | xargs -0 grep -inE "acme is fine, but grep your own company name here" || true
   ```
4. Open a PR with a short "what + why".

### Questions
Open an issue. Use the templates in `.github/ISSUE_TEMPLATE/` for feature requests and strategic-decision discussions.

— Built with [Claude Code](https://claude.com/claude-code). MIT licensed.
