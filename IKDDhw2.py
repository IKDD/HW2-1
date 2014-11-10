'''
This is hw2 for class IKDD
This homework is to scan query string and parse twitter data
Then print out matching text, its user_id, user_name
'''
import psycopg2
import sys
#from tabulate import tabulate

#set the server database information
config = {
	'user' : 'hanklgs9564_user_4527',
	'password' : 'RnoM3V7M',
	'host' : 'iservdb.cloudopenlab.org.tw',
	'port' : '5432',
	'dbname' : 'hanklgs9564_db_4527'
}

query = raw_input()
SQLstring = "SELECT text, user_name, user_id FROM twitter WHERE q = \'" + query + "\' ORDER BY user_id"

#connect iServDB
try:
	conn = psycopg2.connect(**config)
except:
	print "Unable to connect to the database."
cursor = conn.cursor()
try:
	cursor.execute(SQLstring)
except:
	print "Database error!."

result = cursor.fetchall()
print (result)

print "///////////////////////////////////"
for i in result:
	print i[0],",,,,,,,,,,,,",i[1],",,,,,,,,,,",i[2]

conn.close()
cursor.close()