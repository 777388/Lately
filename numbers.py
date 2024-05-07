v = ["o", "t", "t", "f", "f", "s", "s", "e", "n"]
i = ["n", "w", "h", "o", "i", "i", "e", "i", "i"]
e = ["e", "o", "r", "u", "v", "x", "v", "g", "n"]
n = [".", ".", "e", "r", "e", "/", "e", "h", "e"]
l = ["+", "+", "e", "7", "6", "5", "n", "t", "-"]
u = ["5", "4", "3", "2", "1", "0", "1", "8", "9"]
set(bin(str(enumerate.__call__())))
print(set(v).symmetric_difference(set(u)))
print(set(i).symmetric_difference(set(l)))
print(set(e).symmetric_difference(set(n)))