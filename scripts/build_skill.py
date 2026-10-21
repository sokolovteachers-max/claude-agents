"""Собирает навык agency-agents для claude.ai из репозитория msitarzewski/agency-agents.

Использование: python3 build_skill.py <путь к agency-agents> <папка навыка>
"""
import os, re, sys, json, shutil
repo, out = sys.argv[1], sys.argv[2]
divs = ["academic","design","engineering","finance","game-development","gis","healthcare","marketing","paid-media","product","project-management","research","sales","security","spatial-computing","specialized","support","testing"]
shutil.rmtree(out, ignore_errors=True)
os.makedirs(f"{out}/agents")
cat = ["# Каталог агентов (The Agency)\n", "Формат: `файл` — Имя — описание. Файл лежит в `agents/`.\n"]
total = 0
for d in divs:
    rows = []
    for root, _, files in os.walk(f"{repo}/{d}"):
        for fn in files:
            if not fn.endswith(".md") or fn == "README.md": continue
            p = os.path.join(root, fn); txt = open(p, encoding="utf-8").read()
            m = re.match(r"---\n(.*?)\n---", txt, re.S)
            if not m: continue
            fm = dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M))
            if "name" not in fm: continue
            dest = fn if fn.startswith(d) else f"{d}-{fn}"
            shutil.copy(p, f"{out}/agents/{dest}")
            rows.append((fm["name"].strip('"'), dest, fm.get("description","").strip('"')))
    rows.sort()
    total += len(rows)
    cat.append(f"\n## {d} ({len(rows)})\n")
    cat += [f"- `{f}` — {n} — {ds}" for n, f, ds in rows]
open(f"{out}/CATALOG.md","w",encoding="utf-8").write("\n".join(cat)+"\n")
sections = "\n".join("- " + l.strip().lstrip("# ") for l in cat if l.startswith("\n## "))
open(f"{out}/SKILL.md","w",encoding="utf-8").write(f"""---
name: agency-agents
description: Library of {total} specialist AI agent personas (The Agency by msitarzewski) across engineering, design, marketing, paid media, sales, product, project management, testing, security, finance, game development, GIS, academic, healthcare, support and more. Use when the user asks to act as / bring in a specialist (e.g. "как SEO-специалист", "frontend developer", "product manager", "pentester", "маркетолог"), names an Agency agent, asks which expert fits a task, or wants a team of experts to review or plan something.
---

# The Agency — {total} агентов-специалистов

Это библиотека ролей. Каждый агент — markdown-файл в `agents/` с личностью, экспертизой, рабочими процессами, форматами результатов и метриками успеха.

## Как работать

1. Определи, какой специалист нужен под задачу. Если пользователь назвал агента — используй его.
2. Найди его в `CATALOG.md` (разделы по направлениям, у каждого агента файл, имя и описание). Можно искать по ключевым словам.
3. Прочитай целиком файл агента `agents/<файл>` и действуй строго в этой роли: его подход, процессы, формат результатов, стиль общения.
4. Отвечай на языке пользователя (по умолчанию — по-русски), даже если файл агента на английском.
5. Кратко скажи в начале, какой агент взят в работу (эмодзи + имя), например «🖥️ Frontend Developer».
6. Если задача комплексная — собери команду из 2–4 агентов: прочитай их файлы, выполни работу по очереди от каждой роли и сведи итог. Для координации есть `agents/specialized-agents-orchestrator.md`.
7. Если пользователь просит «какие есть агенты» — покажи разделы и нужные части каталога.

## Разделы

{sections}
""")
print(total)
