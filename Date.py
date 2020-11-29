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


def getDefaultDateTimeObj():
	"""
	Default time in this project: 2020-11-27T2:30
	"""
	return datetime.datetime(
		year=2020,
		month=11,
		day=27,
		hour=2,
		minute=30,
		second=0
	)


class Date(object):
	"""
	This class handles processing and changing dates.
	"""

	def __init__(self):
		super(Date, self).__init__()
		self._dateWithTime = getDefaultDateTimeObj()
		self._setPartOfDay()

		self._isLocked = False
		self._timeExist = True

	def isLocked(self):
		return self._isLocked

	def lock(self):
		self._isLocked = True

	def setTimeFromDateTimeObj(self, dateTimeObj: datetime.datetime):
		self._dateWithTime.replace(year=dateTimeObj.year)
		self._dateWithTime.replace(month=dateTimeObj.month)
		self._dateWithTime.replace(day=dateTimeObj.day)

		self._timeExist = dateTimeObj.hour and dateTimeObj.minute and dateTimeObj.second
		if self._timeExist:
			self._dateWithTime.replace(hour=dateTimeObj.hour)
			self._dateWithTime.replace(minute=dateTimeObj.minute)
			self._dateWithTime.replace(second=dateTimeObj.second)
			self._setPartOfDay()
		self.lock()

	def _setPartOfDay(self):
		if self._dateWithTime.hour > 12:
			self._partOfDay = PartOfDay.PM
		else:
			self._partOfDay = PartOfDay.AM

	def __str__(self):
		out = f"{self._dateWithTime.year}-"\
			+ f"{self._dateWithTime.month}-"\
			+ f"{self._dateWithTime.day}"
		if self._timeExist:
			out += f"T{self._dateWithTime.hour // 10}{self._dateWithTime.hour % 10}:"\
				+ f"{self._dateWithTime.minute // 10}{self._dateWithTime.minute % 10}"
		return out
