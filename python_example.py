# test this script after running following bash command (create database to read from):
# docker exec -it pg-docker psql -U postgres -c "create database my_database"

import psycopg2

# Connect to database
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='my_database',
    user='postgres',
    password='docker'
)
cur = conn.cursor()

# Create a table if it doesn't exist yet
cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);")

# Insert new row of data
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abcdef"))

# Read the entire table
cur.execute("SELECT * FROM test;")
result = cur.fetchall()

# Print raw form of data
print(result)

# Commit changes
conn.commit()

# Close connections
cur.close()
conn.close()

# Print length of data (rows)
print(len(result))

# Convert data to dataframe format
import pandas as pd
df = pd.DataFrame(data=result)
print(df)