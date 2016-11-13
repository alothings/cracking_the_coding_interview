def is_unique(st):
    l = [False]*128
    for char in st:
        print(char)
        c = ord(char)
        if l[c]: return False
        l[c] = True
    return True

# s = "hello"
s = "Heloh"
print(is_unique(s))
