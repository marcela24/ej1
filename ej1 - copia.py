ts=int(input("tiempo segundos"))
h=int(input("hora"))
m=int(input("minutos"))
s=int(input("segundos"))
m=m*60
h=h*3600
tt=s+m+h

t=ts-tt
if t>=0:
    print("finaliza")
else:
    print("no finaliza")
    
