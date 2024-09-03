import sqlite3


# データベースに接続

conn = sqlite3.connect("pokemon.db")

c = conn.cursor()


c.execute("ALTER TABLE pokemon ADD COLUMN count INTEGER DEFAULT 0")


# データベースへの変更を保存

conn.commit()


# データベース接続を閉じる

conn.close()
