# slash4py
Pythonic, Synchronous Discord-Python-Slash-Command-Implementation

### Create a SlashBot:

```py
from slash4py import SlashBot

client = SlashBot(bot_id)
```

### Create a Command

```py
@client.command(auth="TOKEN HERE",name:str =...,description:str=...,options:list=[],guild_id=None)
async def Command():
  return "Response here, nice..."
```
