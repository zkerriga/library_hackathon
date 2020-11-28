import datetime

class Period(object):
	"""docstring for Period"""

	dateSeparator:str = '/'

	def __init__(self, dataStart, dataEnd):
		super(Period, self).__init__()
		
		self.dataStart:Date = dataStart
		self.dataEnd:Date = dataEnd

class Date(object):
	"""docstring for Data"""

	def __init__(self):
		super(Data, self).__init__()
		self.now = datetime.datetime.now()

		self.year:int = self.now.year()
		self.month:int
		self.day:int

		self.weekDay:int

		self.partOfDay:bool

		self.hours:int
		self.minutes:int
		self.seconds:int

		# сезон
		# квартал