from pyrogram import Client
from pyrogram.api import functions, types

app = Client("my_account")

with app:
    all_sets = app.send(functions.messages.GetAllStickers(hash=0)).sets
    count = sum([x.count for x in all_sets])
    print(
        f"{count} stickers across {len(all_sets)} sets.\n"
        f"Average of {count / len(all_sets):.2f} stickers per pack."
    )
