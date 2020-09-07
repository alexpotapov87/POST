import requests

# py request-post.py to make a POST request to the app
# Please, paste the IP address of vHost if your virtualization in subnested
req = requests.post("http://127.0.0.1:8080/post",
                    data={'POST_REQUEST': 'POST_VALUE'})

print(req.text)  # displays the result body.
