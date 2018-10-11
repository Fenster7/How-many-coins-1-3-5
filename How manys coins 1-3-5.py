total = int(input("What is the total worth of your coins?"))

five = int(total/5)
three = int((total - (five * 5)) / 3)
one = int(total - ((five * 5) + (three * 3)))


print("You have these coins:", five, "5 coin(s)", three, "3 coin(s)", one, "1 coin(s)")
