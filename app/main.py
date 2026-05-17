from flask import Flask, render_template, request, jsonify

app = Flask(__name__, 
            template_folder='templates', 
            static_folder='static')

# Базовые тарифы за перевод одного слова (в рублях)
TARIF_RATES = {
    "en": 4.0,  # Английский
    "ar": 6.0,  # Арабский
    "zh": 8.0   # Китайский
}

@app.route('/')
def home():
    """Главная страница портала"""
    return "<h1>Бюро переводов: Бэкенд калькулятора успешно запущен!</h1>"

@app.route('/api/calculate', methods=['POST'])
def calculate():
    """API-эндпоинт для расчета стоимости перевода"""
    data = request.get_json() or {}
    text = data.get("text", "")
    lang = data.get("lang", "en")
    
    # Считаем количество слов, разбивая строку по пробелам
    word_count = len(text.split())
    
    # Получаем тариф для выбранного языка (если языка нет — берем дефолтный английский)
    rate = TARIF_RATES.get(lang, 4.0)
    total_price = word_count * rate
    
    return jsonify({
        "status": "success",
        "words_found": word_count,
        "selected_language": lang,
        "rate_per_word": rate,
        "total_price": total_price
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
