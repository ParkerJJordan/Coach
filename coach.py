import requests


result = requests.post(
    'https://wger.de/api/v2/token',
    data={'username': 'user', 'password': 'admin'}
)
access_token = result.json()['access']
refresh_token = result.json()['refresh']

print(result.json())

result = requests.get(
    'https://wger.de/api/v2/workout/',
    headers={'Authorization': f'Bearer {access_token}'}
)

print(result.json())

result = requests.post('https://wger.de/api/v2/token/verify', data={'token': access_token})

result = requests.post(
    'https://wger.de/api/v2/token/refresh/',
    data={'refresh': refresh_token}
)
token = result.json()

print(token)