# SQL и код

## Где размещать код

- Короткий запрос (до 30 строк) - в документе, в блоке кода.
- Длинный запрос или ноутбук - в репозитории, в документе ссылка на файл.
- Перед блоком кода одно предложение: что делает запрос. После - что должно получиться.

## Оформление SQL

- Ключевые слова заглавными: `SELECT`, `FROM`, `WHERE`.
- Сложную логику разбиваем на CTE (`WITH`) с понятными именами.
- Каждое поле в `SELECT` на отдельной строке.
- Таблицы указываем вместе со схемой: `dm.app_events`.
- Фильтры, которые влияют на результат, комментируем.

```sql
-- конверсия в заявку по группам теста за период
WITH users AS (
    SELECT
        user_id,
        ab_group
    FROM dm.ab_assignments
    WHERE test_id = 'new_application_screen'
      AND is_test_account = 0 -- исключаем тестовые аккаунты
),
applications AS (
    SELECT DISTINCT user_id
    FROM dm.app_events
    WHERE event_name = 'application_submitted'
      AND event_date BETWEEN '2026-09-01' AND '2026-09-30'
)
SELECT
    u.ab_group,
    COUNT(*) AS users_cnt,
    COUNT(a.user_id) AS applications_cnt,
    COUNT(a.user_id) * 1.0 / COUNT(*) AS conversion
FROM users AS u
LEFT JOIN applications AS a
    ON u.user_id = a.user_id
GROUP BY u.ab_group;
```

Результат: по одной строке на группу, конверсия в долях.

## Имена в тексте

Имена таблиц, полей, файлов и параметров пишем в моноширинном шрифте и не переводим: поле `ab_group`, файл `metrics.sql`.

## Безопасность данных

- В документах нет персональных данных клиентов: ФИО, телефонов, номеров договоров.
- Примеры строк из таблиц показываем на обезличенных данных.
- Пароли, токены и строки подключения в документы не попадают.
