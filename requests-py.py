import requests
payload = {'page': 2, 'count': 24}
# get req
# r = requests.get('https://httpbin.org/get', params=payload, timeout=10) # throw exp if site doesn't reponds even after 10sec



# post req
payload_post = {'username': 'kyto', 'foo': 'bar'}
r = requests.post('https://httpbin.org/post', data=payload_post, timeout=10)
# r = requests.get('image url')
# with open('dlimage.png', 'wb') as file:
  # file.write(r.content)
# print(r.headers)
response_json = r.json()
print(response_json.get('form'))