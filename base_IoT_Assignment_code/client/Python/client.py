#Base Python client for MEng in IoT Assignment
#consumes data from IoT Gateway
import urllib2
import numpy as np
import matplotlib.pyplot as plt

plt.title (Temperature V Time)
plt.xlabel(Temperature degree C)
plt.ylabel(Time s)

response = urllib2.urlopen('http://localhost:8080/')
resp = response.read()

plt.show()

print resp
