# method overriding
class Base_class(object):
    def base_class_function(self):
        print "hello base class function"


class Derived_class(Base_class):
    def derived_class_function(self):
        print "it is a deribved class function"

    def base_class_function(self):
        print "this is base class function but in derived class "
        print "thsi is method overriding"
        super(Derived_class, self).base_class_function()


derived_class_obj = Derived_class()
derived_class_obj.derived_class_function()
derived_class_obj.base_class_function()


# method hiding

class Base_class1:
    def base_class_function1(self):
        print "hello base class function method hiding is not taking place"


class Derived_class1(Base_class1):
    def base_class_function1(self, a):
        print 'the value of a :', a
        print "this is base class function but in derived class "


derived_class_obj1 = Derived_class1()
derived_class_obj1.base_class_function1(3)
