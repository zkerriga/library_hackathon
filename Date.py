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
		self._now = datetime.datetime.now()

		self._year = int(self._now.year)
		self._month = int(self._now.month)
		self._day = int(self._now.day)

		self._weekDay = self._now.weekday()  # [0,6]

		if self._now.hour > 12:
			self._partOfDay = PartOfDay.PM
		else:
			self._partOfDay = PartOfDay.AM

		self._hours = int(self._now.hour)
		self._minutes = int(self._now.minute)
		self._seconds = int(self._now.second)

		self._isLocked = False

	def isLocked(self):
		return self._isLocked

	def lock(self):
		self._isLocked = True

	def __str__(self):
		return f"{self._year}-{self._month}-{self._day}T{self._hours // 10}"\
				+ f"{self._hours % 10}:{self._minutes // 10}{self._minutes % 10}"
