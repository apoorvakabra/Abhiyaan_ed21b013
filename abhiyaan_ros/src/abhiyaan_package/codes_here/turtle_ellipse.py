#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
#import sys

'''
rosrun turtlesim turtlesim_node
rosservice call /kill "turtle1"
rosservice call /spawn 5.5 3 0 "turtle1"
rosservice call /spawn 5.5 8 3.1414 "turtle2"
'''

radius = 0

def cb1(pose1:Pose):
    X = pose1.x - 5.5
    Y = pose1.y - 4.5
    
    
    vel1 = Twist()
    
    if X == 0 and Y < 0:
        vel1.linear.x = radius
        vel1.linear.y = 0
        vel1.linear.z = 0
        vel1.angular.x = 0
        vel1.angular.y = 0
        vel1.angular.z = 0

    elif X==0 and Y>0:
        vel1.linear.x = -radius
        vel1.linear.y = 0
        vel1.linear.z = 0
        vel1.angular.x = 0
        vel1.angular.y = 0
        vel1.angular.z = 0
    else:
        tan1 = Y/X
        if tan1 == 0 and X>0:
            vel1.linear.x=  0
            vel1.linear.y = 3.73205080757 * radius
            vel1.linear.z = 0
            vel1.angular.x = 0
            vel1.angular.y = 0
            vel1.angular.z = 0
        elif tan1==0 and X<0:
            vel1.linear.x=  0
            vel1.linear.y = -0.26794919243*radius
            vel1.linear.z = 0
            vel1.angular.x = 0
            vel1.angular.y = 0
            vel1.angular.z = 0
        else:
            if X>0 and Y>0:

                vel1.linear.x=  -radius
                vel1.linear.y = -0.5*(vel1.linear.x) / tan1
                vel1.linear.z = 0
                vel1.angular.x = 0
                vel1.angular.y = 0
                vel1.angular.z = 0
            elif X>0 and Y<0:
                vel1.linear.x=  radius
                vel1.linear.y = -0.5*(vel1.linear.x) / tan1
                vel1.linear.z = 0
                vel1.angular.x = 0
                vel1.angular.y = 0
                vel1.angular.z = 0
            elif X<0 and Y>0:
                vel1.linear.x=  -radius
                vel1.linear.y = -0.5*(vel1.linear.x) / tan1
                vel1.linear.z = 0
                vel1.angular.x = 0
                vel1.angular.y = 0
                vel1.angular.z = 0
            else:
                vel1.linear.x=  radius
                vel1.linear.y = -0.5*(vel1.linear.x) / tan1
                vel1.linear.z = 0
                vel1.angular.x = 0
                vel1.angular.y = 0
                vel1.angular.z = 0



    pub1.publish(vel1)

    
def cb2(pose2:Pose):
    X = pose2.x - 5.5
    Y = pose2.y - 6.5
   
    vel2 = Twist()
    if X == 0 and Y>0:
        vel2.linear.x = radius
        vel2.linear.y = 0
        vel2.linear.z = 0
        vel2.angular.x = 0
        vel2.angular.y = 0
        vel2.angular.z = 0
    elif X==0 and Y<0:
        vel2.linear.x = -radius
        vel2.linear.y = 0
        vel2.linear.z = 0
        vel2.angular.x = 0
        vel2.angular.y = 0
        vel2.angular.z = 0

    else:
        tan2 = Y/X
        if tan2 == 0 and X>0:
            vel2.linear.x= 0
            vel2.linear.y = -radius * 0.26794919243
            vel2.linear.z = 0
            vel2.angular.x = 0
            vel2.angular.y = 0
            vel2.angular.z = 0
        elif tan2 == 0 and X<0:
            vel2.linear.x= 0
            vel2.linear.y = 3.73205080757*radius
            vel2.linear.z = 0
            vel2.angular.x = 0
            vel2.angular.y = 0
            vel2.angular.z = 0
        else:
            if X>0 and Y>0:
                vel2.linear.x= radius
                vel2.linear.y = -0.5*(vel2.linear.x) / tan2
                vel2.linear.z = 0
                vel2.angular.x = 0
                vel2.angular.y = 0
                vel2.angular.z = 0

            elif X>0 and Y<0:
                vel2.linear.x= -radius
                vel2.linear.y = -0.5*(vel2.linear.x) / tan2
                vel2.linear.z = 0
                vel2.angular.x = 0
                vel2.angular.y = 0
                vel2.angular.z = 0
                
            elif X<0 and Y>0:
                vel2.linear.x= radius
                vel2.linear.y = -0.5*(vel2.linear.x) / tan2
                vel2.linear.z = 0
                vel2.angular.x = 0
                vel2.angular.y = 0
                vel2.angular.z = 0
                
            else:
                vel2.linear.x= -radius
                vel2.linear.y = -0.5*(vel2.linear.x) / tan2
                vel2.linear.z = 0
                vel2.angular.x = 0
                vel2.angular.y = 0
                vel2.angular.z = 0
                       
    pub2.publish(vel2)
           

# def turtle_circle(r):
#     global radius =   r
#     rospy.init_node("turtlesim",anonymous=True)
#     pub1=rospy.Publisher("/turtle1/cmd_vel",Twist, queue_size = 10)
#     pub2=rospy.Publisher("/turtle2/cmd_vel",Twist, queue_size = 10)
#     sub1 = rospy.Subscriber("/turtle1/pose",Pose,callback = cb1()  )
#     sub2 = rospy.Subscriber("/turtle2/pose",Pose,callback = cb2() )
#     rate= rospy.Rate(10)
    
    
#     rospy.loginfo("Radius = %f", radius)
       
    
#     rate.sleep()

if __name__=='__main__':
    
    r = 0.05
    # try:
    #     turtle_circle(float(sys.argv[1]))
    # except rospy.ROSInterruptException:
    #     pass
    radius = r
     
    rospy.init_node("turtlesim",anonymous=True)
    rospy.loginfo("node has started")
    pub1=rospy.Publisher("/turtle1/cmd_vel",Twist, queue_size = 10)
    pub2=rospy.Publisher("/turtle2/cmd_vel",Twist, queue_size = 10)
    sub1 = rospy.Subscriber("/turtle1/pose",Pose,callback= cb1  )
    sub2 = rospy.Subscriber("/turtle2/pose",Pose,callback= cb2 )
    rospy.spin()
    