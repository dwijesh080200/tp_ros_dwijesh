#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import PoseStamped
import math
from Tkinter import *
from std_msgs.msg import Bool
import time

def callback(data):
		pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
		rate = rospy.Rate(15) # 15hz
		message = PoseStamped()
		message.pose.position.x = 22
		print(message)
		#while not rospy.is_shutdown():

		message.header.frame_id = "map"
		r = 10	
		theta = 0

		if(data.data == True):
			while theta < 2*(math.pi):
				message.pose.position.x = theta
				message.pose.position.y = math.sin(theta)
				print(message)
				#rospy.loginfo(hello_str)
				pub.publish(message)
				rate.sleep()
				theta = theta + 0.1

			while theta >=0:
				message.pose.position.x = theta
				message.pose.position.y = math.sin(-theta)
				print(message)
				#rospy.loginfo(hello_str)
				pub.publish(message)
				rate.sleep()
				theta = theta - 0.1
				print(message)

def listener():
	rospy.init_node('listen', anonymous=True)
	rospy.Subscriber("button_state", Bool, callback)

	rospy.spin()


if __name__ == '__main__':
	listener()


         

