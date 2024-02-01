import requests
import json

green_color = '\033[92m'
blue_color = '\033[94m'
reset_color = '\033[0m'
yellow_color = '\033[93m'
red_color = '\033[91m'

def send_embed_webhook(url, embed, count):
    payload = {
        "embeds": [embed]
    }

    json_payload = json.dumps(payload)

    headers = {
        "Content-Type": "application/json"
    }

    try:
        for _ in range(int(count)):
            response = requests.post(url, data=json_payload, headers=headers)
            # if response.status_code == 200:
            print(f"{green_color}Sent successfully!! {reset_color}[{yellow_color}{_ + 1}{reset_color}]")
        return True
        # else:
        #     print(f"Failed to send embed webhook. Status code: {response.status_code}")
        #     return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def ask_for_webhooks():
    print()
    webhooks = input('Enter webhooks separated by space (or enter "exit" to quit): ')
    print()
    return webhooks

webhook_url = 'https://discord.com/api/webhooks/1045744470274084888/1DIUnIIPt2nrPmQPQ4DtaqojhzDG7r1kUAn6PAMv2Dz71QexoEC_BJV7f32SvQ__xtwr'

while True:
    webhooks = ask_for_webhooks()
    if webhooks.lower() == 'exit':
        break
    else:
        webhook_list = webhooks.split()
        title = input('Enter Title: ')
        description = input('Enter Description: ')
        footer = input('Enter Footer: ')
        count = input('Enter Count: ')
        embed = {
            "title": title,
            "description": description,
            "color": 16711680, 
            "footer": {"text": footer},
        }
        for webhook in webhook_list:
            webhook_id = webhook.split('/')[-2]
            webhook_token = webhook.split('/')[-1]
            print()
            print(f"Webhook ID: {blue_color}{webhook_id}{reset_color}")
            print(f"Webhook Token: {yellow_color}{webhook_token}{reset_color}")
            print(f"!! {green_color}Detail{reset_color} !!")
            print(f"[ {blue_color}Title {reset_color}: {green_color}{embed['title']} {reset_color}]")
            print(f"[ {blue_color}Description {reset_color}: {green_color}{embed['description']} {reset_color}]")
            print(f"[ {blue_color}Footer {reset_color}: {green_color}{embed['footer']['text']} {reset_color}]")
            print()
            send_embed_webhook(webhook, embed, count)
