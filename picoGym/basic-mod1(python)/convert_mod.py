import string

candidate = string.ascii_uppercase + string.digits + '_'
arr = [165,248,94,346,299,73,198,221,313,137,205,87,336,110,186,69,223,213,216,216,177,138]

for a in arr:
     print(candidate[a%37], end='')
