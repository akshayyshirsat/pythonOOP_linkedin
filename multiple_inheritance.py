class A:
    def __init__(self):
        super().__init__();
        self.foo = "foo";
        self.name = "A";


class B:
    def __init__(self):
        super().__init__();
        self.bar = "bar";
        self.name = "B";


class C(A, B):
    def __init__(self):
        super().__init__();

    def showProps(self):
        print(self.foo);
        print(self.bar);
        print(self.name);


c = C();
c.showProps();
print(c.__class__.__mro__);  # Important step here, __class__ was used
