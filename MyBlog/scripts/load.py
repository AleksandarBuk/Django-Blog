import json
import psycopg2
import argparse

db = 'blogdb'
username = 'alex'
password = 'runserver{}'

# Function to create tables


def create_tables(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS blog_post (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            content TEXT,
            date_posted TIMESTAMP,
            author_id INTEGER
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users_profile (
            id SERIAL PRIMARY KEY,
            user_id INTEGER,
            image VARCHAR(255)
        );
    ''')

# Function to insert data


def insert_data(data, cursor):
    for record in data:
        if record['model'] == 'blog.post':
            cursor.execute('''
                INSERT INTO blog_post (id, title, content, date_posted, author_id) 
                VALUES (%s, %s, %s, %s, %s)
            ''', (record['pk'], record['fields']['title'], record['fields']['content'],
                  record['fields']['date_posted'], record['fields']['author_id']))
        elif record['model'] == 'users.profile':
            cursor.execute('''
                INSERT INTO users_profile (id, user_id, image) 
                VALUES (%s, %s, %s)
            ''', (record['pk'], record['fields']['user'], record['fields']['image']))

# Main script


def main(args):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        f"dbname={args.dbname} user={args.username} password={args.password}")
    cur = conn.cursor()

    # Create tables
    create_tables(cur)

    # Load data from JSON file
    with open(args.json_file, 'r') as file:
        data = json.load(file)

    # Insert data into the database
    insert_data(data, cur)

    # Commit changes and close the connection
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script to import JSON data into a PostgreSQL database.")
    parser.add_argument("json_file", help="Path to the JSON file")
    parser.add_argument("dbname", help="Database name")
    parser.add_argument("username", help="Database username")
    parser.add_argument("password", help="Database password")

    args = parser.parse_args()
    main(args)
