import requests

# py request-post.py to make a GET request to the app
req = requests.get("http://127.0.0.1:8080/post", data={'GET': 'SOMETHING'})

print(req.text)  # displays the result body.
