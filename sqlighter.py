import sqlite3

class SQLighter:

	def __init__(self, database):
		"""подключаемся к БД"""
		self.connection = sqlite3.connect(database)
		self.cursor = self.connection.cursor()


	def subscriber_exists(self, user_id):
		"""проверяем, етсь ли уде в базе"""
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `homework` WHERE `user_id` = ?', (user_id,)).fetchall()
			return bool(len(result))

	def add_subscriber(self, user_id, name, username, status = 1):
		"""Добовляем нового пользователя"""
		with self.connection:
			return self.cursor.execute("INSERT INTO `homework` (`user_id`, `status`, `name`, `username`) VALUES(?,?,?,?)", (user_id,status,name,username))

	def update_subscription(self, user_id, status):
		"""Обновляем статус"""
		with self.connection:
			return self.cursor.execute("UPDATE `homework` SET `status` = ? WHERE `user_id` = ?", (status, user_id))


	def update_time(self, user_id, time):
		with self.connection:
			return self.cursor.execute("UPDATE `homework` SET `last_time` = ? WHERE `user_id` = ?", (time, user_id))

	def get_time(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM `homework` WHERE `user_id` = ?", (user_id,)).fetchall()
			for row in result:
				return row[14] 


	def get(self, user_id, var):
		"""Получаем заначение для общения"""
		with self.connection:
			if type(user_id) is int:
				result = self.cursor.execute("SELECT * FROM `homework` WHERE `user_id` = ?", (user_id,)).fetchall()
				for row in result:
					try:
						return {
							'user_id': row[1],
							'status': row[2],
							'class': row[3],
							'hw0': row[4],
							'hw1': row[5],
							'hw2': row[6],
							'hw3': row[7],
							'hw4': row[8],
							'hw5': row[9],
							'noten': row[10],
							'add_hw': row[11],
							'name': row[12],
							'last': row[14],
						}[var]
					except:
						return -1
			elif (var == 'statistics'):
				result = self.cursor.execute("SELECT * FROM `homework` WHERE `status` = 22 AND `class` = ?", (user_id,)).fetchall()
				for row in result:
					return row[11]
			else:
				result = self.cursor.execute("SELECT * FROM `homework` WHERE `class` = ?", (user_id,)).fetchall()
				for row in result:
					try:
						return {
							'user_id': row[1],
							'status': row[2],
							'class': row[3],
							'hw0': row[4],
							'hw1': row[5],
							'hw2': row[6],
							'hw3': row[7],
							'hw4': row[8],
							'hw5': row[9],
							'noten': row[10],
							'add_hw': row[11],
						}[var]
					except:
						return -1

	def update(self, user_id, var, status):
		with self.connection:
			if var == 'class':	#0 - неактивно, 1 - плохо, 2 - хорошо
				return self.cursor.execute("UPDATE `homework` SET `class` = ? WHERE `user_id` = ?", (status, user_id))
			elif var == 'status':	#1 ; 0
				return self.cursor.execute("UPDATE `homework` SET `status` = ? WHERE `user_id` = ?", (status, user_id))
			elif var == 'hw0':	#1 ; 0
				return self.cursor.execute("UPDATE `homework` SET `hw0` = ? WHERE `class` = ?", (status, user_id))
			elif var == 'hw1':	#1 ; 0
				return self.cursor.execute("UPDATE `homework` SET `hw1` = ? WHERE `class` = ?", (status, user_id))
			elif var == 'hw2':	#1 ; 0
				return self.cursor.execute("UPDATE `homework` SET `hw2` = ? WHERE `class` = ?", (status, user_id))
			elif var == 'hw3':	#1 ; 0
				return self.cursor.execute("UPDATE `homework` SET `hw3` = ? WHERE `class` = ?", (status, user_id))
			elif var == 'hw4':	#1 ; 0
				return self.cursor.execute("UPDATE `homework` SET `hw4` = ? WHERE `class` = ?", (status, user_id))
			elif var == 'hw5':	#1 ; 0
				return self.cursor.execute("UPDATE `homework` SET `hw5` = ? WHERE `class` = ?", (status, user_id))
			elif var == 'add_hw':	#1 ; 0
				return self.cursor.execute("UPDATE `homework` SET `add_hw` = ? WHERE `user_id` = ?", (status, user_id))
			elif var == 'noten':	#1 ; 0
				return self.cursor.execute("UPDATE `homework` SET `noten` = ? WHERE `class` = ?", (status, user_id))
			elif var == 'name':	#1 ; 0
				return self.cursor.execute("UPDATE `homework` SET `name` = ? WHERE `user_id` = ?", (status, user_id))
			elif var == 'statistics':
				return self.cursor.execute("UPDATE `homework` SET `add_hw` = ? WHERE `status` = 22 AND `class` = ?", (status, user_id))


	def debug(self):
		with self.connection:
			return self.cursor.execute("SELECT * FROM `homework`").fetchall()

	def get_lesson(self, clas, day):
		"""Получаем заначение для общения"""
		with self.connection:
			result = self.cursor.execute("SELECT * FROM `lessons` WHERE `clas` = ?", (clas,)).fetchall()
			for row in result:
				try:
					return {
						'day0': row[2],
						'day1': row[3],
						'day2': row[4],
						'day3': row[5],
						'day4': row[6],
						'day5': row[7],
						'day6': row[8],
						'tday0': row[9],
						'tday1': row[10],
						'tday2': row[11],
						'tday3': row[12],
						'tday4': row[13],
						'tday5': row[14],
						'tday6': row[15],
						'remake0': row[16],
						'remake1': row[17],
						'remake2': row[18],
						'remake3': row[19],
						'remake4': row[20],
						'remake5': row[21],
						'status': row[22],
					}[day]
				except:
					return -1

	def add_new_rasp(self, clas, day, rasp):
		with self.connection:
			if day  == 0:
				return self.cursor.execute("UPDATE `lessons` SET `remake0` = ? WHERE `clas` = ?", (rasp, clas))
			elif day == 1:
				return self.cursor.execute("UPDATE `lessons` SET `remake1` = ? WHERE `clas` = ?", (rasp, clas))
			elif day == 2:
				return self.cursor.execute("UPDATE `lessons` SET `remake2` = ? WHERE `clas` = ?", (rasp, clas))
			elif day == 3:
				return self.cursor.execute("UPDATE `lessons` SET `remake3` = ? WHERE `clas` = ?", (rasp, clas))
			elif day == 4:
				return self.cursor.execute("UPDATE `lessons` SET `remake4` = ? WHERE `clas` = ?", (rasp, clas))
			elif day == 5:
				return self.cursor.execute("UPDATE `lessons` SET `remake5` = ? WHERE `clas` = ?", (rasp, clas))
	def set_upd_rasp(self, clas, day):
		with self.connection:
			return self.cursor.execute("UPDATE `lessons` SET `stat_remake` = ? WHERE `clas` = ?", (day, clas))

	def get_upd_rasp(self, clas):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM `lessons` WHERE `clas` = ?", (clas,)).fetchall()
			for row in result:
				return row[22]


	def close(self):
		"""Закрываем БД"""
		self.connection.close()