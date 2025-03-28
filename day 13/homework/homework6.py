number=int(input('please enter number: '))
if number < 2:
    print(number, "is not prime")
else:
    num=True
    for i in range(2,number):
        if number %i ==0:
            num=False
        break
    if num:
        print(num,'is prime')
    else:
        print(num,'is not prime')
    
            
