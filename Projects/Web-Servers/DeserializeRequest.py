import json, ssl
import urllib.request
from RandomCryptoCoin import RandomCryptoCoin

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
cryptocoinURL = "https://random-data-api.com/api/crypto_coin/random_crypto_coin?size=100"

# Create a list to populate with our data
cryptocoins:RandomCryptoCoin = [] 

# Execute HTTP Request
req = urllib.request.Request(cryptocoinURL)
requestData = json.loads(urllib.request.urlopen(req).read())

# Loop over JSON items and Deserialize them into python objects
for r in requestData:  
    # Deserialize 
    cryptocoin:RandomCryptoCoin = RandomCryptoCoin(**r)
    # Add object to list
    cryptocoins.append(cryptocoin) 
    # Print id
    print(cryptocoin.coin_name)