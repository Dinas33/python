s=input("enter string")
s_dd=input('enter add char')
final_s= s+s_dd
result=0
for car in final_s:
    result^=ord(car)
    

print(chr(result))