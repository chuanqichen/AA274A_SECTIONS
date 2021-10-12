#!/usr/bin/env python3 
import rospy
from geometry_msgs.msg import Twist


def publisher():
    pub = rospy.Publisher('Twist', Twist, queue_size=10)
    rospy.init_node("Twist_Command_Node", anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
         twist_message = Twist()
         twist_message.linear.x = 1.0
         twist_message.linear.y = 1.1
         twist_message.linear.z = 1.2
         twist_message.angular.x = 0.1
         twist_message.angular.y = 0.2
         twist_message.angular.z = 0.3
         pub.publish(twist_message)
         rate.sleep() 


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
