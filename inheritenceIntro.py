# inheritence

class A:# superclass/ sub class
    def feature1(self):
        print('feature one')

    def feature2(self):
        print('feature 2')
        
class B(A): # child class of a/ sub class and inheting the feature from A
    def feature1(self):
        print('feature one')

    def feature2(self):
        print('feature 2')

class C(B): 
    def feature1(self):
        print('feature one')

    def feature2(self):
        print('feature 2')

        
a1 = A() # how u get the object

a1.feature1()
a1.feature2()

b1 = B()

c1 = C()
-------------------------------------------------------------------------------
