f = open('temp/demo.txt', mode='w')
f.write('Hello from Python')
f.close()

f = open('temp/demo.txt', mode='r')
content = f.read()
f.close()
print(content)

f = open('temp/demo2.txt', mode='w')
f.write('Hello\n')
f.write('world\n')
f.write('from\n')
f.write('Python.')
f.close()

f = open('temp/demo2.txt', mode="r")
content = f.read()
f.close()
print(content)

f = open('temp/demo2.txt', mode="r")
content = f.readlines()
f.close()
print(content)
for line in content:
  print(line[:-1])

f = open('temp/demo2.txt', mode="r")
line = f.readline()
while line:
  print(line[:-1])
  line = f.readline()

# using with to automaticaly call close()
with open('temp/demo2.txt', mode="r") as f:
  print(f.read())