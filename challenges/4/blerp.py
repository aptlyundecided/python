"""RH Sensor Module."""

class Sensor(object):
    """Define the sensor module"""

    """
    args[0] == name, type = string
    args[1] == location, type = string
    args[2] == sample rate, type = integer (represents milliseconds)
    args[3] == rh_range, type = list [int, int] (first int must be smaller than second)
    args[4] == sensor_type, type = string, (Should be set to RH, or similar)
    """
    # def factory(args):
    #     """do a factory"""
    #     if args[5] == "RH": return RH_Sensor(args)
    #     factory = staticmethod(factory)

class RHSensor(Sensor):
    """Create a relative humidity sensor simulator"""
    # Sensor name
    name = ''

    #Sensor Location
    location = ''

    # Sample rate of the sensor
    sample_rate = 0

    # Range for simulated values
    rh_range = []

    # Amount of variance in simulation
    variance = 0


# Create params for sensor
PARAMS = [
    'test-sensor',
    'my-brain',
    1000,
    [55, 80],
    8
]



# class Shape(object):
#     # Create based on class name:
#     def factory(type):
#         #return eval(type + "()")
#         if type == "Circle": return Circle()
#         if type == "Square": return Square()
#         assert 0, "Bad shape creation: " + type
#     factory = staticmethod(factory)

# class Circle(Shape):
#     def draw(self): print("Circle.draw")
#     def erase(self): print("Circle.erase")

# class Square(Shape):
#     def draw(self): print("Square.draw")
#     def erase(self): print("Square.erase")

# # Generate shape name strings:
# def shapeNameGen(n):
#     types = Shape.__subclasses__()
#     for i in range(n):
#         yield random.choice(types).__name__

# shapes = \
#   [ Shape.factory(i) for i in shapeNameGen(7)]

# for shape in shapes:
#     shape.draw()
#     shape.erase()