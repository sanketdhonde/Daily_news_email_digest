import requests
from send_email import send_email

topic = "tesla"
api_key = "5783549b55ce44f5871f6264e06bdab8"
url ="https://newsapi.org/v2/everything?" \
     f"q={topic}" \
     "&from=2024-05-26&" \
     "sortBy=publishedAt&apiKey=5783549b55ce44f5871f6264e06bdab8&" \
     "language=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
     if article["title"] is not None:
         body = "Subject = todays news" + "\n" + body + \
               article["title"] + "\n" + \
               article["url"] \
               + article["description"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message =body)
