class Time:
	def __init__(self, hour=0, minute=0, second=0):
		self._hour = hour # Private attribute
		self._minute = minute # Private attribute
		self._second = second # Private attribute

	def __add__(self, other):
		total_seconds = self._hour * 3600 + self._minute * 60 + self._second + other._hour * 3600 + other._minute * 60 + other._second

		new_hour, remainder = divmod(total_seconds, 3600)
		new_minute, new_second = divmod(remainder, 60)

		return Time(new_hour, new_minute, new_second)

	def __str__(self):
		return f"{self._hour:02d}:{self._minute:02d}:{self._second:02d}"
	
a=int(input("Enter the hour1 "))
b=int(input("Enter the minute1 "))
c=int(input("Enter the seconds1 "))

d=int(input("Enter the hour2 "))
e=int(input("Enter the minute2 "))
f=int(input("Enter the seconds2 "))

time1 = Time(a, b, c)
time2 = Time(d, e, f)	

sum_time = time1 + time2
print("Time 1:", time1)
print("Time 2:", time2)
print("Sum of Time 1 and Time 2:", sum_time)
