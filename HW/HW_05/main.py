import aiohttp
import asyncio
import argparse
import datetime

async def get_exchange_rates(date):
    url = f"https://api.privatbank.ua/p24api/exchange_rates?date={date}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                raise Exception(f"Помилка запиту. Код відповіді: {response.status}")

async def get_currency_rates(days, currency):
    try:
        for i in range(days):
            date = (datetime.date.today() - datetime.timedelta(days=i)).strftime("%d.%m.%Y")
            data = await get_exchange_rates(date)
            currency_rate = next(item for item in data["exchangeRate"] if item["currency"] == currency)
            print(f"Дата: {date}, Курс {currency}: {currency_rate['purchaseRate']}")
    except Exception as e:
        print(f"Помилка: {e}")

def main():
    parser = argparse.ArgumentParser(description="Отримати курс EUR та USD ПриватБанку за останні дні.")
    parser.add_argument("days", type=int, help="Кількість днів для отримання курсів (максимум 10)")
    args = parser.parse_args()
    days = args.days

    if days > 10:
        print("Запит не повинен перевищувати 10 днів. Буде виведено результат за 10 днів.")
        days = 10

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_currency_rates(days, "USD"))
    loop.run_until_complete(get_currency_rates(days, "EUR"))
    


if __name__ == "__main__":
    main()
