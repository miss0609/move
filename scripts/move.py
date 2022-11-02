#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    # 1 初始化节点
    rospy.init_node("control")
    # 2 创建发布者对象
    pub = rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=1000)
    # 3 循环发布运动控制消息
    rate = rospy.Rate(2)
    # 定义话题发布的消息
    msg = Twist()
    msg.linear.x =  0.1
    msg.linear.y =  0
    msg.linear.z =  0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0
    rospy.loginfo("haha")
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()