import requests 

token = '8944643813:AAEg9scFKMLSQxrk9G5GhS4H6RWo48xz0OA'
method = "sendMessage"
url = f'https://api.telegram.org/bot{token}/{method}'
data = {
    'text' : 'salom',
    'chat_id' : 5873838700
}

requests.post(url=url, json=data)
