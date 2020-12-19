num=input()
if num.isdigit() and len(num)>1:
    digits=[]
    for i in str(num):
        digits.append(int(i))
    digits.sort(reverse=True)
    Max=""
    for k in digits:
        Max+=str(k)
    print(int(Max))
        
