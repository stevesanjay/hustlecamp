# Multiple Inheritance:

class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    def method_c(self):
        print("Method C")

c = C()
c.method_a()  # Output: Method A
c.method_b()  # Output: Method B
c.method_c()  # Output: Method C