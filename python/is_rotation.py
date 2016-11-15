def is_rotation(s1, s2):
    if len(s1) != len(s2): return False
    s1 = s1 + s1
    # print(s1)
    return s2 in s1

s1 = "sometime"
s2 = "timesome"
print(is_rotation(s1, s2))