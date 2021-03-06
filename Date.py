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
		self._dateWithTime: datetime.datetime = getDefaultDateTimeObj()
		self._setPartOfDay()

		self._isLocked: bool = False
		self._timeExist: bool = True
		self._isQuarter: bool = False
		self._dateForPeriod: Date = None

	def isLocked(self):
		return self._isLocked

	def lock(self):
		self._isLocked = True

	def setTimeFromDateTimeObj(self, dateTimeObj: datetime.datetime):
		self._dateWithTime = self._dateWithTime.replace(year=dateTimeObj.year)
		self._dateWithTime = self._dateWithTime.replace(month=dateTimeObj.month)
		self._dateWithTime = self._dateWithTime.replace(day=dateTimeObj.day)

		hasNotTime: bool = not bool(dateTimeObj.hour) and \
						   not bool(dateTimeObj.minute) and \
						   not bool(dateTimeObj.second)

		self._timeExist = not hasNotTime
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

	def setDateToPeriod(self, endObjDated: datetime.datetime):
		self._dateForPeriod = endObjDated

	def __str__(self):
		if self._isQuarter:
			return self._getQuartalString()
		out = f"{self._dateWithTime.year}-" \
			+ f"{self._dateWithTime.month}-" \
			+ f"{self._dateWithTime.day}"
		if self._dateForPeriod:
			out += f" - {self._dateForPeriod}"
		return out
