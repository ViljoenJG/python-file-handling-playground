numbers = [1, 2, 3]
infile = open('output.txt', 'w')

for i in numbers:
    infile.write(str(i) + '\n')

infile.close()
