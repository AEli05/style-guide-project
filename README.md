# style-guide-project

Руководство по стилю аналитической документации: отчеты по A/B-тестам, описания SQL-витрин и описания дашбордов.

Проект сделан по методологии Docs as Code: тексты в Markdown, сайт собирается MkDocs, изменения проходят через Pull Request, линтер и автоматический деплой на GitHub Pages.

- Сайт: <https://AEli05.github.io/style-guide-project/>
- Как предложить изменение: [CONTRIBUTING.md](CONTRIBUTING.md)

## Структура

```text
docs/                 разделы руководства
docs/examples/        документы, написанные по руководству
scripts/check_style.py  проверка текста на правила стайлгайда
.markdownlint-cli2.yaml настройки markdownlint
.github/workflows/    CI/CD: линтинг, сборка, деплой
mkdocs.yml            настройки сайта и навигация
```

## Быстрый старт

```bash
pip install -r requirements.txt
mkdocs serve
```

Сайт откроется на <http://127.0.0.1:8000>.
