a = [4, 5, 6]

def modify_part(x):
    a[0] = x

def modify_whole(x):
    global a
    a = x

modify_part(100)
print a

modify_whole(100)
print a