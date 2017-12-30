import csv
import random
import copy
import math

def loadData(filename) :
    data=[]
    with open(filename, 'r') as file :
        read=csv.reader(file)
        data1=list(read)
        #data=float(data)
        for a in data :
            a.remove(a[-1])
        atribut=len(data1[0])
        index=len(data1)
        data2=missValue(data1,atribut)
        data3=normalize(data2)
    print(len(data3[0]))
    return data3,atribut,index

def normalize(dataset):
    for m in range(len(dataset[0])):
        #print(m)
        temp = []
        for n in range(len(dataset)):
            temp.append(float(dataset[n][m]))
        minimal = min(temp)
        maksimal = max(temp)
        #print(minimal, maksimal)
        for o in range(len(dataset)):
            if maksimal - minimal == 0:
                dataset[o][m] = temp[o]
            else:
                dataset[o][m] = (temp[o] - minimal) / (maksimal - minimal)
    return dataset

def missValue(dataset,panjang): #mencari missing value
    for x in range(panjang-1): #iterasi sebanyak jumlah attribut
        #print(x)
        rata = findRata(dataset,x) 
        #print(rata)
        for y in range(len(dataset)-1):
            if dataset[y][x] == 0  :
                dataset[y][x] = rata
    return dataset

def findRata(dataset,index): #mencari rata"
    jumlah=0 #buat nyari jumlah yang gak missing value
    total=0 #buat jumlah nilai
    for x in range(len(dataset)-1):
        if dataset[x][index] !=0:
            jumlah+=1
            #print str(x)+" "+str(index)
            total+=float(dataset[x][index])
    return float(float(total)/float(jumlah))

def pickRandom(dataset,k): #buat ambil random titik awal
    centroid=[]    
    #print ("Centroid awal:")
    i=0
    for i in range(k):
        count=0
        while True :
            pick=random.randint(count,count+10)
            if dataset[pick] not in centroid :
                break 
        count=pick
        if count > len(dataset) :
            count=0
        take=True
        stop=False
        while(not stop):
            take=True
            stop=False
            if(len(centroid)==0):
                stop=True
            for x in range(len(centroid)):
                if centroid[x]==pick:
                    take=False
                    stop=False
            if(take):
                stop=True
        if(take) :
            centroid.append(dataset[pick])
            print (str(pick+1)+": "+str(dataset[pick]))
    return centroid

def getNewCentroid(cluster,panjang,centroid=[]):
    for x in range(len(cluster)): #iterasi sebanyak cluster
        for y in range(panjang-1): #attribut
            jumlah = 0.0
            for z in range(len(cluster[x])):
                jumlah += cluster[x][z][y]
            jumlah /= len(cluster[x])
            output=round(jumlah,2)
            centroid[x][y]=output

def kMeans(dataset,centroid,k): #kmeans utama
    cluster=[] #array
    y=0
    for y in range(k):
        cluster.append([])
    for x in range(len(dataset)-1):
        cek=[]
        terkecil=0
        for y in range(k):
            #print (str(x) +" "+str(y)+" "+str(k)+" "+str(len(dataset)-1))
            cek.append(eucledianDistance(dataset[x],centroid[y],len(dataset[0])-1))
            terkecil = min(cek)
            #print(cek)
        for y in range(k):
            if cek[y] == terkecil:
                ss=[float(i) for i in dataset[x]]
                cluster[y].append(ss)
    return cluster

def eucledianDistance (instance1,instance2, length):
    distance = 0
    instance1=[float(i) for i in instance1]
    instance2=[float(i) for i in instance2]
    #print(instance1, instance2)
    #instance1=list(map(int, instance1)
    #instance2=list(map(int, instance2)
    for x in range(length):
        distance += pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)

#results = list(map(int, results))
filename=input("Nama File :")
n=input('Jumlah K : ')
n=int(n)
data, atribut, index = loadData(filename)
#data=[]
#for a in datas :
#    for x in a :
#        x=[float(i) for i in x]
#        del x[-1]
#        print(x)
#        data=x.append
centroid=pickRandom(data, n)
#centroid=list(map(int,centroid)
#print (centroid)
cluster=[]
while True: #loop sampai clusternya tidak berubah
    old=copy.deepcopy(centroid) #copy centroid yang lama buat dicek apakah berubah atau nggak
    cluster=kMeans(data,centroid,n) #membagi menjadi cluster (variable cluster isiya berubah, isinya pembagian berdasarkan cluster)
    #cluster=[float(i) for i in cluster]
    getNewCentroid(cluster,atribut,centroid) #mencari centroid baru (variable centroid isinya berubah, dapet centroid yang baru)   
    if centroid == old:
        break
i=1
#print(cluster[0][0])
for a in cluster :
    print("Cluster " + str(i) + ' :')
    i+=1    
    for x in a :
        print(x)
    print('\n')


