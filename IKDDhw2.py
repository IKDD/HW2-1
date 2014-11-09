'''
This is hw2 for class IKDD
This homework is to scan query string and parse twitter data
Then print out matching text, its user_id, user_name
'''
import psycopg2

config = {
	'user' : 'hanklgs9564_user_4527',
	'password' : 'RnoM3V7M',
	'host' : 'iservdb.cloudopenlab.org.tw',
	'port' : '5432',
	'dbname' : 'hanklgs9564_db_4527'
}

conn = psycopg2.connect(**config)
cursor = conn.cursor()
cursor.execute("SELECT text, user_name, user_id FROM twitter WHERE q = 'haha' ORDER BY user_id")
print(cursor.fetchall())
conn.close()
cursor.close()