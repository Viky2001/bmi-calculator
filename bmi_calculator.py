# importing modules
from tkinter import StringVar
from pywebio.input import *
from pywebio.output import *

# classify person
class calculation:

	# defining method
	def BMIcalculator(Height, Mass):

		for t1, t2 in [(16, 'severely underweight'),
					(18.5, 'underweight'),
					(25, 'normal'),
					(30, 'overweight'),
					(35, 'moderately obese'),
					(float('inf'), 'severely obese')]:
			if BMI <= t1:
				put_text('Your BMI is', BMI, 'and the person is :', t2)
				break

# classify and compute BMI
class calculation:

	# defining method
	def BMIcalculator(self, Height, Mass):

		# compute BMI
		BMI = (Mass)/(Height*Height)

		# classify
		for t1, t2 in [(16, 'severely underweight'),
					(18.5, 'underweight'),
					(25, 'normal'), (30, 'overweight'),
					(35, 'moderately obese'),
					(float('inf'), 'severely obese')]:

			if BMI <= t1:
				put_text('Your BMI is', BMI, 'and the person is :', t2)
				break


# height input
Height = input("Please enter height in meters(m)", type=FLOAT)

# Mass input
Mass = input("Please enter Mass/Weight in Kilograms(Kg)", type=FLOAT)

obj = calculation()
obj.BMIcalculator(Height, Mass)

try:
	from googlesearch import search
except ImportError:
	#print("No module named 'google' found")
	put_text("No module named /'google'/ found")
				

# to search input
location=input("Please enter your location to find the near by GYMs")

query = "gyms near {0}".format(location)

for j in search(query):
	put_text(j)

