while True:
    import requests

    url = "https://api.exchangerate-api.com/v4/latest/USD"

    response = requests.get(url)
    data = response.json()

    rates = data["rates"] 

    print("\nВведите код валюты (USD, EUR, KZT) или 'ВЫХОД'")
    valute = input("Введите валюту: ").upper()

    if valute == "ВЫХОД":
        print("Выход из программы.")
        break
    elif valute in rates:
        while True:
            try:
                amount = float(input(f"Введите сумму в {valute}: "))
                break
            except ValueError:
                print("Ошибка! Нужно ввести число. Попробуйте снова.")
        result = amount * rates["RUB"] / rates[valute]
        print(f"{amount} {valute} = {result:.2f} RUB")
    else:
        print("Такой валюты нет")