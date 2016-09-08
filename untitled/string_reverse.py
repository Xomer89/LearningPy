def string_rev(s):
    a = ""
    dec = len(s) - 1
    for i in range(dec):
        a = s[i]
        s = a + s[i+1::dec]
        dec -= 1
    print(s)
    return s

s1 = "abcdef"
string_rev(s1)
