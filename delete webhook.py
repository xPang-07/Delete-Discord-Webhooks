import requests

green_color = '\033[92m'
blue_color = '\033[94m'
reset_color = '\033[0m'
yellow_color = '\033[93m'
red_color = '\033[91m'

def remove_webhooks(webhooks):
    if webhooks:
        for webhook in webhooks:
            requests.delete(webhook)
            webhook_id = webhook.split('/')[-2]
            webhook_token = webhook.split('/')[-1]

            print(f"Webhook ID: {blue_color}{webhook_id}{reset_color}")
            print(f"Webhook Token: {yellow_color}{webhook_token}{reset_color}")
            print(f"Status: {green_color}Successfully removed!{reset_color}")
            print()
        return True
    else:
        print(f"{red_color}Webhooks list is empty. Please provide valid webhooks.{reset_color}")
        return False

def ask_for_webhooks():
    webhooks_str = input('Enter webhooks separated by space: ')
    webhooks = webhooks_str.split()
    print()
    return webhooks

while True:
    webhooks = ask_for_webhooks()
    if not remove_webhooks(webhooks):
        break
