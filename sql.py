import sqlite3
import datetime

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    sql_create_transactions_table = '''
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_number TEXT NOT NULL,
        amount REAL NOT NULL,
        merchant TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        status TEXT NOT NULL
    );
    '''
    try:
        c = conn.cursor()
        c.execute(sql_create_transactions_table)
    except sqlite3.Error as e:
        print(e)

def insert_transaction(conn, transaction):
    sql = ''' INSERT INTO transactions(card_number, amount, merchant, timestamp, status)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, transaction)
    conn.commit()
    return cur.lastrowid

def insert_sample_transactions(conn):
    # Sample VISA-like transactions for a day
    today = datetime.date.today()
    transactions = [
        ("4111111111111111", 120.50, "Amazon", f"{today} 09:15:00", "approved"),
        ("4111111111111111", 15.75, "Starbucks", f"{today} 10:05:00", "approved"),
        ("4000123412341234", 200.00, "Apple Store", f"{today} 11:30:00", "declined"),
        ("4012888888881881", 50.00, "Uber", f"{today} 12:45:00", "approved"),
        ("4222222222222", 5.25, "McDonald's", f"{today} 13:20:00", "approved"),
        ("4111111111111111", 300.00, "Best Buy", f"{today} 15:00:00", "approved"),
        ("4000123412341234", 80.00, "Walmart", f"{today} 16:10:00", "approved"),
        ("4012888888881881", 60.00, "Target", f"{today} 17:25:00", "declined"),
        ("4222222222222", 22.00, "CVS", f"{today} 18:40:00", "approved"),
        ("4111111111111111", 10.00, "Subway", f"{today} 19:55:00", "approved"),
    ]
    for txn in transactions:
        insert_transaction(conn, txn)

def fetch_all_transactions(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions")
    return cur.fetchall()

def main():
    db_file = "visa_transactions.db"
    conn = create_connection(db_file)
    if conn is not None:
        create_table(conn)
        insert_sample_transactions(conn)
        txns = fetch_all_transactions(conn)
        print("All VISA transactions for today:")
        for txn in txns:
            print(txn)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    main()
