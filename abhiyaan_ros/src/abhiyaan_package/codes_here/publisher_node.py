#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__=='__main__':
    pub= rospy.Publisher("/team_abhiyaan",String,queue_size=10)
    rospy.init_node("pub_node",anonymous=True)
    rospy.loginfo("publisher node has started")

    rate=rospy.Rate(10)

    while not rospy.is_shutdown():
       # rospy.loginfo('Team Abhiyaan Rocks')
        pub.publish('Team Abhiyaan Rocks')
        rate.sleep()


    
