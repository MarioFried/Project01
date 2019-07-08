#
# Exemplo de uso de Classes e Metodos com Python
#
class MyClass():
    def method01(self):
        print ("method 1")

    def method02(self, SomeString):
        print ("method 2 " + SomeString)

class AnotherMyClass(MyClass):
    def method01(self):
        MyClass.method01(self)
        print ("Another Class - Method 1")

    def method02(self,SomeString):
        print ("Another Class - Method 2 " + SomeString)

def main():
    c1 = MyClass()
    c1.method01()
    c1.method02("Esta eh mais uma string")

    c2 = AnotherMyClass()
    c2.method01()
    c2.method02("OK Again")

if __name__ == "__main__":
    main()