import sys
import wave
f = wave.open(sys.argv[1], 'w')
f.setnchannels(4)
f.setsampwidth(4)
f.setframerate(98)
x = []
for letters in sys.argv[1]:
    x.append(letters)
for letter in sys.argv[2]:
    x.append(letter)
for letter in sys.argv[3]:
    x.append(letter)
for letter in sys.argv[4]:
    x.append(letter)
with open(sys.argv[4], "r") as d:
    for line in d:
        for let in line:
            v = lambda c: abs(int(ord(let)) - ord(c) - 96)
            print(list(map(v, x)), end="")
            f.writeframesraw(bytes(str(list(map(v, x))).encode("utf-8")))
    f.writeframes(b"")
with open(sys.argv[3], 'r') as w:
    for line in w:
        for let in line:
            v = lambda c: abs(int(ord(let)) - ord(c) - 96)
            print(list(map(v, x)), end="")
            f.writeframesraw(bytes(str(list(map(v, x))).encode("utf-8")))
    f.writeframes(b"")