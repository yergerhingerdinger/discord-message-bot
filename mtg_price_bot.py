import requests
import schedule
import time
from dotenv import load_dotenv
import os

load_dotenv()

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_mtg_price():
    scryfall_url = "https://api.scryfall.com/cards/sld/7009"
    response = requests.get(scryfall_url)
    
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        foil_price = data["prices"]["usd_foil"]
        scryfall_link = "https://scryfall.com/card/sld/7009/smothering-tithe"

        message = {
            "content": f"💰 **{name}** (Secret Lair Foil #7009)\n📈 Today's TCGPlayer Price: **{'$'}{foil_price}**\n🔗 {scryfall_link}"
        }
        response = requests.post(WEBHOOK_URL, json=message)
        if response.status_code == 204:
            print("Price sent successfully!")
        else:            
            print(f"Failed to send price: {response.status_code}")


# Scheduled MTG price - Every day at 9 AM and 9 PM
schedule.every().day.at("04:00").do(send_mtg_price) # Convert to 9 PT
schedule.every().day.at("16:00").do(send_mtg_price) # Convert to 9 PT

send_mtg_price()  # Send immediately on startup

while True:
    schedule.run_pending()
    time.sleep(60)
    