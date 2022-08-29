import requests
from datetime import date

url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
file_currency = 'file_currency.txt'


def update_currency():
    try:
        result = requests.request('GET', url)
        result_list = result.json()
    except Exception as e:
        print(e)
    else:
        if 300 > result.status_code >= 200:
            with open(file_currency, 'at') as file:
                file.write(f'"[{date.today()}]"\n')
                for currency in result_list:
                    file.write(f'[{currency.get("txt")}] to UAH: [{currency.get("rate")}]\n')


if __name__ == '__main__':
    update_currency()

