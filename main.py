import json
import requests


def main(event, context):
    update = json.loads(event['body'])
    text = update['message']['text']
    lat, lon = text.split()
    id = update['message']['chat']['id']
    token = "0ee6eefdb5cc2a7cdfea1bdf123fd5502eccf999"
    response = requests.post('https://suggestions.dadata.ru/suggestions/api/4_1/rs/geolocate/address', json={
        'lat': lat, 'lon': lon}, headers={
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json',
    })
    if response:
        suggestions = response.json()['suggestions']
        if len(suggestions) != 0:
            text = ""
            for s in suggestions:
                text += s['value'] + "\n"
        else:
            text = 'Ничего не найдено'

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(
            {
                'method': 'sendMessage',
                'chat_id': id,
                'text': text
            }
        )
    }
