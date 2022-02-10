from ast import While
import random
def is_finished(tablo,kapakia):
    if kapakia['s']==kapakia['m']==kapakia['l']==0:
        return True
    elif tablo[0][0]==tablo[0][1]==tablo[0][2]!=0 or tablo[0]==["s","m","l"] or tablo[0]==["l","m","s"]:
        return True
    elif tablo[1][0]==tablo[1][1]==tablo[1][2]!=0 or tablo[1]==["s","m","l"] or tablo[1]==["l","m","s"]:
        return True
    elif tablo[2][0]==tablo[2][1]==tablo[2][2]!=0 or tablo[2]==["s","m","l"] or tablo[2]==["l","m","s"]:
        return True
    elif tablo[0][0]==tablo[1][0]==tablo[2][0]!=0 or [tablo[0][0],tablo[1][0],tablo[2][0]]==["s","m","l"] or [tablo[0][0],tablo[1][0],tablo[2][0]]==["l","m","s"]:
        return True
    elif tablo[0][1]==tablo[1][1]==tablo[2][1]!=0 or [tablo[0][1],tablo[1][1],tablo[2][1]]==["s","m","l"] or [tablo[0][1],tablo[1][1],tablo[2][1]]==["l","m","s"]:
        return True
    elif tablo[0][2]==tablo[1][2]==tablo[2][2]!=0 or [tablo[0][2],tablo[1][2],tablo[2][2]]==["s","m","l"] or [tablo[0][2],tablo[1][2],tablo[2][2]]==["l","m","s"]:
        return True
    elif tablo[0][0]==tablo[1][1]==tablo[2][2]!=0 or [tablo[0][0],tablo[1][1],tablo[2][2]]==["s","m","l"] or [tablo[0][0],tablo[1][1],tablo[2][2]]==["l","m","s"]:
        return True
    elif tablo[0][2]==tablo[1][1]==tablo[2][0]!=0 or [tablo[0][2],tablo[1][1],tablo[2][0]]==["s","m","l"] or [tablo[0][2],tablo[1][1],tablo[2][0]]==["l","m","s"]:
        return True
    else: 
        return False


total_sum=0
sizes=['s','m','l']
for i in range(100):
    kapakia={"s":9,"m":9,"l":9}
    tablo=[[0,0,0],[0,0,0],[0,0,0]]
    sum=0
    while True:
        x=random.randint(0,2)
        y=random.randint(0,2)
        kapaki=sizes[random.randint(0,2)]
        position=tablo[x][y]
        if (position==0 or sizes.index(position)<sizes.index(kapaki)):
            kapakia[kapaki]=kapakia[kapaki]-1
            tablo[x][y]=kapaki
            sum+=1
        if is_finished(tablo,kapakia):
            total_sum=total_sum+sum
            break
print(total_sum/100)


    


