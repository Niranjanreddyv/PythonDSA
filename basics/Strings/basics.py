print('It"s')
print("it's")
a = "hello, world"
print(a[1])

# loop in strings

for x in a:
    print(x)
print(len(a))

# check string 

txt = "the best things in life are free!"
print("free" in txt)
if "best" in txt:
    print("yes, 'best' is present")
else:
    print("no, 'best' not present")

txt1 = "The best things in life are free!"
print("expensive" not in txt1)