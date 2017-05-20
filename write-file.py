source = open('textfile.txt', 'r')
target = open('output/writeOutput.txt', 'w')

contentLines = source.readlines()
content = [i.rstrip('\n') for i in contentLines]

for item in content:
    target.write(item + '\n')

target.close()
source.close()
