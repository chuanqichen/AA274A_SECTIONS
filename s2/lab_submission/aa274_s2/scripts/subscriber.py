#!/usr/bin/env python3

import rospy
from aa274_s2.msg import MyMessage

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    rospy.loginfo(rospy.get_caller_id() + " x = %.3f", data.x)
    rospy.loginfo(rospy.get_caller_id() + " y = %.3f", data.y)
    rospy.loginfo(rospy.get_caller_id() + " z = %.3f", data.z)
    rospy.loginfo(rospy.get_caller_id() + " status = %r", data.status)

def subscriber():
    rospy.init_node('my_subscriber', anonymous=True)
    rospy.Subscriber("my_topic", MyMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
