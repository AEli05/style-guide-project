"""Проверка текстов документации на правила стайлгайда.

markdownlint проверяет разметку, а этот скрипт - сам текст:
букву е без точек, дефис вместо длинного тире, кавычки и запрещенные обороты.
Текст в блоках кода и в `инлайн-коде` не проверяется.

Запуск: python scripts/check_style.py
"""

import re
import sys
from pathlib import Path

FILES = sorted(Path("docs").rglob("*.md")) + [Path("README.md"), Path("CONTRIBUTING.md")]

RULES = [
    (re.compile("[\u0451\u0401]"), "две точки над е: пишем просто е (раздел 'Орфография и пунктуация')"),
    (re.compile("[\u2014\u2013]"), "длинное или среднее тире: используем дефис -"),
    (re.compile("[\u201c\u201d\u201e]"), "типографские кавычки: используем «елочки» или прямые"),
    (re.compile(r"\bв ходе\b", re.I), "канцелярит 'в ходе'"),
    (re.compile(r"\bбыло установлено\b", re.I), "канцелярит 'было установлено'"),
    (re.compile(r"\bследует отметить\b", re.I), "канцелярит 'следует отметить'"),
    (re.compile(r"\bосуществл\w*", re.I), "канцелярит 'осуществлять'"),
    # только единственное число, чтобы не ловить слово "данные" в смысле data
    (re.compile(r"\bданн(ый|ая|ое|ого|ой|ом|ую)\b", re.I), "канцелярит 'данный'"),
    (re.compile(r"\bв рамках\b", re.I), "канцелярит 'в рамках'"),
]

INLINE_CODE = re.compile(r"`[^`]*`")


def check_file(path: Path) -> list[str]:
    errors = []
    in_code_block = False
    for num, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        text = INLINE_CODE.sub("", line)
        for pattern, message in RULES:
            if pattern.search(text):
                errors.append(f"{path}:{num}: {message}")
    return errors


def main() -> int:
    errors = []
    for path in FILES:
        if path.exists():
            errors.extend(check_file(path))
    for err in errors:
        print(err)
    if errors:
        print(f"\nНайдено нарушений: {len(errors)}")
        return 1
    print("Проверка стиля пройдена")
    return 0


if __name__ == "__main__":
    sys.exit(main())
