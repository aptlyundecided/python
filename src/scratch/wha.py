"""Does a docstring require 3 quotes"""
# What is a factory anyway?

class Shape(object):
    """Let's make a shape."""
    def factory(type):
        """Check the type, do the correct shape."""

        #declar stuff
        yarn = 'YARN.'


        # check the type.
        if type == 'triangle':
            return Triangle()
        if type == 'KrispyKreme':
            return BuildShape()
        # if type == 'square': return Square()
        # if type == 'circle': return Circle()
        assert 0, "Bad shape creation:" + type
    factory = staticmethod(factory)

class Triangle():
    """I make a triangle."""
    def draw(self):
        """Draw a triangle."""
        print('Triangle.Draw')
    def erase(self):
        """Erase a triangle."""
        print('Triangle.Erase')

class BuildShape(type):
    """thing"""
    def draw(self):
        """draw the name of the shape."""
        print(dir(self))
        # print(name + '.Draw')
    def erase(self):
        """erase the shape."""
        print(self)
        # print(name + '.erase')

print(Shape.factory('KrispyKreme').draw())
