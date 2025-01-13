def invertstr(s):
    invs = ''
    for i in s:
        invs = i + invs
    return invs
s = 'gabriel'
print(invertstr(s))
