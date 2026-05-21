# Translation B2B Portal

Веб-платформа для автоматизации работы бюро переводов. Проект включает в себя бэкенд на Flask, изолированное виртуальное окружение, REST API для мгновенного расчета стоимости перевода бизнес-документов и поддержку контейнеризации через Docker.

## 🛠 Технологический стек
* **Backend:** Python 3.13 / Flask 3.0.3
* **Environment & Tools:** Python venv, Docker
* **Infrastructure:** Netcup VPS / Ubuntu Server

## 🚀 Архитектура проекта
* `/app/main.py` — Главный файл приложения, логика калькулятора и API-эндпоинты.
* `/requirements.txt` — Список зависимостей проекта.
* `/.gitignore` — Исключение системных файлов из контроля версий Git.
* `/Dockerfile` — Инструкция (чертеж) для сборки Docker-образа.

## 🐳 Запуск через Docker (Рекомендуемый способ)

Для сборки и запуска приложения внутри изолированного контейнера выполните следующие команды:

1. **Соберите Docker-образ:**
   `docker build -t translation-portal .` - После этого интерфейс калькулятора будет доступен по адресу http://<IP_твоего_сервера>:8000. 
2. **Запустите контейнер в фоновом режиме на порту 8000:**
   `docker run -d -p 8000:5000 --name b2b-calculator translation-portal`
   **🔧 Локальный запуск (Без Docker)
   Если вы хотите запустить проект напрямую в операционной системе:
   - Перейдите в папку проекта:`cd ~/translation-b2b-portal`
   - Создайте и активируйте виртуальное окружение:
     `python3 -m venv .venv 
      source .venv/bin/activate`
   - Установите зависимости и запустите сервер:
     `pip install -r requirements.txt
      python3 app/main.py`
   **📡 Примеры использования API**
   Пример запроса (POST через curl):
     `curl -X POST [http://127.0.0.1:8000/api/calculate](http://127.0.0.1:8000/api/calculate) \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello world, this is our amazing translation B2B platform", "lang": "en"}'`
   **Пример успешного ответа (JSON):**
      {
    ` "rate_per_word": 4.0,
      "selected_language": "en",
      "status": "success",
      "total_price": 36.0,
      "words_found": 9
      }`
