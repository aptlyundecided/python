"""Sensor Factory"""

class Sensor(object):
    """Create a type of sensor simulator"""

    # Create based on class name:
    def factory(sensor_type):
        """Create a specific sensor type"""
        if sensor_type == 'rh':
            return RHSensor()
        else:
            print('not a sensor type')
    factory = staticmethod(factory)



class RHSensor():
    """Create an RH Sensor"""
    def __init__(self):
        """AUTO-MAGIX"""
        print("Relative Humidity Sensor Created.")
        self.current_value = 0
        self.name = ''
        self.location = ''
        self.rh_range = [0, 99]
        self.sample_rate = 0


    # [!] Internal Mutations [!]
    def set_base_params(self, args):
        """Accept a list of params for... """
        self.set_name(args[0])
        self.set_location(args[1])
        self.set_rh_range(args[2])
        self.set_sample_rate(args[3])

    def set_name(self, name):
        """Set the name of this sensor"""
        self.name = name

    def set_location(self, location):
        """Set the location of this sensor"""
        self.location = location

    def set_rh_range(self, rh_range):
        """Set the rh_range of this sensor"""
        self.rh_range = rh_range

    def set_sample_rate(self, sample_rate):
        """Set the sample rate of this sensor"""
        self.sample_rate = sample_rate




# [!] Tests & Test Mocks [!]
def make_params():
    """Make parameters for test sensor"""
    return  [
        'h1b',
        'hallway 1b',
        [55, 70],
        1000
    ]

# Check initialized values
def test_check_init():
    """tests for Sensor.__init__"""
    rh1 = Sensor.factory('rh')
    assert rh1.current_value == 0
    assert rh1.name == ''
    assert rh1.location == ''
    assert rh1.rh_range == [0, 99]
    assert rh1.sample_rate == 0

# Create several sensors in an array. 
def test_check_several():
    """make 5 sensors"""
    sensors = []
    for x in range(0, 5):
        sensors.append(Sensor.factory('rh'))

    print(sensors)
    assert len(sensors) == 5

    # Change name of sensor 3
    sensors[2].set_name('h1c')
    assert sensors[2].name == 'h1c'
    assert sensors[4].name == ''
