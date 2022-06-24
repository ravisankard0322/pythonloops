# pythonloops
#python divisorpattern
def divisoroattern(x):
  for i in range(1,x+1):
    for j in range(1,x+1):
      if((i%j==0)or(j%i==0):
         print("*",end=' ')
      else:
         print(" ",end=" ")
    print(i)
         
         
