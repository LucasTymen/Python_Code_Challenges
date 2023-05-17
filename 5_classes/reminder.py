"""
Python Code Challenges Involving Classes

This article will help you review Python classes by providing some interesting code challenges.

Some of these challenges are difficult! Take some time to think about them before starting to code.

You might not get the solution correct on your first try — look at your output, try to find where you’re going wrong, and iterate on your solution.

Finally, if you get stuck, use our solution code! If you “Check Answer” twice with an incorrect solution, you should see an option to get our solution code.
However, truly investigate that solution — experiment and play with the solution code until you have a good grasp of how it is working.
Good luck!

Class Syntax

As a refresher, class syntax looks like this:
"""
class MyClass:
    # ... class variables ...

    def __init__(self):
        # ... instance variables ...

        """
For example, a class which defines a rectangle using a class variable, instance variables, and a method looks like this:
"""
class Rectangle:
    sides = 4

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


rectangle_1 = Rectangle(5, 10)
rect_area = rectangle_1.calculate_area()

"""
The last two lines in the above example show how to initialize an object of the class as well as calling one of the methods.
"""
