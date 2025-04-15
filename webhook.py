
import requests 
import json

webhook_url = 'https://discord.com/api/webhooks/1361598790238339122/uggjYRkRldhdttaNFTwApfawdvcA-TwvdcrODI89Ft8xDPsRUtqdR_XA7qtRGzOqVOhR'

data = {
    "content": "Ahoj, toto je zpráva poslaná přes webhook!"
}

response = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

if response.status_code == 204:
    print("Zpráva byla úspěšně odeslána!")
else:
    print(f"Došlo k chybě: {response.status_code}")
