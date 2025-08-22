x = "rama"

def myFun():
    global y 
    y = "sita"
    print("function call ", x , y)

myFun()
print(x + y)
print(x, y)
