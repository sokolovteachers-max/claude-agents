# Claude Agents

282 агента-специалиста из [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) (лицензия MIT, см. `LICENSE`).

- `.claude/agents/` — сабагенты для Claude Code. Работают в любой сессии Claude Code (в том числе облачной) с этим репозиторием.
- `skill/agency-agents/` — те же агенты в виде навыка (Skill) для claude.ai и приложения Claude. Чтобы установить: заархивируйте папку в zip и загрузите в Настройки → Возможности → Навыки.

## Автообновление

GitHub Action `.github/workflows/sync.yml` каждый понедельник забирает свежие агенты из оригинального репозитория, обновляет `.claude/agents/` и `skill/agency-agents/` и выкладывает готовый `agency-agents-skill.zip` в релиз [skill-latest](../../releases/tag/skill-latest). Запустить вручную: вкладка Actions → Sync agents → Run workflow.

Навык в claude.ai обновляется вручную: скачайте zip из релиза и загрузите заново (Настройки → Возможности → Навыки).
