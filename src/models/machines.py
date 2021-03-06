# base class for accessing machines table 
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, './models')))
from baseModel import Base_Model


from schedules import Schedule

class Machine(Base_Model):
	"""docstring for Machine"""
	def __init__(self,name):
		Base_Model.__init__(self)
		self.name = name
		self.conn = self.db_connect()
		self.cur = self.conn.cursor()
		self.Schedule = None
		#@staticmethod
	def get_all_machines(self):
		machines = []
		conn = self.db_connect()

		cur = conn.cursor()
		cur.execute("select * from machines")

		for machine in cur.fetchall():
			machines.append(machine)

		return machines 

	def create_machine(self):
		conn = self.db_connect()
		cur = conn.cursor()
		cur.execute("INSERT INTO machines VALUES ( DEFAULT, 'Yellow Machine', 'Elliptical', '712 Schermerhorn');")
		print(cur.statusmessage)
		conn.commit()

	def get_machine_schedule_dictionaries(self):
		mg = Machine("temp")
		machines = mg.get_all_machines()
		types = {"Treadmill":{},"Strider":{},"Ski":{}}
		for machine in machines:
			mid = machine[0]
			#print(mid)
			mtype = machine[2]
			#print(mtype)
			schedule = Schedule()
			times = schedule.get_available_times(mid)
			#print(times)
			if mtype == "Treadmill":
				types["Treadmill"][mid] = times
			if mtype == "Strider":
				types["Strider"][mid] = times
			if mtype == "Ski":
				types["Ski"][mid] = times
			schedule.db_close()
		mg.db_close()
		return types

	def getTypeFromID(self,mid):
		try:
			print('SELECT * FROM machines WHERE mid={}'.format(mid))

			conn = self.db_connect()
			print("connected")
			cur = conn.cursor()
			print("cursor")

			cur.execute('SELECT * FROM machines WHERE mid={}'.format(mid))
			record = cur.fetchone()
			print("record",record)
			print(record[2])
			return record[2]
		except Exception as e:
			print("exception")
			print(e)


