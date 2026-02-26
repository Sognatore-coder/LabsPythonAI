n = int(input())
permissions = {}

for _ in range(n):
    data = input().split()
    filename = data[0]
    ops = data[1:]
    permissions[filename] = set(ops)

m = int(input())
for _ in range(m):
    op, filename = input().split()
    if op == "read":
        op = "R"
    elif op == "write":
        op = "W"
    elif op == "execute":
        op = "X"
    
    if filename in permissions and op in permissions[filename]:
        print("OK")
    else:
        print("Access denied")