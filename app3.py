import sqlite3
import tkinter as tk
from tkinter import Label, Entry, Button
from PIL import Image, ImageTk
import requests
from io import BytesIO


def show_pokemon_info():
    name = name_entry.get()

    conn = sqlite3.connect("pokemon.db")
    c = conn.cursor()
    c.execute("SELECT type1, type2, hp, image_url FROM pokemon WHERE name = ?", (name,))

    row = c.fetchone()

    conn.close()

    if row:
        type1, type2, hp, image_url = row

        name_label.config(text=f"名前:{name}")
        type1_label.config(text=f"タイプ1{type1}")
        if type2:
            type2_label.config(text=f"タイプ2{type2}")
        hp_label.config(text=f"HP:{hp}")

        response = requests.get(image_url)
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img = img.resize((200, 200), Image.LANCZOS)  # 画像のサイズを調整
        photo = ImageTk.PhotoImage(img)

        image_label.config(image=photo)
        image_label.image = photo

    else:
        name_label.config(text=f"ポケモン{name}は見つかりませんでした。")
        type1_label.config(text="")
        type2_label.config(text="")
        hp_label.config(text="")
        image_label.config(text="")
        image_label.image = None


root = tk.Tk()
root.title("ポケモン情報開示")

Label(root, text="ポケモンの名前を入力してください。", font=("Arial", 16)).pack(padx=20, pady=10)

name_entry = Entry(root, font=("Arial", 14))
name_entry.pack(padx=20, pady=10)

Button(root, text="表示", font=("Arial", 14), command=show_pokemon_info).pack(padx=20, pady=10)

name_label = Label(root, font=("Arial", 20))
name_label.pack(padx=20, pady=10)

type1_label = Label(root, font=("Arial", 20))
type1_label.pack(padx=20, pady=10)

type2_label = Label(root, font=("Arial", 20))
type2_label.pack(padx=20, pady=10)

hp_label = Label(root, font=("Arial", 20))
hp_label.pack(padx=20, pady=10)

image_label = Label(root)
image_label.pack(padx=20, pady=10)

root.mainloop()
