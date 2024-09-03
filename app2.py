import sqlite3
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import requests
from io import BytesIO

# これ接続
conn = sqlite3.connect("pokemon.db")
# これ毎回必要なやつ
c = conn.cursor()

name = input("検索したいポケモンの名前を入力してください:")

# 一番最後1個だけだったとしてもカンマが必要
c.execute("SELECT type1, type2, hp, image_url FROM pokemon WHERE name = ?", (name,))

# 今回はfetchallではなくfetchone
row = c.fetchone()

conn.close()

root = tk.Tk()
root.title("ポケモン情報開示")

if row:
    # すべてのデータがrowだったとき、（すべてのデータが取れているとき？）
    type1, type2, hp, image_url = row

    Label(root, text=f"名前:{name}", font=("Arial", 20)).pack(padx=20, pady=10)
    Label(root, text=f"タイプ1:{type1}", font=("Arial", 16)).pack(padx=20, pady=5)
    if type2:
        Label(root, text=f"タイプ2:{type2}", font=("Arial", 16)).pack(padx=20, pady=5)
    Label(root, text=f"HP: {hp}", font=("Arial", 16)).pack(padx=20, pady=5)

    response = requests.get(image_url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)
    img = img.resize((200, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    Label(root, image=photo).pack(padx=20, pady=10)


else:
    Label(root, text=f"ポケモン'{name}'は見つかりませんでした。", font=("Arial,20")).pack(padx=20, pady=20)

root.mainloop()
