import random

def paixnidi(x,y):
    pirgos=0
    aksiomatikos=0
    for i in range(100):
        xp=random.randint(0,x-1)
        yp=random.randint(0,y-1)
        xa=random.randint(0,x-1)
        ya=random.randint(0,y-1)
        while ([xp,yp]==[xa,ya]):
            xa=random.randint(0,x-1)
            ya=random.randint(0,y-1)
        curr=random.randint(0,1)
        while ([xp,yp]!=[xa,ya]):
            if curr==0:
                choosemove=random.randint(0,3)
                if choosemove==0:
                    if xp-1>=0:
                        xp=random.randint(0,xp-1)
                elif choosemove==1:
                    if xp+1<=x:
                        xp=random.randint(xp+1,x)
                elif choosemove==2:
                    if yp-1>=0:
                        yp=random.randint(0,yp-1)
                else:
                    if yp+1<=y:
                        yp=random.randint(yp+1,y)
                if [xp,yp]==[xa,ya]:
                        pirgos+=1
                curr=1
            else:
                choosemove=random.randint(0,3)
                if choosemove==0:
                    if xa<ya:
                        amount=random.randint(0,xa)
                    else:
                        amount=random.randint(0,ya)
                    xa,ya=xa-amount,ya-amount
                elif choosemove==1:
                    if y-ya<=xa:
                        amount=random.randint(0,y-ya)
                    else:
                        amount=random.randint(0,xa)
                    xa,ya=xa-amount,ya+amount
                elif choosemove==2:
                    if x-xa<=ya:
                        amount=random.randint(0,x-xa)
                    else:
                        amount=random.randint(0,ya)
                    xa,ya=xa+amount,ya-amount
                else:
                    if xa<ya:
                        amount=random.randint(0,y-ya)
                    else:
                        amount=random.randint(0,x-xa)
                    xa,ya=xa+amount,ya+amount
                if [xp,yp]==[xa,ya]:
                        aksiomatikos+=1
                curr=0
    return pirgos,aksiomatikos

p,a=paixnidi(8,8)
print("8x8 - "+"Pyrgos:"+str(p)+" Aksiomatikos:"+str(a))    
p,a=paixnidi(7,8)
print("7x8 - "+"Pyrgos:"+str(p)+" Aksiomatikos:"+str(a))  
p,a=paixnidi(7,7)
print("7x7 - "+"Pyrgos:"+str(p)+" Aksiomatikos:"+str(a))  





