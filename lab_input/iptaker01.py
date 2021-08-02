name = input("what's your name: ")
from datetime import datetime
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = days[datetime.now().weekday()]

print("Hello, " + name + "! " + "HAPPY " + day + "!")
