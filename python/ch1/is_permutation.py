def is_permutation(s1, s2):
    if len(s1) != len(s2): return False
    return sorted(s1) == sorted(s2)

def is_permutation2(s1, s2):
    # Cooler way, without sorting (and O(n))
    if len(s1) != len(s2): return False

    l = [0]*128
    for char in s1:
        l[ord(char)] += 1
    for char in s1:
        l[ord(char)] -= 1
        if l[ord(char)] < 0: return False
    return True


s1 = "iam lord voldemort"
s2 = "tom marvolo riddle"

print(is_permutation2(s1, s2))