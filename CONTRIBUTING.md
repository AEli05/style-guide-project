# Как вносить изменения

## Как предложить изменение

1. Если правка небольшая (опечатка, неудачная формулировка), создайте Issue или сразу Pull Request.
2. Если вы хотите добавить новое правило, сначала опишите его в Issue: какую проблему оно решает и пример «плохо / хорошо».
3. Все изменения попадают в `main` только через Pull Request. Прямые коммиты в `main` не делаем.

Порядок работы:

```bash
git checkout main
git pull
git checkout -b docs/short-description
# правки
git add .
git commit -m "docs: add rule about rounding"
git push -u origin docs/short-description
```

После этого откройте Pull Request на GitHub.

## Оформление коммитов

Используем [Conventional Commits](https://www.conventionalcommits.org/ru/v1.0.0/). Формат:

```text
<тип>(<область>): <короткое описание>
```

| Тип | Когда использовать | Пример |
| --- | --- | --- |
| `docs` | Новый раздел или правка текста руководства | `docs(numbers): add rounding table` |
| `fix` | Исправление ошибки в правиле или примере | `fix(examples): correct p-value in ab report` |
| `style` | Форматирование без изменения смысла | `style: fix list markers` |
| `ci` | Изменения в GitHub Actions | `ci: add markdownlint step` |
| `build` | Настройки MkDocs и зависимости | `build: add tasklist extension` |
| `chore` | Прочее (gitignore и т.д.) | `chore: ignore site folder` |

Правила:

- описание короткое, в повелительном наклонении, без точки в конце;
- один коммит - одно логическое изменение;
- ветку называем по типу изменения: `docs/accessibility`, `fix/glossary-typo`.

## Процесс ревью

1. После открытия Pull Request автоматически запускается проверка: markdownlint, `scripts/check_style.py` и `mkdocs build --strict`. Если проверка красная, сначала исправьте ошибки.
2. Назначьте ревьюера. Ревьюер проверяет изменения по [чек-листу](docs/review.md) и оставляет комментарии: замечания, предложения или вопросы.
3. Автор отвечает на каждый комментарий: исправляет и пишет, в каком коммите, или объясняет, почему оставил как есть.
4. Когда ревьюер нажимает Approve, автор делает merge в `main`.
5. После merge сайт пересобирается и публикуется автоматически. Проверьте, что изменения появились на сайте.

## Как запустить локальную сборку

Нужны Python 3.10+ и (для markdownlint) Node.js.

```bash
pip install -r requirements.txt
mkdocs serve
```

Сайт будет доступен на <http://127.0.0.1:8000> и обновляется при сохранении файлов.

Проверки, которые запускаются в CI:

```bash
python scripts/check_style.py
npx markdownlint-cli2
mkdocs build --strict
```

## Как добавить новый раздел

1. Создайте файл в папке `docs/`, например `docs/accessibility.md`. Первая строка - заголовок первого уровня.
2. Добавьте раздел в навигацию в `mkdocs.yml`, в блок `nav`:

    ```yaml
    nav:
      - Оформление:
          - Доступность текста: accessibility.md
    ```

3. Добавьте строку в таблицу разделов на главной странице `docs/index.md`.
4. Запустите локальную сборку и проверки.
5. Сделайте коммит с типом `docs` и откройте Pull Request.
