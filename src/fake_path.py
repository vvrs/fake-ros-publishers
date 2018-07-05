#!/usr/bin/env python

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped

class publishFakePath:
		'''This requires odom data, if not available run fake_odom.py'''

	def __init__(self):

		rospy.Subscriber('/odom',Odometry,self.callback_odom)
		self.pathpub = rospy.Publisher('/test_path',Path,queue_size=10)
		
		self.path_msg = Path()


	def callback_odom(self,data):
		self.path_msg.header = data.header
		pose = PoseStamped()
		pose.header = data.header
		pose.pose = data.pose.pose
		self.path_msg.poses.append(pose)
		self.pathpub.publish(self.path_msg)


def main():
	rospy.init_node('fake_path')
	pfp = publishFakePath()

if __name__ == '__main__':
	main()