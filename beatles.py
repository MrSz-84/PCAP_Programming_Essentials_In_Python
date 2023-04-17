beatles = []

beatles.append("John Lennon")            
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(beatles)

for i in range(2):
    i = str(input("Enter another Beatles members Stu Sutcliffe and Pete Best:"))
    beatles.append(i) 

print(beatles)

del beatles[-1]
del beatles[-1]

beatles.insert(0, "Ringo Starr")
print(beatles)