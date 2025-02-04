fp = open("text.txt" , "r") # this is open from reading
print(fp.read()) # read() methods gets the entire file content
fp.close() # this is good practice

# same thing using a context manager
#this is more pythonic!
with open("text.txt" , "r") as f:
    print(f.read())
# no need to close

# read the file line by line
with open("text.txt" , "r") as f:
    for line in f:
        print(line, end="")

with open("text.txt" , "r") as f:
    for line in f:
        print(line.rstrip())
