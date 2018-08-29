#Question 1
with open('test.txt','r') as f:
    n=int(input("Enter The number of lines you want to enter"))
    for i in range(n):
        x=f.readline()
        print(x)

#Question 2
with open('test.txt','r') as f:
    n=input("Enter The word You want to find")
    x=f.read()
    print(x)
    y=x.count(n)
    print(y)

#Question 3
f=open('test.txt','r')
e=open('test1.txt','w')
x=f.read()
e.write(x)
f.close()
e.close()

#Question 4
with open('test.txt') as f1,open('test2.txt') as f2 ,open('combine.txt','w') as f3:
    for i,j in zip(f1,f2):
        f3.write(i+j)
        
#Question 5
import random
li3=[]
f=open('test.txt','w')
for i in range(10):
    a=str(random.randrange(100))
    f.write(a)
    f.write('\n')
f.close()
f=open('test.txt')
data=f.read()
data2=data.split()
for i in data2:
    li3.append(int(i))
li3.sort()
e=open("text4.txt",'w')
for i in li3:
    e.write(str(i)+'\n')
e.close()
e=open("text4.txt",'r')
print(e.read())
