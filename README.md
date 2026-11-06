# Study Project — CI & Модульное тестирование

## Структура проекта

```
study_project/
├── .github/
│   └── workflows/
│       └── ci.yml              # Конфигурация GitHub Actions
├── calculator.py               # Код с намеренными багами
├── test_calculator.py           # Модульные тесты (pytest)
├── requirements.txt             # Зависимости
├── .gitignore                   # Исключения для Git
└── README.md                    # Этот файл
```

## Установка

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск тестов локально

```bash
pytest test_calculator.py -v
```

## Проверка покрытия

```bash
pytest test_calculator.py --cov=calculator --cov-report=term-missing
```

## Статус CI

[![CI Pipeline](https://github.com/FapV1r/study_teleBot/actions/workflows/ci.yml/badge.svg)](https://github.com/FapV1r/study_teleBot/actions/workflows/ci.yml)

## Известные баги в calculator.py

При первом пуше CI упадёт из-за трёх багов:

| Метод | Баг | Ожидаемое поведение |
|-------|-----|---------------------|
| `subtract(a, b)` | Возвращает `b - a` | Должен возвращать `a - b` |
| `multiply(a, b)` | Всегда возвращает `4.0` | Должен возвращать `a * b` |
| `divide(a, 0)` | Возвращает `0.0` | Должен выбрасывать `ValueError` |

## Как исправить

1. **subtract**: заменить `return b - a` → `return a - b`
2. **multiply**: заменить `return 4.0` → `return a * b`
3. **divide**: заменить `return 0.0` → `raise ValueError("Деление на ноль невозможно")`

После исправлений запустите тесты повторно:
```bash
pytest test_calculator.py -v
```
