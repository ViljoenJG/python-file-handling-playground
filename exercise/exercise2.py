def get_file_lines(loc):
    infile = open(loc, "r")
    content = infile.readlines()
    infile.close()
    return [i.rstrip("\n") for i in content]

lines = get_file_lines("fruits.txt")
for line in lines:
    print(len(line))
