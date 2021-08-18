import packages.mysql.connector as mydb

db_password = 'okemen65536'
db_user = 'okemenlandz'
db_host = 'mysql1033.db.sakura.ne.jp'
alarm_list = []
version = 'ver 8.0'

def sql_query():
	conn = None
	try:
		conn = mydb.connect(
			user=db_user,  # ユーザー名
			password=db_password,  # パスワード
			host=db_host,  # ホスト名(IPアドレス）
			port='3306',
			database='okemenlandz.okemenlandz'
		)

		if conn.is_connected:
			print("Connected!")
		else:
			print('failed')
			
	except Exception as e:
		print(f"Error Occurred: {e}")

	finally:
		if conn is not None and conn.is_connected():
			conn.close()

	cur = conn.cursor()

sql_query()