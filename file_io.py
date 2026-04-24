# reading file
f= open("main.txt")
data = f.read()
print(data)
f.close()


# write file
add = "hey he is student of SOIT RGPV Bhopal"
f = open("main2.txt", "a")
f.write(add)
f.close()


# close case 
with open("main.txt") as f:
    print(f.read())
    # dont need to explicitly close the file