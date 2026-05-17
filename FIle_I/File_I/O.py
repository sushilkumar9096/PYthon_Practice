f = open("2.py", "r")
data = f.readline()
print(data)
print(type(data))
f.close()


# r -> Read Mode
f = open("2.py", "r")
print(f.read())
f.close()


# w -> Write Mode (overwrites old content)
f = open("2.py", "w")
f.write("Hello World")
f.close()


# a -> Append Mode
f = open("2.py", "a")
f.write("\nNew Line Added")
f.close()


# r+ -> Read and Write
f = open("2.py", "r+")
print(f.read())
f.write("\nAdded using r+")
f.close()


# w+ -> Write and Read
f = open("2.py", "w+")
f.write("Python File")
f.seek(0)
print(f.read())
f.close()


# a+ -> Append and Read
f = open("2.py", "a+")
f.write("\nAppended using a+")
f.seek(0)
print(f.read())
f.close()


# rb -> Read Binary
f = open("2.py", "rb")
data = f.read()
print(data)
f.close()


# wb -> Write Binary
f = open("2.py", "wb")
f.write(b"Binary Write")
f.close()


# ab -> Append Binary
f = open("2.py", "ab")
f.write(b"\nBinary Append")
f.close()