#!/usr/bin/env python 
import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msgs import Bool

global boo 
def callback(data):
	boo = data.data
	pub = rospy.Publisher('chatter', PoseStamped, queue_size = 10)
	rate = rospy.Rate(15)
        message=PoseStamped()

        pub.publish(message)
	rate.sleep()
	

def listener():
	rospy.init_node('sub', anonymous=True)
	rospy.Subscriber("button_state", Bool, callback)

	rospy.spin()


if __name__ == '__main__':
	listener()
