inp=int(input("Enter a number lesser than 25: "))
if inp<25:
    while inp<26:
        print("Inside the loop, my variable is", inp)
        inp+=1
else:
    print("ERROR")