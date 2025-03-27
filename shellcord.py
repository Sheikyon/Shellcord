import requests
import json
from colorama import init, Fore, Style

# Initialize Colorama (required for Windows compatibility)
init()

def send_discord_message(webhook_url, message, username="Shellcord", avatar_url=None):
    """
    Sends a message to a Discord channel via a webhook.
    """
    payload = {
        "content": message,
        "username": username
    }
    if avatar_url:
        payload["avatar_url"] = avatar_url
    
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 204:
        print(f"{Fore.GREEN}Message sent successfully!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Failed to send message. Status code: {response.status_code}, Response: {response.text}{Style.RESET_ALL}")

def main():
    WEBHOOK_URL = "https://discord.com/api/webhooks/1354210816345247985/jXgLRvZ0zgNvQQffhOv7RztByOTu-6DgPByuqvJv65-vvd4Gc0GXtC6IlCP0OVTnOaUk"
    AVATAR_URL = "https://i.imgur.com/shell_icon.png"  # Optional
    
    # Colored welcome message
    print(f"{Fore.CYAN}Shellcord: Enter messages below. Type 'exit' to quit.{Style.RESET_ALL}")
    
    while True:
        # Colored input prompt
        message = input(f"{Fore.YELLOW}Message to send: {Style.RESET_ALL}")
        
        if message.lower() == "exit":
            print(f"{Fore.MAGENTA}Shellcord: Exiting.{Style.RESET_ALL}")
            break
        
        if message.strip():
            send_discord_message(
                webhook_url=WEBHOOK_URL,
                message=message,
                username="Shellcord",
                avatar_url=AVATAR_URL
            )
        else:
            print(f"{Fore.RED}Shellcord: Empty message, nothing sent.{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        import requests
    except ImportError:
        print(f"{Fore.RED}Shellcord: 'requests' library missing. Install with: pip install requests{Style.RESET_ALL}")
        exit(1)
    
    try:
        from colorama import init, Fore, Style
    except ImportError:
        print(f"{Fore.RED}Shellcord: 'colorama' library missing. Install with: pip install colorama{Style.RESET_ALL}")
        exit(1)
    
    main()