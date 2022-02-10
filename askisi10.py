import re
f = open("askisi10text.txt", "r").read()
ascii=list(f)

for i in range(len(ascii)):
    ascii[i]=bin(ord(ascii[i]))[2:4]+bin(ord(ascii[i]))[-2:]

length=len("".join(ascii))
if length%16!=0:
    merged="".join(ascii)[:length]
merged=re.findall('................',"".join(ascii))
    
for i in range(len(merged)):
    merged[i]=int(merged[i],2)

zugoi=0
dia3=0
dia5=0
dia7=0
for number in merged:
    if number%2==0:
        zugoi+=1
    if number%3==0:
        dia3+=1
    if number%5==0:
        dia5+=1
    if number%7==0:
        dia7+=1


print("Zugoi:"+str((zugoi/len(merged))*100)+"%")
print("Dia 3:"+str((dia3/len(merged))*100)+"%")
print("Dia 5:"+str((dia5/len(merged))*100)+"%")
print("Dia 7:"+str((dia7/len(merged))*100)+"%")

