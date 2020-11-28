import datetime


class Period(object):
	"""docstring for Period"""

	dateSeparator = '/'

	def __init__(self, dataStart, dataEnd):
		super(Period, self).__init__()

		self.dataStart = dataStart
		self.dataEnd = dataEnd


class PartOfDay(enumerate):
	AM = 0
	PM = 1


class Date(object):
	"""docstring for Data"""

	def __init__(self):
		super(Date, self).__init__()
		self.now = datetime.datetime.now()

		self.year = int(self.now.year)
		self.month = int(self.now.month)
		self.day = int(self.now.day)

		self.weekDay = self.now.weekday()  # [0,6]

		if self.now.hour > 12:
			self.partOfDay = PartOfDay.PM
		else:
			self.partOfDay = PartOfDay.AM

		self.hours = int(self.now.hour)
		self.minutes = int(self.now.minute)
		self.seconds = int(self.now.second)

		self.isLocked = False

	def isLocked(self):
		return self.isLocked

	def lock(self):
		self.isLocked = True

	def __str__(self):
		return f"{self.year}-{self.month}-{self.day}T{self.hours // 10}{self.hours % 10}:{self.minutes // 10}{self.minutes % 10}"
