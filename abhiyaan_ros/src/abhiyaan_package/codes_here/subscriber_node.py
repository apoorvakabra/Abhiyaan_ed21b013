#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(data)

def listener():
    rospy.init_node("listener_node",anonymous=True)
    rospy.loginfo("listener node has started")
    rospy.Subscriber("/team_abhiyaan",String, callback) 

    rospy.spin()
    
if __name__=='__main__':
    listener()


