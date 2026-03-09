a = (input("what is your name? "))
b = (int(input("what is your age? ")))
mom = (int(input(f"{a} what is your mum age? ")))

bornmumage = (mom - b)

print(f"Hi!, {a} ")
print(f"you have {b} years old")
print(f"Your Mum had you at {bornmumage} years old")