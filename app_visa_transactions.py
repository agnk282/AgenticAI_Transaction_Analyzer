import os
import sqlite3
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DB_FILE = "visa_transactions.db"

# Configure OpenAI API
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY
else:
    raise ValueError("OPENAI_API_KEY not set in .env file.")

def get_sql_query_from_gpt(user_text):
    """
    Use the OpenAI GPT API (>=1.0.0) to convert user natural language input to a SQL query.
    """
    prompt = f"""
You are an expert SQL assistant. The database has a table called 'transactions' with the following columns:
- transaction_id (INTEGER)
- card_number (TEXT)
- amount (REAL)
- merchant (TEXT)
- timestamp (TEXT)
- status (TEXT)

Convert the following user request into a valid SQLite SQL query. Only return the SQL query, nothing else.
User request: {user_text}
"""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes only SQL queries."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=256,
        temperature=0
    )
    sql_query = response.choices[0].message.content.strip()
    # Remove code block markers if present
    if sql_query.startswith("```sql"):
        sql_query = sql_query[6:]
    if sql_query.startswith("```"):
        sql_query = sql_query[3:]
    sql_query = sql_query.strip('`').strip()
    # Only take the first statement if multiple are returned
    sql_query = sql_query.split(';')[0].strip()
    if not sql_query.lower().startswith("select"):
        raise ValueError("Generated query is not a SELECT statement.")
    return sql_query

def execute_sql_query(sql_query):
    conn = sqlite3.connect(DB_FILE)
    try:
        cur = conn.cursor()
        cur.execute(sql_query)
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        return columns, rows
    except Exception as e:
        return None, str(e)
    finally:
        conn.close()

def main():
    print("Welcome to the VISA Transactions Query Assistant!")
    print("Type your request in plain English (e.g., 'Show all approved transactions above $100'). Type 'exit' to quit.")
    while True:
        user_text = input("\nYour request: ").strip()
        if user_text.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        try:
            sql_query = get_sql_query_from_gpt(user_text)
            print(f"\nGenerated SQL query:\n{sql_query}")  # Always print the generated query
            columns, result = execute_sql_query(sql_query)
            if columns is None:
                print(f"Error executing query: {result}")
            elif not result:
                print("No results found.")
            else:
                print("\nResults:")
                print(" | ".join(columns))
                for row in result:
                    print(" | ".join(str(x) for x in row))
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
