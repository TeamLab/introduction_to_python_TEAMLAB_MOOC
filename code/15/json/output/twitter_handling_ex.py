
consumer_key = 'QTWaIgaMpRyXULUt67JzamiS9'
consumer_secret = 'Ux4EYBYbLhMFgj3GPkoTo9ZT2Dxd1sOVHJX3Om9JKCP3TjRd7I'
access_token = '63969436-3RamHxJl4OTfLvUzfUfLbBER1g1QDVK9P8oKYiMMQ'
access_token_secret = 'SqKjP7AHI4BeKdTuLUZ7Awus5tywbZG6Mb5xkhyPv23Ct'

oauth = OAuth1(client_key=consumer_key, client_secret=consumer_secret,
               resource_owner_key=access_token, resource_owner_secret=access_token_secret)


# Twitter REST api // screen_name 은 트위터 계정명
url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={0}'.format('fcseoul')
r = requests.get(url=url,auth=oauth)
statuses =  r.json()

for status in statuses:
    print (status['text'], status['created_at'])