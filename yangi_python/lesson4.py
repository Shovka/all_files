def salon(sa):
    s = 1
    if s==2:
        return sa
    else:
        return salon()

@salon
def a(ob):
    return 'ishladi'
print(a(1))