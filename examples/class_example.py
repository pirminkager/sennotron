
class Example(object):  # use superclass 'object' for new style (python3) classes

    CONSTANT = "This is a static variable"  # access it by using Example.CONSTANT

    def __init__(self, const_param):
        """
        This is the constructor. It is used to create an object (instance) out of the class
        The parameter "self" points to the object
        The constructor doesn't have a return value
        The constructor can have parameters. To store parameters in the object, directly assign them
        to the 'self' (this) object (see const_param)
        """
        self.variable = 2
        self.const_param = const_param

    def do_an_operation(self, param):
        """
        This is a method. Do whatever you want here. You can again use self to access the object
        :return:
        """
        self.another_variable = 3  # an IDE might give you a warning here because the variable has not been set in the constructor

        self.variable += self.another_variable

        self.param = param


# until here we just wrote the class, now we are going to use the class and create objects out of it:
example_object = Example("this is a constructor parameter")

# now we do an operation on the object
example_object.do_an_operation("with a method parameter")


