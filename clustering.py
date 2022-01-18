import math
import matplotlib.pyplot as plt

class hrlper:
    def toFloat(self,x):
        for i in x:
            for j in range(len(i)):
                i[j] = float(i[j])

class cluster:
    def __init__(self):
        file = open('clustering/data.txt')
        lines = file.read().splitlines()
        self.data = []
        self.cost = []
        for line in lines:
            x=line.split()
            self.data.append(x)
        hlp=hrlper()
        hlp.toFloat(self.data)


    def distance(self,x,y):
        sum = 0
        for i in range(len(x)):
            s = (x[i]-y[i])*(x[i]-y[i])
            sum+=s
        return math.sqrt(sum)
    def mean(self,data,past):
        if len(data) == 0:
            return past
        result=[]
        for i in range(len(data[0])):
            result.append(0)
        count = 0
        for i in data:
            for j in range(len(i)):
                result[j]+=i[j]

            count+=1
        for i in range(len(result)):
            result[i]/=count
        return result


    def calculateE(self,c):

        for iteration in range(0,20):
            self.cost.append(0)
            centroides = []
            for i in range(0, len(c)):
                centroides.append([])

            for j in self.data:
                distances = []
                for i in range(0, len(c)):
                    distances.append(0)
                for i in range(0,len(c)):
                    distances[i]=self.distance(j,c[i])
                shortestdistance = min(distances)
                centroides[distances.index(shortestdistance)].append(j)
                self.cost[iteration]+= (shortestdistance*shortestdistance)

            for i in range(0,len(c)):
                c[i]=self.mean(centroides[i],c[i])

    def similarity(self,x,y):

        nom = 0
        for i in range(len(x)):
            s = x[i]*y[i]
            nom+=s
        length1=0
        for i in x:
            s=i*i
            length1+=s
        length2=0
        for i in y:
            s=i*i
            length2+=s
        dom=(math.sqrt(length1))*(math.sqrt(length2))
        return nom/dom

    def calculateC(self,c):


        for iteration in range(0,20):
            self.cost.append(0)
            centroides = []
            for i in range(0, len(c)):
                centroides.append([])
            for j in self.data:
                similarities = []
                for i in range(0, len(c)):
                    similarities.append(0)
                for i in range(0,len(c)):
                    similarities[i]=self.similarity(j,c[i])
                shortestdistance = max(similarities)
                centroides[similarities.index(shortestdistance)].append(j)
                self.cost[iteration]+= (shortestdistance)

            for i in range(len(c)):
                c[i]=self.mean(centroides[i],c[i])



file = open('clustering/c1.txt')
lines = file.read().splitlines()
c1=[]
c3=[]
for line in lines:
    x=line.split()
    c1.append(x)
    c3.append(list(x))
hlp = hrlper()
hlp.toFloat(c1)
hlp.toFloat(c3)

file = open('clustering/c2.txt')
lines = file.read().splitlines()
c2=[]
c4=[]
for line in lines:
    x=line.split()
    c2.append(x)
    c4.append(list(x))

hlp = hrlper()
hlp.toFloat(c2)
hlp.toFloat(c4)

oper1 = cluster()
oper2 = cluster()
oper3 = cluster()
oper4 = cluster()
number=[]
for i in range(20):
    number.append(i)




print("cosine")
oper1.calculateC(c1)
cost1=list(oper1.cost)
print(cost1)
print("cost percentage at 10 iteration: ",(cost1[0]-cost1[10])/cost1[0])
plt.plot(number,cost1,"r-",label='c1')


oper2.calculateC(c2)
cost2=list(oper2.cost)
print(cost2)
print("cost percentage at 10 iteration: ",(cost2[0]-cost2[10])/cost2[0])
plt.plot(number,cost2,"blue",label='c2')


plt.legend(loc='best')
plt.xlim(0, 20)
plt.xlabel('iterations')
plt.ylabel('cost')
plt.title("cosine")
plt.show()
print("**************************************************")
plt.clf()

print("euclidean")
oper3.calculateE(c3)
cost3=list(oper3.cost)
print(cost3)
print("cost percentage at 10 iteration: ",(cost3[0]-cost3[10])/cost3[0])
plt.plot(number,cost3,"r-",label='c1')


oper4.calculateE(c4)
cost4=list(oper4.cost)
print(cost4)
print("cost percentage at 10 iteration: ",(cost4[0]-cost4[10])/cost4[0])

plt.plot(number,cost4,"blue",label='c2')





plt.legend(loc='best')
plt.xlim(0, 20)
plt.title("euclidean")
plt.xlabel('iterations')
plt.ylabel('cost')
plt.show()

#yazan jarrar