from curl_cffi import requests

TOKEN = 'f76475250462cdf3941dd438edcba9747a244278'
HEADERS = {'Authorization': f'Token {TOKEN}', 'Accept': 'application/json'}

# Test 1: Events nikaalein
r = requests.get(
    'https://sports.bzzoiro.com/api/v2/events/?format=json',
    headers=HEADERS,
    params={'league_id': 3},
    impersonate='chrome'
)
print('Events Status:', r.status_code)
data = r.json()
print('Total events:', data.get('count'))
events = data.get('results', [])
print('First event:', events[0] if events else 'None')

# Test 2: Pehle event ka incidents nikaalein
if events:
    event_id = events[0]['id']
    print(f'\nTesting event_id: {event_id}')
    r2 = requests.get(
        f'https://sports.bzzoiro.com/api/v2/events/{event_id}/incidents/?format=json',
        headers=HEADERS,
        impersonate='chrome'
    )
    print('Incidents Status:', r2.status_code)
    print(r2.text[:500])