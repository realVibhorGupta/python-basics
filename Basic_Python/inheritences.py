# multi level inheritence
class base:
    def hello_base_function(self):
        print "hello  base class function"


# noinspection PyMethodMayBeStatic
class first_derived(base):
    def hello_first_derived_function(self):
        print "hello first derived class function"


class second_derived(first_derived):
    def second_derived_function(self):
        print "this is multi level inheritence"
        print "hello second derived class function"


multlevel_inheritence = second_derived()

multlevel_inheritence.hello_base_function()
multlevel_inheritence.hello_first_derived_function()
multlevel_inheritence.second_derived_function()


# hierarchical inheritence


class base:
    def hello_base_function(self):
        print "hello  base class function"


class first_derived(base):
    def hello_first_derived_function(self):
        print "hello first derived class function"


class second_derived(base):
    def second_derived_function(self):
        print "hello second derived class function"


class first_derived_derived(first_derived):
    def first_derived_derived_function(self):
        print "this is hierarchical inheritence"
        print "it is the derived function of the  first derived class"


first_derived_class_object = first_derived()
first_derived_class_object.hello_first_derived_function()
first_derived_class_object.hello_base_function()

second_derived_class_object = second_derived()
second_derived_class_object.hello_base_function()
second_derived_class_object.second_derived_function()

first_derived_class_object_from_derived = first_derived_derived()
first_derived_class_object_from_derived.hello_first_derived_function()
first_derived_class_object_from_derived.first_derived_derived_function()
first_derived_class_object_from_derived.hello_base_function()


# MULTIPLE  INHERITENCE

class base1:
    def hello_base1_function(self):
        print "hello  this is forst base class function"


# noinspection PyMethodMayBeStatic
class base2(base1):
    def hello_base2_function(self):
        print "hello second base  class function"


# noinspection PyMethodMayBeStatic
class first_derived_multiple(base1, base2):
    def first_derived_function(self):
        print "this ia multiple inheritence"
        print "hello first derived class function"


multiple_inheritence = first_derived_multiple()
multiple_inheritence.first_derived_function()
multiple_inheritence.hello_base2_function()
multiple_inheritence.hello_base1_function()


# hybrid is the mixture of two or more types of inhertences
