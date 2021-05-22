stars = 1

row = int(input("Enter the number of rows: "))

while row>0:
    print(""*row+""+stars*"*")
    stars = stars + 1
    row = row - 1
    