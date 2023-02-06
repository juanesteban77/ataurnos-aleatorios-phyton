import random
x=1;
y=2;
cont =0;
cont2=0
cont1=0

while cont<=10:
    cont1+1
    cont+=1
    cedula=int(input("ingrese su cedula \n"))
    print (f" cliente con la decula {cedula} - su turno es {cedula}-N-{cont} eres cliente normal")
if cont==1:
    cont2+1
    print (f" cliente con la decula {cedula} - su turno es {cedula}-P-{cont} eres cliente preferencial")
    print(f"la cantidad de normales es {cont1}")
    print(f"la cantidad de prefereanciales es {cont2}")


            
 




