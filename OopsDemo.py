#classes are user defined  blueprint  or prototype
#sum , multipication , addition , constant
#method , class variable , instance variable , constructor etc.
#object for your classes
#inclass we can have only variable and method commonly used
#to decler mathod in class  have to follow the same syntax which we followed for function
#(Once we have mastered the internal behaviour of Python, we are now able to begin providing
# several constructors within our classes. That is, we will offer multiple methods to create
# objects in the same Python class.)
class calculator:
        num = 100
        def getdata(self):
            print("I am execution the OOps concepts and this method sytax")


object = calculator()
object.getdata()
print(object.num)


