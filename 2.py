a=3721
hh = a//3600%24
mm = str(a%3600//60//10)+str(a%3600//60%10)
ss = str(a%3600%60/10)+' '+str(a%3600%60%10)
print(hh,mm,ss,sep=':')