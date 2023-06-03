#file = open('read.txt')
#print(file.read())

#with open('read.txt') as tt:
    #print(tt.read())

#with open('read.txt') as tf:
    #print(tf.readline())

with open('read.txt') as tt:
    for line in tt.readlines():
        print(line)

