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

class WeekDay(enumerate):
	Monday = 0
	Tuesday = 1
	Wednesday = 2
	Thursday = 3
	Friday = 4
	Saturday = 5
	Sunday = 6

class Date(object):
	"""docstring for Data"""

	def __init__(self):
		super(Date, self).__init__()
		self._dateWithTime = datetime.datetime.now()
		self._setPartOfDay()
		self._isLocked = False

	def isLocked(self):
		return self._isLocked

	def lock(self):
		self._isLocked = True

	def setTimeFromDateTimeObj(self, dateTimeObj: datetime.datetime):
		if dateTimeObj.year:
			self._dateWithTime.replace(year=dateTimeObj.year)
		if dateTimeObj.month:
			self._dateWithTime.replace(month=dateTimeObj.month)
		if dateTimeObj.day:
			self._dateWithTime.replace(day=dateTimeObj.day)
		if dateTimeObj.hour:
			self._dateWithTime.replace(hour=dateTimeObj.hour)
		if dateTimeObj.minute:
			self._dateWithTime.replace(minute=dateTimeObj.minute)
		if dateTimeObj.second:
			self._dateWithTime.replace(second=dateTimeObj.second)
		self._setPartOfDay()
		self.lock()

	def _setPartOfDay(self):
		if self._dateWithTime.hour > 12:
			self._partOfDay = PartOfDay.PM
		else:
			self._partOfDay = PartOfDay.AM

	def __str__(self):
		return f"{self._dateWithTime.year}-"\
			+ f"{self._dateWithTime.month}-"\
			+ f"{self._dateWithTime.day}T"\
			+ f"{self._dateWithTime.hour // 10}{self._dateWithTime.hour % 10}:"\
			+ f"{self._dateWithTime.minute // 10}{self._dateWithTime.minute % 10}"
