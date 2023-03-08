#import scipy.stats as stats
import random
import scipy.stats as stats

randomNumbers=[]
s=[0,0,0,0,0,0,0,0,0,0,0,0,0]
N= 100
for i in range(0, N):
	rnd = random.randint(0, 10)
	randomNumbers.append(rnd)
for i in range(0,N):
	for j in range(0,10):
		if (randomNumbers[i] == j):
			s[j] = s[j] +1
print (randomNumbers)
for i in range(0,10):
	print("S", i," " ,s[i])
chi=0
for i in range(0,10):
	chi= chi + ((s[i]-N/10)**2)/(N/10)
print("chi ", chi)

chiTableVal=stats.chi2.cdf(chi, 10-1)

if (chi>chiTableVal):
	print("Ret")
else:
	print("Kabul")