import time
import hashlib
import requests

# Telegram bot token and chat ID
telegram_token = "6607994197:AAFi3hBsT6IdJjP4sUS-yiZHqddk7ZjKM5E"
telegram_chat_id = "6098861668"

# setting the URL you want to monitor
url = 'https://insider.in/ipl-indian-premier-league/srh-sunrisers-hyderabad'

# Function to send message via Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    data = {"chat_id": telegram_chat_id, "text": message}
    requests.post(url, data=data)

# to perform a GET request and load the
# content of the website and store it in a var
response = requests.get(url).content

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(10)
while True:
    try:
        # perform the get request and store it in a var
        response = requests.get(url).content

        # create a hash
        currentHash = hashlib.sha224(response).hexdigest()

        # wait for 30 seconds
        time.sleep(120)

        # perform the get request
        response = requests.get(url).content

        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()

        # check if new hash is same as the previous hash
        if newHash == currentHash:
            continue

        # if something changed in the hashes
        else:
            # notify
            send_telegram_message("Something changed on the website!")

            # again read the website
            response = requests.get(url).content

            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()

            # wait for 30 seconds
            time.sleep(120)
            continue

    # To handle exceptions
    except Exception as e:
        print("Error:", e)
