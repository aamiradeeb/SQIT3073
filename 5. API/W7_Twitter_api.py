import requests
import json
# Set the bearer token and the search query
bearer_token = "YOUR_BEARER_TOKEN"
query = "#malaysia"
# Set the headers
headers = {
    "Authorization": f"Bearer {bearer_token}",
}
# Set the parameters for the search request
params = {
    "q": query,
    "result_type": "popular",
"count": 1, }
# Make the search request
response = requests.get("https://api.twitter.com/2/tweets/search/recent",
headers=headers, params=params)
# Check the status code of the response
if response.status_code == 200:
    # Parse the JSON data
    data = json.loads(response.text)
    # Get the first tweet from the data
    tweet = data["data"][0]
    # Print the text of the tweet
    print(tweet["text"])
else:
    print("An error occurred")