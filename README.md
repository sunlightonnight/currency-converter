# Конвертер валют / Currency converter

Простой конвертер валют на Python. Использует API ExchangeRate для получения актуальных курсов.

A simple currency converter in Python. Uses the ExchangeRate API to get live exchange rates.

---

## Как запустить / How to run

1. Установи Python 3 и библиотеку `requests`: `pip install requests` / Install Python 3 and the `requests` library: `pip install requests`
2. Скачай файл `converter.py` / Download `converter.py`
3. Запусти в терминале: `python converter.py` / Run in terminal: `python converter.py`

---

## Команды / Commands

- Введи код валюты (USD, EUR, KZT) или `ВЫХОД` для выхода / Enter currency code (USD, EUR, KZT) or `EXIT` to quit.
- Введи сумму / Enter the amount.
- Программа переведёт в рубли / The program converts to RUB.

---

## Пример / Example

Введите код валюты (USD, EUR, KZT) или 'ВЫХОД'
Введите валюту: USD
Введите сумму в USD: 100
100.0 USD = 8512.50 RUB

---

## Код / Code

```python
import requests

print("Введите код валюты (USD, EUR, KZT) или 'ВЫХОД'")

while True:
    valute = input("Введите валюту: ").upper()
    
    if valute == "ВЫХОД":
        print("Выход из конвертера.")
        break
    
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    rates = data["rates"]
    
    if valute not in rates:
        print("Такой валюты нет. Попробуй снова.")
        continue
    
    try:
        amount = float(input(f"Введите сумму в {valute}: "))
        result = amount * rates["RUB"] / rates[valute]
        print(f"{amount} {valute} = {result:.2f} RUB")
    except ValueError:
        print("Ошибка! Нужно ввести число.")
```
## Author / Автор

**sunlightonnight**

---

## License / Лицензия

MIT
