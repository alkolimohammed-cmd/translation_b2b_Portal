# Translation B2B Portal

Веб-платформа для автоматизации работы бюро переводов. Проект включает в себя бэкенд на Flask, изолированное окружение и REST API для мгновенного расчета стоимости перевода бизнес-документов.

## 🛠 Технологический стек
* **Backend:** Python 3.13 / Flask 3.0.3
* **Environment:** Python venv
* **Infrastructure:**  VPS / Ubuntu Server

## 🚀 Архитектура проекта
* `/app/main.py` — Главный файл приложения, логика калькулятора и API-эндпоинты.
* `/requirements.txt` — Список зависимостей проекта (фиксированные версии библиотек).
* `/.gitignore` — Исключение системных файлов и виртуального окружения из контроля версий.

## 🔧 Локальный запуск и развертывание

1. **Клонируйте репозиторий и перейдите в папку проекта:**
   ```bash
   cd ~/translation-b2b-portal
2. **Создайте и активируйте виртуальное окружение:**
   python3 -m venv .venv
   source .venv/bin/activate
3. **Создайте и активируйте виртуальное окружение:**
   python3 -m venv .venv
   source .venv/bin/activate
4. **Запустите сервер разработки Flask:**
   python3 app/main.py
 ## 📡 Примеры использования API
Приложение предоставляет эндпоинт /api/calculate для расчета стоимости по количеству слов.
 ## Пример запроса (POST):
   curl -X POST [http://127.0.0.1:5000/api/calculate](http://127.0.0.1:5000/api/calculate) \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello world, this is our amazing translation B2B platform", "lang": "en"}'
 ## Пример ответа от бэкенда:
   {
  "rate_per_word": 4.0,
  "selected_language": "en",
  "status": "success",
  "total_price": 36.0,
  "words_found": 9
}
