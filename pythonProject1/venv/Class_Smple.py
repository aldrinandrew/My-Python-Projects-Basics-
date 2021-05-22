class MySampleClass:
    def Hello(self,n):
        self.name=n
        print("Hello",n)
    def print_name(self):
        print(self.name)

x=MySampleClass()
y=MySampleClass()
name1 = "Aldrin Andrew"
x.Hello(name1)
