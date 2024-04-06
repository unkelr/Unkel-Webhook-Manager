import os
import time
import requests
from datetime import datetime
from colorama import init, Fore


init(autoreset=True)
os.system('cls')
os.system('title Unkel Webhook Manager')

class WebhookMessageEmbedder:
    def __init__(self, webhook, content="", username="", avatar_url="", embed=False, embed_color="", title="", description="", footer="", footer_url="", timestamp=False):
        self.webhook = webhook
        self.content = content
        self.username = username
        self.avatar_url = avatar_url
        self.embed = embed
        self.embed_color = embed_color
        self.title = title
        self.description = description
        self.footer = footer
        self.footer_url = footer_url
        self.timestamp = timestamp

    def send_message(self):
        data = {}

        if self.embed:
            embed = {
                "title": self.title,
                "description": self.description,
                "color": self._get_color(self.embed_color),
                "footer": {
                    "text": self.footer,
                    "icon_url": self.footer_url
                },
                "timestamp": self._get_timestamp() if self.timestamp else None
            }
            data["embeds"] = [embed]
        else:
            data["content"] = self.content

        if self.username:
            data["username"] = self.username

        if self.avatar_url:
            data["avatar_url"] = self.avatar_url

        response = requests.post(self.webhook, json=data)

        if response.status_code != 200:
            print(Fore.GREEN + f"Message Sent! {response.text}")
        else:
            print(Fore.GREEN + "Message sent successfully.")

    def _get_color(self, color_name):
        colors = {
            "white": 0xFFFFFF,
            "silver": 0xC0C0C0,
            "gray": 0x808080,
            "black": 0x000000,
            "red": 0xFF0000,
            "maroon": 0x800000,
            "yellow": 0xFFFF00,
            "olive": 0x808000,
            "lime": 0x00FF00,
            "green": 0x008000,
            "aqua": 0x00FFFF,
            "teal": 0x008080,
            "blue": 0x0000FF,
            "navy": 0x000080,
            "fuchsia": 0xFF00FF,
            "purple": 0x800080,
            "pink": 0xFFC0CB,
            "salmon": 0xFA8072,
            "orange": 0xFFA500,
            "gold": 0xFFD700,
            "khaki": 0xF0E68C,
            "brown": 0xA52A2A,
            "sienna": 0xA0522D
        }
        if color_name.lower() in colors:
            return colors[color_name.lower()]
        else:
            try:
                return int(color_name, 16)
            except ValueError:
                print(Fore.YELLOW + "Invalid color provided. Defaulting to 'black'.")
                return colors["black"]

    def _get_timestamp(self):
        return datetime.utcnow().isoformat()

class WebhookManager:
    def delete_webhook(self, webhook_url):
        print(Fore.GREEN + "Webhook deleted successfully.")

def get_input(prompt):
    return input(prompt).strip()

def get_bool_input(prompt):
    while True:
        choice = input(prompt + " (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print(Fore.YELLOW + "Invalid input. Please enter 'y' or 'n'.")

intro = """
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
"""
print(Fore.RED + intro)
print(Fore.CYAN + "Welcome To Unkel Webhook Manager!")
time.sleep(3)
os.system('cls')
print(Fore.RED + intro)

webhook_manager = WebhookManager()

while True:
    print(Fore.CYAN + "Choose an action:")
    print(Fore.CYAN + "1. Send a message")
    print(Fore.CYAN + "2. Delete a webhook")
    action = get_input(Fore.CYAN + "Choice : ")

    if action == '1':
        webhook_url = get_input(Fore.CYAN + "Webhook : ")
        content = get_input(Fore.CYAN + "Enter the message content (leave blank if you want to send only an embed): ")
        username = get_input(Fore.CYAN + "Enter the webhook username (leave blank for default): ")
        avatar_url = get_input(Fore.CYAN + "Enter the webhook avatar URL (leave blank for default): ")
        embed = get_bool_input(Fore.CYAN + "Do you want to send as an embed?")
        if embed:
            title = get_input(Fore.CYAN + "Enter the embed title: ")
            description = get_input(Fore.CYAN + "Enter the embed description: ")
            footer = get_input(Fore.CYAN + "Enter the footer text: ")
            footer_url = get_input(Fore.CYAN + "Enter the footer URL (leave blank for no footer image): ")
            print(Fore.CYAN + "Choose a color for the embed (or provide a hex value):")
            embed_color = get_input(Fore.CYAN + "Enter the embed color: ")
            timestamp = get_bool_input(Fore.CYAN + "Do you want to include a timestamp?")
        else:
            title = description = footer = footer_url = embed_color = ""
            timestamp = False

        message_embedder = WebhookMessageEmbedder(
            webhook=webhook_url,
            content=content,
            username=username,
            avatar_url=avatar_url,
            embed=embed,
            embed_color=embed_color,
            title=title,
            description=description,
            footer=footer,
            footer_url=footer_url,
            timestamp=timestamp
        )

        print(Fore.CYAN + "\nSending message...")
        message_embedder.send_message()

        
        time.sleep(2)  
        os.system('cls')
        print(Fore.RED + intro)

    elif action == '2':
        webhook_url = get_input(Fore.CYAN + "Webhook : ")
        check = requests.get(webhook_url)
        requests.delete(webhook_url)
        if check.status_code == 404:
            print(Fore.GREEN + "Webhook deleted successfully.")
        elif check.status_code == 200:
            print(Fore.RED + "Failed to delete webhook.")
    else:
        print(Fore.RED + "Invalid choice. Please enter '1' or '2'.")

    os.system('cls')
    print(Fore.RED + intro)