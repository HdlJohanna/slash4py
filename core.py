import requests
import asyncio

class SlashBot:
    def __init__(self,id):
        self.url = f"https://discord.com/api/v8/applications/{id}/commands"
        self.commands = []
        self.id = id
        self.loop = asyncio.new_event_loop()

    def command(self,name:str =...,description:str=...,options:list=[],coro=None):
        json = {
            "name":name,
            "type":1,
            "description":description,
            "options":options
        }
        def decorator(func):
             url = "https://discord.com/api/v8/interactions/<interaction_id>/<interaction_token>/callback"

             json = {
                 "type": 4,
                 "data": {
                     "content": self.loop.run_until_complete(func)
                 }
             }
             r = requests.post(url, json=json)
            self.commands.append(json)

        return decorator

    def run(self,token,guild__id:int=None):
        headers = {
            "Authorization": f"Bot {token}"
        }
        
        json = self.commands[0]
        if guild__id:
            url = f"https://discord.com/api/v8/applications/{self.id}/guilds/{guild__id}/commands"

            r = requests.post(url, headers=headers, json=json)
        else:
            r = requests.post(self.url, headers=headers, json=json)
