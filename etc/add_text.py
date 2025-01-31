lines = ["test\n"]
f = open("test.txt", "a")
f.writelines(lines)
#f.close()

#f = open("test.txt")
print(f.read())
f.close()