import psycopg;

# Option 1: Connection using Keyword Arguments
with psycopg.connect(
  host="localhost",
  dbname="postgres", # Name of the database inside the server
  user="postgres", # Located in server > properties
  password="12",
  port=5432
) as conn:
  
  # Open a cursor to perform database operations
  cur = conn.cursor()
  sentence = """
    INSERT INTO users (user_id, user_name, user_surnames, user_password, user_email, user_phone, user_role, user_regdate) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING user_id;"""
  
  # Column count: 8
  user_id = '1234qwer'
  user_name = 'John'
  user_surnames = 'Postgres'
  user_passwords = '1234'
  user_email = 'jp09@protonmail.com'
  user_phone = 944565789
  user_role = 1
  user_regdate = '12-12-2004'
  
  cur.execute(sentence, (user_id, user_name, user_surnames, user_passwords, user_email, user_phone, user_role, user_regdate))
