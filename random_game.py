import random

def sec_num():
    s_num = random.randint(1,101)
    try:
        c = 0
        while True:
            u_num = int(input("Enter a number:\n"))
            if u_num > 0 and u_num > s_num:
                print("To Big. Try again")
                c += 1
                continue
            elif u_num > 0 and u_num < s_num:
                print("Too small. Try again")
                c += 1
                continue
            elif u_num < 0:
                print("Please Enter a Positive Number.") 
                c += 1
                continue
            else:
                c += 1
                print(f"Congratulations.You got in {c} trials")
                break 
    except ValueError:
        print("Your Entry is invalid. Please enter integer numbers only.")        

sec_num()
