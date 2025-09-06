
def ismonotonic():
 mono=list(map(int,input ('input arrau nubers with space').split()))
 mono_incresing= all(mono[i]>= mono[i+1] for i in range(len(mono)-1))
 mono_decresing= all(mono[i]<= mono[i+1] for i in range(len(mono)-1))
 return mono_decresing or mono_incresing
 
print(ismonotonic())