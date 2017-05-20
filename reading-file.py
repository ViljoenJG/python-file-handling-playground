file = open('textfile.txt', 'r')
content = file.readlines()
content = [i.rstrip('\n') for i in content]

print(content)
file.close()
