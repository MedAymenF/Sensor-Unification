#!/usr/bin/python3

import sys
import rospy
from sensor_unification.srv import *

def convert_to_absolute_client(sensor_position, sensor_orientation, relative_coordinates):
    rospy.wait_for_service('convert_to_absolute')
    try:
        convert_to_absolute_proxy = rospy.ServiceProxy('convert_to_absolute', convert_to_absolute)
        resp1 = convert_to_absolute_proxy(sensor_position, sensor_orientation, relative_coordinates)
        return resp1.absolute_coordinates
    except rospy.ServiceException as e:
        print("Service call failed: {}".format(e))

def usage(argv):
    return("{} sensor_position sensor_orientation relative_coordinates]".format(argv[0]))

if __name__ == "__main__":
    if len(sys.argv) == 4:
        sensor_position = [float(item) for item in sys.argv[1].split()]
        sensor_orientation = [float(item) for item in sys.argv[2].split()]
        relative_coordinates = [float(item) for item in sys.argv[3].split()]
    else:
        print(usage(sys.argv))
        sys.exit(1)
    '''print "Requesting %s+%s"%(x, y)
    print "%s + %s = %s"%(x, y, add_two_ints_client(x, y))'''
    print(convert_to_absolute_client(sensor_position, sensor_orientation, relative_coordinates))
