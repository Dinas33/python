while True :
  try:
 
   w=input()
   if w== '' :
    raise ValueError('enter the value')
   w=int(w)
   if w in range(1,101):
    if w%2 ==0 and w>2:
     print('yes')
    else:
     print('no')
     break
   else:
     print('error weight range 1:100')
  except ValueError :
     print('error  its empty enter the value')

