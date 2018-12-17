print("Begin", __name__)
import proga

print("Define fB")
def fB():
    print("Dentro fB")
    proga.fA()

print("Chama fb")
fB()

print("End", __name__)
