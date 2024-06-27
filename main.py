import requests

api_key = "5783549b55ce44f5871f6264e06bdab8"
url ="https://newsapi.org/v2/everything?q=tesla&" \
     "from=2024-05-26&sortBy=publishedAt&" \
     "apiKey=5783549b55ce44f5871f6264e06bdab8"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
     print(article["title"])
     print(article["description"])
