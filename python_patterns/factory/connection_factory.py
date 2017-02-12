import MySQLdb


class ConnectionFactory:
	"""Creates a DB connection"""

	def get_connection(self):
		connection = MySQLdb.connect(
			host="localhost",
			user='root',
			passwd='',
			db='mydb'
			)

		return connection