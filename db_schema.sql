CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    password TEXT,
    name TEXT NOT NULL,
    price FLOAT
) ;
