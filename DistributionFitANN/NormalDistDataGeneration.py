import matplotlib.pyplot as plt
import random

#import xlrd
#import xlwt
def Tablo(L):
    for i in L:
        print(i, "  ", i[1]-i[0])

def Frekans(L, interval,mlt):
    intervalwFrekans=[]
    for i in interval:
        sayac=0
        for j in L:
            if (j >=i[0] and j<i[1]):
                sayac +=1
        r=[i[0],i[1], sayac]
        intervalwFrekans.append(r)

    return intervalwFrekans

def SeriKontrol(data):
    mn=min(data)
    mx=max(data)
    mlt=1
    newData=data
    while (mx-mn)/10 <=5:
        newData=[]
        mlt *=10
        for i in data:
            newData.append(i*mlt)
        mn=min(newData)
        mx=max(newData)
    return newData,mlt

def Uniform(P):
    a=P[0]
    b=P[1]
    adet=P[2]
    data=[]
    for i in range(adet):
        data.append(random.uniform(a,b))
    return data

def Beta(P):
    alpha=P[0]
    beta=P[1]
    adet=P[2]
    data=[]
    for i in range(adet):
        data.append(random.betavariate(alpha,beta))
    return data


def Normal(P):
    mu=P[0]
    std=P[1]
    adet=P[2]
    data=[]
    for i in range(adet):
        data.append(random.normalvariate(mu, std))
    return data

def Ustel(P):
    mu=P[0]
    data=[]
    for i in range(P[2]):
        data.append(random.expovariate(mu))
    return data



dict={"Normal":Normal, "Ustel":Ustel, "Beta":Beta, "Uniform":Uniform}
dagilim=input("Dagılım Normal/Ustel/Uniform/Beta ")
average=float(input("Param 1 "))
std=float(input("Param 2 "))
adet=int(input("Kaç adet "))
#wb = xlwt.Workbook()
#ws = wb.add_sheet('Normal Dist')

#for i in range(500):
#    ws.write(i,0, random.normalvariate(average,std))



#wb.save("C://Academic//Kitap//Simülasyon//Codes//DistributionFitANN//normalDist.xls")

#wbRead=xlrd.open_workbook("C://Academic//Kitap//Simülasyon//Codes//DistributionFitANN//normalDist.xls")
#wsRead=wbRead.sheet_by_index(0)

#for i in range(wsRead.nrows):
#    data.append(wsRead.cell_value(i,0))

data = dict[dagilim]([average, std,adet])
data,mlt=SeriKontrol(data)
mn=min(data)
mx=max(data)

inter=int((mx-mn)/10)




intervals=[]
for i in range(10):
    alt=mn+i*inter
    ust=mn+(i+1)*inter
    intervals.append([alt, ust])

intervals.append([ust, mx])



#print(Frekans(data,intervals))
datawf=Frekans(data,intervals,mlt)
Tablo(datawf)
xaxis=[]
yaxis=[]
for i in datawf:
    x=((i[0]+i[1])/2)
    xaxis.append(x)
    y=i[2]
    yaxis.append(y)

plt.bar(xaxis,yaxis, width =inter-.5)
plt.plot(xaxis,yaxis)

plt.show()
