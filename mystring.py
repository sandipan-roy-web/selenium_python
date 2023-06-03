str='This is Python'
mylist=str.split(" ")
print(mylist)
newlist=[]
new_list=reversed(mylist)
for i in new_list:
    print(i)


def check_cases(S):
    d = {"upper": 0, "lower": 0}
    for word in S:
        if word.isupper():
            d['upper'] += 1
        elif word.islower():
            d['lower'] += 1
        else:
            pass
    print("The number of upper case characters =" ,d['upper'])
    print("The number of lower case characters =", d['lower'])



