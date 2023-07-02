import requests
from random import randrange

TEST_URL = ["google.com", "facebook.com", "twitter.com", "amazon.com", "apple.com"]

i = randrange(5) # add randomiser

print(TEST_URL[i])
res = requests.get(f"https://{TEST_URL[i]}/")
print(f"Response status code is {res.status_code}")
print(f"Response len is {len(res.content)}")
