print("ciao mondooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
# ciao

f= open("guru99.txt","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
     print("ciao ciao ciao")
f.close()