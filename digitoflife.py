def result(inp):
    add = 0
    for i in str(inp):
        add += int(i)
    if len(str(add)) > 1:
        return result(add)
    return add

inp = int(input())
print(result(inp))