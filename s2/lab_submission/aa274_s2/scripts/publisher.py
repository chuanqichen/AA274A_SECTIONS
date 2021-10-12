#!/usr/bin/env python3

import rospy
from aa274_s2.msg import MyMessage
from datetime import datetime
import random

def publisher():
    pub = rospy.Publisher('my_topic', MyMessage, queue_size=10)
    rospy.init_node('my_node', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        my_message = MyMessage()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        my_message.data = "Hello World at : " + current_time
        my_message.x = random.random()
        my_message.y = random.random()
        my_message.z = random.random()
        my_message.status = True 
        pub.publish(my_message)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
 
