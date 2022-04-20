#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node("rev_sub_node",anonymous=True)
rospy.loginfo("node has started")

def rev(d):
    words= d.split(" ")
    nword = [i[::-1] for i in words]
    rev_d = " ".join(nword)
    return rev_d

def callback(msg):
    doubled= String()
    doubled.data= msg.data
    doubled.data= rev(doubled.data)
    #print(doubled)
    pub.publish(doubled)
    

pub=rospy.Publisher('naayihba_maet',String,queue_size=10)
sub= rospy.Subscriber("/team_abhiyaan",String, callback)
 
rospy.spin()


   