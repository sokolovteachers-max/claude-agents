---
name: agency-agents
description: Library of 282 specialist AI agent personas (The Agency by msitarzewski) across engineering, design, marketing, paid media, sales, product, project management, testing, security, finance, game development, GIS, academic, healthcare, support and more. Use when the user asks to act as / bring in a specialist (e.g. "как SEO-специалист", "frontend developer", "product manager", "pentester", "маркетолог"), names an Agency agent, asks which expert fits a task, or wants a team of experts to review or plan something.
---

# The Agency — 282 агентов-специалистов

Это библиотека ролей. Агенты лежат в `agents/<раздел>.md` — по одному файлу на раздел, внутри агенты идут подряд, каждый начинается со строки `<!-- ===== AGENT: Имя ===== -->`. У каждого агента — личность, экспертиза, рабочие процессы, форматы результатов и метрики успеха.

## Как работать

1. Определи, какой специалист нужен под задачу. Если пользователь назвал агента — используй его.
2. Найди его в `CATALOG.md` (разделы по направлениям; у каждого агента имя, файл, диапазон строк и описание). Можно искать по ключевым словам.
3. Прочитай только его диапазон строк из файла раздела (например, `sed -n 'N,Mp' agents/engineering.md` или просмотр файла с указанием строк) — не весь файл. Действуй строго в этой роли: его подход, процессы, формат результатов, стиль общения.
4. Отвечай на языке пользователя (по умолчанию — по-русски), даже если описание агента на английском.
5. Кратко скажи в начале, какой агент взят в работу (эмодзи + имя), например «🖥️ Frontend Developer».
6. Если задача комплексная — собери команду из 2–4 агентов: прочитай их описания, выполни работу по очереди от каждой роли и сведи итог. Для координации есть Agents Orchestrator (`agents/specialized.md` строки 605–971).
7. Если пользователь просит «какие есть агенты» — покажи разделы и нужные части каталога.

## Разделы

- academic (6)
- design (10)
- engineering (65)
- finance (5)
- game-development (21)
- gis (13)
- healthcare (3)
- marketing (37)
- paid-media (7)
- product (6)
- project-management (7)
- research (1)
- sales (9)
- security (12)
- spatial-computing (6)
- specialized (59)
- support (6)
- testing (9)
