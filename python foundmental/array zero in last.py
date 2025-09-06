number=[1,25,8,0,5,0,88,0,12]
nonzeroindex=0
for i in range(len(number)):
   
    if number[i] !=0:
        
           number[i], number[nonzeroindex]=number[nonzeroindex],number[i]

           nonzeroindex+=1           

print(number)

