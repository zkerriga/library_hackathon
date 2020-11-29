import datetime
from typing import Final


class Period(object):
	"""docstring for Period"""

	dateSeparator: Final = '/'

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
	"""
	This class handles processing and changing dates.
	"""

	def __init__(self):
		super(Date, self).__init__()
		self._dateWithTime = datetime.datetime.now()
		self._setPartOfDay()

		self._isLocked = False
		self._timeExist = True
		self._isQuarter = False

	def isLocked(self):
		return self._isLocked

	def lock(self):
		self._isLocked = True

	def setTimeFromDateTimeObj(self, dateTimeObj: datetime.datetime):
		self._dateWithTime = self._dateWithTime.replace(year=dateTimeObj.year)
		self._dateWithTime = self._dateWithTime.replace(month=dateTimeObj.month)
		self._dateWithTime = self._dateWithTime.replace(day=dateTimeObj.day)

		self._timeExist = dateTimeObj.hour and dateTimeObj.minute and dateTimeObj.second
		if self._timeExist:
			self._dateWithTime = self._dateWithTime.replace(hour=dateTimeObj.hour)
			self._dateWithTime = self._dateWithTime.replace(minute=dateTimeObj.minute)
			self._dateWithTime = self._dateWithTime.replace(second=dateTimeObj.second)
			self._setPartOfDay()
		self.lock()

	def _setPartOfDay(self):
		if self._dateWithTime.hour > 12:
			self._partOfDay = PartOfDay.PM
		else:
			self._partOfDay = PartOfDay.AM

	def setQuarter(self, data_quarter: tuple):
		month = data_quarter[0]
		year = data_quarter[1]
		if year:
			self._dateWithTime = self._dateWithTime.replace(year=year)
		self._dateWithTime = self._dateWithTime.replace(month=(month * 3))
		self._isQuarter = True
		self._isLocked = True

	def _getQuartalString(self):
		out = f"{self._dateWithTime.year}-" \
			  + f"Q{self._dateWithTime.month // 3}"
		return out

	def __str__(self):
		if self._isQuarter:
			return self._getQuartalString()
		out = f"{self._dateWithTime.year}-"\
			+ f"{self._dateWithTime.month}-"\
			+ f"{self._dateWithTime.day}"
		if self._timeExist:
			out += f"T{self._dateWithTime.hour // 10}{self._dateWithTime.hour % 10}:"\
				+ f"{self._dateWithTime.minute // 10}{self._dateWithTime.minute % 10}"
		return out
