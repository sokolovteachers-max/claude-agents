"""Собирает навык agency-agents для claude.ai из репозитория msitarzewski/agency-agents.

claude.ai принимает zip не более чем из 200 файлов, поэтому агенты одного
раздела склеиваются в один файл agents/<раздел>.md, а CATALOG.md хранит
диапазон строк каждого агента.

Использование: python3 build_skill.py <путь к agency-agents> <папка навыка>
"""
import os, re, sys, shutil
repo, out = sys.argv[1], sys.argv[2]
divs = ["academic","design","engineering","finance","game-development","gis","healthcare","marketing","paid-media","product","project-management","research","sales","security","spatial-computing","specialized","support","testing"]
shutil.rmtree(out, ignore_errors=True)
os.makedirs(f"{out}/agents")
cat = ["# Каталог агентов (The Agency)\n", "Формат: Имя — `agents/<раздел>.md` строки N–M — описание.\n"]
total = 0
orchestrator = ""
for d in divs:
    agents = []
    for root, _, files in os.walk(f"{repo}/{d}"):
        for fn in files:
            if not fn.endswith(".md") or fn == "README.md": continue
            txt = open(os.path.join(root, fn), encoding="utf-8").read()
            m = re.match(r"---\n(.*?)\n---", txt, re.S)
            if not m: continue
            fm = dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M))
            if "name" not in fm: continue
            agents.append((fm["name"].strip('"'), fm.get("description", "").strip('"'), txt.rstrip("\n")))
    agents.sort()
    total += len(agents)
    path = f"agents/{d}.md"
    lines, rows = [], []
    for name, desc, txt in agents:
        lines.append(f"<!-- ===== AGENT: {name} ===== -->")
        start = len(lines) + 1
        lines += txt.split("\n")
        rows.append(f"- {name} — `{path}` строки {start}–{len(lines)} — {desc}")
        if name == "Agents Orchestrator":
            orchestrator = f"`{path}` строки {start}–{len(lines)}"
        lines.append("")
    open(f"{out}/{path}", "w", encoding="utf-8").write("\n".join(lines))
    cat.append(f"\n## {d} ({len(agents)})\n")
    cat += rows
open(f"{out}/CATALOG.md", "w", encoding="utf-8").write("\n".join(cat) + "\n")
sections = "\n".join("- " + l.strip().lstrip("# ") for l in cat if l.startswith("\n## "))
open(f"{out}/SKILL.md", "w", encoding="utf-8").write(f"""---
name: agency-agents
description: Library of {total} expert personas (The Agency) — engineering, design, marketing, ads, sales, product, management, testing, security, finance, legal, HR, games, GIS, science, healthcare, support. USE PROACTIVELY for almost any substantive request, even when the user does not mention agents or experts: writing or reviewing code, architecture, debugging, UI/UX, texts and content, SEO, social media, ads, sales, emails, pricing, strategy, business plans, product and project planning, analytics, finance, taxes, contracts, HR, hiring, resumes, training, research, security, games, data, documents. Pick the best-matching specialist yourself and answer in that role. Skip only for small talk, trivial facts or very short replies.
---

# The Agency — {total} агентов-специалистов

Это библиотека ролей. Агенты лежат в `agents/<раздел>.md` — по одному файлу на раздел, внутри агенты идут подряд, каждый начинается со строки `<!-- ===== AGENT: Имя ===== -->`. У каждого агента — личность, экспертиза, рабочие процессы, форматы результатов и метрики успеха.

## Как работать

1. Сам определи, какой специалист лучше всего подходит под запрос — пользователь не обязан называть агента и не должен об этом просить. Не спрашивай, какого агента взять: выбери сам. Если пользователь назвал агента — используй его. Если подходящего агента нет — отвечай как обычно, без навыка.
2. Найди его в `CATALOG.md` (разделы по направлениям; у каждого агента имя, файл, диапазон строк и описание). Можно искать по ключевым словам.
3. Прочитай только его диапазон строк из файла раздела (например, `sed -n 'N,Mp' agents/engineering.md` или просмотр файла с указанием строк) — не весь файл. Действуй строго в этой роли: его подход, процессы, формат результатов, стиль общения.
4. Отвечай на языке пользователя (по умолчанию — по-русски), даже если описание агента на английском.
5. Кратко скажи в начале, какой агент взят в работу (эмодзи + имя), например «🖥️ Frontend Developer».
6. Если задача комплексная — собери команду из 2–4 агентов: прочитай их описания, выполни работу по очереди от каждой роли и сведи итог. Для координации есть Agents Orchestrator ({orchestrator}).
7. Если пользователь просит «какие есть агенты» — покажи разделы и нужные части каталога.

## Разделы

{sections}
""")
print(total)
