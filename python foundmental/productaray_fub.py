def sign_fun():
 arr = input('enter array: ')        
 arr1 = list(map(int, arr.split())) 
 p=1
 for i in arr1:
  p*=i

 return print('1')if p>0 else print('-1') if p<0  else print('0')

sign_fun()



