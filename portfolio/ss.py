from random import choices

a = 'python'
result = []
for i in a:
    a = choices([i.lower(), i.upper()])
    result.append(a)
print(result)