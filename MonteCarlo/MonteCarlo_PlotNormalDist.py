from numpy.random import normal
from matplotlib import pyplot
# Dağılımın tanımı
mu = 50
sigma = 5
# Monte Carlo örneklerinin farklı örnek hacimlerinde hazırlanması
sizes = [100, 50, 100, 1000]
for i in range(len(sizes)):
	# generate sample
	sample = normal(mu, sigma, sizes[i])
	# Örnek histogram çizimi
	pyplot.subplot(2, 2, i+1)
	pyplot.hist(sample, bins=20)
	pyplot.title('%d Örnek' % sizes[i])
	pyplot.xticks([])
# show the plot
pyplot.show()