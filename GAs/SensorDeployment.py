import random
X=int(input("X : "))
Y=int(input("Y : "))
Sensor=int(input("# of Sensors : "))


goalL=[]
goal="max ="
goalL.append(goal)
for sensor in range (Sensor):
    for x in range(1,X+1):
        for y in range(1,Y+1):
            s="x"+str(sensor)+str(x)+str(y)
            s +="*("
            for i in range(1,X+1):
                for j in range(1,Y+1):
                    if (i==x and y==j):
                        pass
                    else:
                        s +=str(random.randint(60,100)/100)+"*y"+str(sensor)+str(i)+str(j)+"+"
            s=s[:-1]
            s +=")+"
           #print(s)
            goalL.append(s)
            #goal +=s

goalL[len(goalL)-1]  = goalL[len(goalL)-1] [:-1]
goalL[len(goalL)-1]  = goalL[len(goalL)-1] + ";"
constraints=[]
for x in range(1,X+1):
    for y in range(1, Y+1):
        c=""
        c2=""
        for sensor in range(Sensor):
            c +="y"+str(sensor)+str(x)+str(y)+"+"
            c2 += "x" + str(sensor) + str(x) + str(y) + "+"
        c =c[:-1]
        c2 =c2[:-1]
        c +="<=1;"#+c2+";"
        constraints.append(c)

for sensor in range (Sensor):
    c=""
    for x in range(1,X+1):
        for y in range(1,Y+1):
            c +="y"+str(sensor)+str(x)+str(y)+"+"
    c=c[:-1]
    c+="=1;"
    constraints.append(c)


for x in range(1,X+1):
    for y in range(1, Y+1):
        c=""
        for sensor in range(Sensor):
            c +="x"+str(sensor)+str(x)+str(y)+"+"
        c =c[:-1]
        c +="<=1;"
        constraints.append(c)

for sensor in range(Sensor):
    c=""
    for x in range(1,X+1):
        for y in range(1,Y+1):
            c +="x"+str(sensor)+str(x)+str(y)+"+"
    c=c[:-1]
    c+="<=1;"
    constraints.append(c)

for sensor in range (Sensor):
    for x in range(1,X+1):
        for y in range(1,Y+1):
            constraints.append("@bin(x"+str(sensor)+str(x)+str(y)+");")
            constraints.append("@bin(y" + str(sensor) + str(x) + str(y) + ");")
for i in constraints:
    print(i)

f=open("D://temp//SensorCoverage"+str(Sensor)+"."+str(X)+"."+str(Y)+".txt", "w")

for i in goalL:
    f.write(i + chr(13))
for i in constraints:
    f.write(i+chr(13))

f.close()