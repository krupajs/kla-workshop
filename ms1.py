file_path='C:/Users/krupa/Desktop/kla-workshop/Workshop2024/Milestone1/Input/Testcase4.txt'

l=[]
with open(file_path,'r') as file:
    for line in file:
        s=''
        for i in range(len(line)):
            if line[i] in ['0','1','2','3','4','5','6','7','8','9']:
                s=s+line[i]
        s=int(s)
        l.append(s)
f=open("new4s.txt","w+")
import math
print(l)
wd=l[0]
r=wd/2
n=l[1]
ang=l[2]
rad=(ang* math.pi)/180
c1=0
x1=r*(math.cos(rad))
y1=r*(math.sin(rad))


coord0=(str((x1,y1)))+"\n"
print(coord0[0],coord0[1])

x2=2*c1-x1
y2=2*c1-y1
coord1=(str((x2,y2)))+"\n"
p=0
mr=1
nr=n-2
f.write(coord0)
while(p!=n-2):
    x=(mr*x1+nr*x2)/(mr+nr)
    y=(mr*y1+nr*y2)/(mr+nr)
    mr=mr+1
    nr=nr-1
    coord=x,y
    coord=(str(coord))+"\n"
    f.write(coord)
    p+=1

f.write(coord1)
f.close()


