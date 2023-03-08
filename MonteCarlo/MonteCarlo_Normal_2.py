import matplotlib.pyplot as plt
import numpy as np


def Ploting(mu, sigma):
    s = np.random.normal(mu, sigma, 1000)
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth=2,
             color='r')
    plt.show()


mu=float(input("Ortalama "))
sigma=float(input("Standart Sapma "))

Ploting(mu,sigma)
