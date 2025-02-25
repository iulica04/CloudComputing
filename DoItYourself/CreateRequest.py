# o it yourself:
#
# Create a program (Python, Node Js or any language you like) that sends HTTP requests to one of the following APIs (or any other you would like):
#
# https://www.virustotal.com/en/documentation/public-api/
# http://www.splashbase.co/api#images_random
# https://api.random.org/api-keys
import requests
from io import BytesIO
from PIL import Image

# The URL to send the request to
url = "https://picsum.photos/800/1000"

# Send the GET request to the URL
response = requests.get(url)
print("Response code: ", response.status_code)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    try:
        # Open the image from the response content
        img = Image.open(BytesIO(response.content))

        # Display the image
        img.show()
    except Exception as e:
        print(f"Error processing the image: {e}")
else:
    print(f"The request failed with status code: {response.status_code}")




# -----------------------------

url = "https://api.random.org/api-keys"
response = requests.get(url)
print("Response code: ", response.status_code)

