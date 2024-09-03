import sqlite3
import tkinter as tk
from tkinter import Label, Entry, Button
from PIL import Image, ImageTk
import requests
from io import BytesIO
import customtkinter


def show_top_three():

    conn = sqlite3.connect("pokemon.db")
    c = conn.cursor()

    # ORDER BY count DESCで昇順にしている
    c.execute("SELECT name , count FROM pokemon ORDER BY count DESC LIMIT 3")
    top_three = c.fetchall()

    # 一番初めのデータを取りたいから0
    top1_label.config(text=f"1位: {top_three[0][0]} - {top_three[0][1]}回")
    top2_label.config(text=f"2位: {top_three[1][0]} - {top_three[1][1]}回")
    top3_label.config(text=f"3位: {top_three[2][0]} - {top_three[2][1]}回")

    conn.close()


def show_pokemon_info():
    name = name_entry.get()

    conn = sqlite3.connect("pokemon.db")
    c = conn.cursor()
    # countを追加
    c.execute("SELECT type1, type2, hp, image_url, count FROM pokemon WHERE name = ?", (name,))

    row = c.fetchone()

    if row:
        type1, type2, hp, image_url, count = row

        c.execute("UPDATE pokemon SET count = ? WHERE name = ?", (count + 1, name))
        conn.commit()

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

    conn.close()

    show_top_three()


root = tk.Tk()
root.title("ポケモン情報開示")


Label(root, text="ポケモンの名前を入力してください。", font=("Arial", 16)).pack(padx=20, pady=10)

name_entry = Entry(root, font=("Arial", 14))
name_entry.pack(padx=20, pady=10)


app = customtkinter.CTk()
app.geometry("400x150")
app.configure(fg_color="#FFFFFF")


button = customtkinter.CTkButton(root, text="表示", font=("Arial", 14), command=show_pokemon_info)
button.pack(padx=20, pady=10)

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


top1_label = Label(root, font=("Arial", 14))
top1_label.pack(padx=20, pady=5)
top2_label = Label(root, font=("Arial", 14))
top2_label.pack(padx=20, pady=5)
top3_label = Label(root, font=("Arial", 14))
top3_label.pack(padx=20, pady=5)

show_top_three()

root.mainloop()
