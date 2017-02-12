from connection_factory import ConnectionFactory

connection = ConnectionFactory().get_connection()
cursor = connection.cursor()

cursor.execute("SELECT * FROM CURSO")

for line in cursor:
	print(line)

connection.close()

