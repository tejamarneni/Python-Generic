def desirum(num):
    s = 0
    temp = num
    while num > 0:
        n = num % 10
        n2 = n**(len(str(num)))
        s = s + n2
        num = num // 10   
    num = temp        
    if s == num:
        print(num,"is a disarium")  
    else:
        print(num,"is not a disarium")  

desirum(175)                  