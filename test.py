from coda import coda

c=coda()
for i in range(10):
    c.push(i)

d=coda()
d=c

while not d.empty():
    print(f"D={d.front()}")
    print(f"D={d.front()}")
    print(f"C={c.front()}")

    d.pop()
    c.pop()

while not c.empty():
    print(f"C1={c.front()}")

    c.pop()

