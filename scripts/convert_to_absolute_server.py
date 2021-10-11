#!/usr/bin/python3

from sensor_unification.srv import convert_to_absolute,convert_to_absoluteResponse
import rospy
import numpy as np
from scipy.spatial.transform import Rotation as R

def convert_to_absolute_function(sensor_position, sensor_orientation, relative_coordinates, degrees=False):
	rot_matrix = R.from_euler('ZXZ', sensor_orientation, degrees=degrees)
	absolute_coordinates = rot_matrix.apply(relative_coordinates) + sensor_position
	return (absolute_coordinates)

def handle_convert_to_absolute(req):
    absolute_coordinates = convert_to_absolute_function(req.sensor_position, req.sensor_orientation, req.relative_coordinates)
    print("Returning {}".format(absolute_coordinates))
    return (convert_to_absoluteResponse(absolute_coordinates))

def convert_to_absolute_server():
    rospy.init_node('convert_to_absolute_server')
    s = rospy.Service('convert_to_absolute', convert_to_absolute, handle_convert_to_absolute)
    print("Ready to convert to absolute.")
    rospy.spin()

if __name__ == "__main__":
    convert_to_absolute_server()
