string = '1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1'
ones = 0
ls = 0

for x in string:
    if x == '1':
        ones += 1
    elif x == 'l':
        ls += 1
    else:
        print 'error'

print 'Ones = ' + str(ones), 'L\'s = ' + str(ls)
