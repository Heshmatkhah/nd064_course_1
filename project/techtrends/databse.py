import sqlite3


# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
	connection = sqlite3.connect('database.db')
	connection.row_factory = sqlite3.Row
	# Increase total number of connections.
	connection.execute("UPDATE information SET value = CAST(CAST(value +1 AS INT) AS TEXT) where key = 'connections'")
	connection.commit()
	return connection


# Function to get a post using its ID
def get_post(post_id):
	connection = get_db_connection()
	post = connection.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
	connection.close()
	return post


def get_post_count():
	connection = get_db_connection()
	post = connection.execute('SELECT COUNT(*) FROM posts;', ).fetchone()
	return post['count(*)']


def get_connection_count():
	connection = get_db_connection()
	count = connection.execute("SELECT value FROM information where key = 'connections';", ).fetchone()
	return int(count['value'])
