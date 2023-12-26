# Апи расписания для сайта rasp.pskgu.ru
Базируется на MongoDB, которая используется в проекте ["Бот ПсковГУ"](https://github.com/mrgick/pskgu_api).

Основная цель – использование апи для [альтернативного сайта расписания](https://github.com/mrgick/rasp_pskgu) 
# Запуск

Запуск вручную
```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app
```

## Настройки
в файле config.py прописаны настройки проекта.

Для запуска нужно создать переменные среды:
```bash
export MONGO_URL="mongodb://localhost:27017"
export URL_PING="http://127.0.0.1:8000/ping"
```

# Особенности
- Используется MongoDB для хранения записей о расписании.
- Используется кеширование записей в базе данных.
- Используется FastApi с SlowApi для ограничения нагрузки (максимально - 5 запросов в секунду).

> p.s. для работы в heroku/render нужен cron - авто пинг сайта

# Полезные ссылки

- [группа вк](https://vk.com/pskgu_bot)
- ["Бот ПсковГУ"](https://github.com/mrgick/pskgu_api)
- [альтернативный сайт расписания](https://github.com/mrgick/rasp_pskgu)
