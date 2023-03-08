import Anderson_Darling_Test.AndersonDarlingTest as adt
from scipy.stats import norm
import random
#calculate probability that random value is less than 1.96 in normal CDF

r=[]
for i in range(100):
    r.append(random.normalvariate(10,.2))

dd=[]
for i in r:
    dd.append(norm.cdf((i-10)/.2))
x=adt.AndersonDarlingTest(dd)
print(x)


