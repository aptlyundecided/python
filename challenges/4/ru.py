"""Factories!"""

class Sensor(object):
    """Sensor ... parent class??"""

    def factory(sensor_type):
        """Sensor factory chooses what type of sensor to create, param is a string."""

        if sensor_type == 'rh':
            return BaseSensor()
        else:
            print('[*] Sensor Module [*]: factory(\'type\') -> Sensor type does not exist.')
    factory = staticmethod(factory)


# Every sensor will have certain properties and methods.  These will live here.
class BaseSensor():
    """Create base sensor properties and methods"""

    def __init__(self):
        """Initiliaze name[string], location[string], and sample rate[int]."""
        self.name = ''
        self.location = ''
        self.sample_rate = 0

    def set_name(self, new_name):
        """set own sensor name"""
        self.name = new_name


# RH | Relative Humidity Sensor Class
class RHSensor():
    """Extend BaseSensor with current_value, last_100."""
    def __init__(self):
        self.current_value = 0.0
        self.last_100 = []

    def set_current_value(self, new_value):
        """Set RH value of self to new_value, if new_value is proper type."""


    def append_new_value(self, new_value):
        if type(new_value) == 'float':
            if len(self.last_100) > 99:
                self.insert(0, new_value)
        else:
            print('')
def test_parent_class():
    """Test the parent class"""
    test_sensor = Sensor.factory('rh')

    assert test_sensor.name == ''

print(type(0.0))
print(type(0))
