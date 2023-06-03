# so we are reading a file in 'r' mode ,reading the lines and store it as list ,list is reversed using the reversed()
# function reading the reversed list using for loop and writing back to the file
with open('read.txt', 'r') as tt:
    content = tt.readlines()
    with open('read.txt','w') as wr:
        for line in reversed(content):
            wr.write(line)

