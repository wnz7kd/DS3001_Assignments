"""
Question 1:
I was suprised at the amount of jobs that only required a Bachelor's degree.
I think especially now a lot of skills can be aquired by simply doing a job, and
most occupations don't need highly-specialized workers in order for the to be
productive/successful. I also noticed that even the higher-paying trade jobs
didn't really compete with other jobs on the spreadsheet, maybe indication why
there are shortages of workers in these areas.

I would put the jobs in this order:
Economist, Data Scientist, Management Analyst, Marketing Manager, Personal Financial
Advisor, Postsecondary Teacher, Budget Analyst, Accountant, Welder.
I ranked them this way based off of perceived personal fufillment. A part of this
would be making a good salary, but also feeling like the work I am doing is
meaningful and I am serving people I am proud of.
"""
import numpy as np
from matplotlib import pyplot as plt

points = np.linspace(0, 1, 50)
y = np.log(points)
z = np.exp(points)
plt.scatter(points,y, label = 'Log')
plt.scatter(points,z,label = 'Exponential' )
plt.legend(loc = 'lower right')

plt.title("Natural Log and Exponential Functions")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()



points1 = np.linspace(-6.5, 6.5, 100)
y1 = np.sin(points1)
z1 = np.cos(points1)
plt.plot(points1,y1, label = 'Sin')
plt.plot(points1,z1,label = 'Cos' )
plt.legend(loc = 'lower left')

plt.title("Sin and Cos Functions")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")