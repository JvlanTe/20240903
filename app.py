import sqlite3

conn = sqlite3.connect("pokemon.db")

c = conn.cursor()

c.execute(
    """
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT,
        type1 TEXT,
        type2 TEXT,
        height REAL,
        weight REAL,
        generation INTEGER,
        total_stats INTEGER,
        hp INTEGER,
        attack INTEGER,
        defense INTEGER,
        special_attack INTEGER,
        special_defense INTEGER,
        speed INTEGER,
        catch_rate INTEGER,
        is_baby BOOLEAN,
        is_legendary BOOLEAN,
        evolves_from INTEGER,
        image_url TEXT
    )
"""
)

conn.commit()
conn.close()
