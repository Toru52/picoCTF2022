import string

candidate = string.ascii_uppercase + string.digits + '_'
arr = [268,413,438,313,426,337,272,188,392,338,77,332,139,113,92,239,247,120,419,72,295,190,131]

for a in arr:
     print(candidate[pow(a, -1, 41)-1], end='')
