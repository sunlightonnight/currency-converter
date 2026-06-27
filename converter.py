while True:
    import requests

    url = "https://api.exchangerate-api.com/v4/latest/USD"

    response = requests.get(url)
    data = response.json()

    rates = data["rates"] 

    print("\nВведите код валюты (RUB, EUR, KZT) или 'ВЫХОД'")
    valute = (input("Введите валюту:")).upper()
    if valute == "ВЫХОД":
        print("Выход")
        break
    elif valute in rates:
        amount = float(input(f"Введите сумму в {valute}:"))
        result = amount * rates["RUB"] / rates[valute]
        print(f"{amount} {valute} = {result:.2f} RUB")
    else:
        print("Такой валюты нет")