# str
a = "abc"
print(a, type(a))
# int
b = 4
print(b, type(b))

# float
c = 4.5
print(c, type(c))

# omplex
d = 3 + 4j
print(d, type(d))

# list
f = [1, 2, 3]
print(f, type(f))

#t tuple 
e = (1,2,3)
print(e, type(e))

# range
g = range(5)
print(g, type(g))
h = list(range(5))
print(h)
i = list(range(2, 6)) # range(start,stop)
print(i)
j = list(range(1, 10, 2)) # range(start, stop, step)
print(j)

# map -> dict
k = {"name" : "rama", "age" : 20}
print(k, type(k))
l = dict(name = "rama", age = 20)
print(l, type(l))

# set 
m = {"a", "b" ,"c" , "a"}
print(m, type(m))
n = set(("a", "b", "b"))
print(n, type(n))

# bool
o , p = True, False
print(o, type(o))
print(p, type(p))


