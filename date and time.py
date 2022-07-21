# using datetime module
from datetime import datetime
# string
my_date_string = "Mar 11 2011 11:31AM"
# displaying the string in date time format
datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')
print(type(datetime_object))
print(datetime_object)
# getting the current time
now = datetime.now()
# displaying the current time in the particular format
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
