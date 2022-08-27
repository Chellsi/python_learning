import requests

# url = 'https://webhook.site/85fe91a0-aae0-4b93-81b6-54651bac27fd'
#
#
# result = requests.request('GET', 'https://www.python.org/')
#
# print(1)
#
#
# with open('example.html', 'wt') as file:
#     file.write(result.text)
#
#
# url = 'https://www.python.org/static/img/python-logo@2x.png'
#
# try:
#     result = requests.request('GET', url)
# except Exception as e:
#     print(e)
# else:
#     if 300 > result.status_code >= 200:
#         if content := result.headers.get('Content-Type'):
#             if content == 'image/png':
#                 with open('logo.png', 'wb') as file:
#                     file.write(result.content)


kuna_url = 'https://api.kuna.io/v3/currencies'

result = requests.request('GET', kuna_url)

print(1)
try:
    res_json = result.json()
except:
    print('Exception')

print(res_json[0])



result = requests.request(
    'POST',
    url,
    headers={
        'X-AUTH': '123456'
    },
    params={
        'q_arg1': 'val1',
        'q_arg2': 'val2',

    },
    json={
        'action': 'login',
        'data': {
            'login': 'asdfgh',
            'password': '54321'
        }
    }
)

print(1)

