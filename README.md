# Claude Agents

282 агента-специалиста из [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) (лицензия MIT, см. `LICENSE`).

- `.claude/agents/` — сабагенты для Claude Code. Работают в любой сессии Claude Code (в том числе облачной) с этим репозиторием.
- `skill/agency-agents/` — те же агенты в виде навыка (Skill) для claude.ai и приложения Claude. Чтобы установить: заархивируйте папку в zip и загрузите в Настройки → Возможности → Навыки.

## Обновление

```bash
git clone --depth 1 https://github.com/msitarzewski/agency-agents /tmp/aa
rm -f .claude/agents/*.md && cp /tmp/aa/*/*.md .claude/agents/ 2>/dev/null
# либо: /tmp/aa/scripts/install.sh --tool claude-code --path .claude/agents
```
