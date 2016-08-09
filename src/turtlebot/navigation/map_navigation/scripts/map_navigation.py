
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees


class map_navigation():
	
	# declare the coordinates of interest 
	

	goalReached = False

	def choose(self):

		choice='q'
		
		rospy.loginfo("|-------------------------------|")
		rospy.loginfo("|PRESSE A KEY:")
		rospy.loginfo("|'0': Cafe ")
		rospy.loginfo("|'1': Office 1 ")
		rospy.loginfo("|'2': Office 2 ")
		rospy.loginfo("|'3': Office 3 ")
		rospy.loginfo("|'q': Quit ")
		rospy.loginfo("|-------------------------------|")
		rospy.loginfo("|WHERE TO GO?")
		choice = eval(input())
		return choice

	def __init__(self): 
		self.xCafe = 15.50
		self.yCafe = 10.20
		self.xOffice1 = 27.70
		self.yOffice1 = 12.50
		self.xOffice2 = 30.44
		self.yOffice2 = 12.50
		self.xOffice3 = 35.20
		self.yOffice3 = 13.50
		# initiliaze
        	rospy.init_node('map_navigation', anonymous=False)
		choice = self.choose()
		rospy.loginfo(type(choice))
		
		if (choice == 0):

			rospy.loginfo(choice)
			self.goalReached = self.moveToGoal(self.xCafe, self.yCafe)
		
		elif (choice == 1):
			rospy.loginfo(choice)

			self.goalReached = self.moveToGoal(self.xOffice1, self.yOffice1)

		elif (choice == 2):
			rospy.loginfo(choice)
			
			self.goalReached = self.moveToGoal(self.xOffice2, self.yOffice2)
		
		elif (choice == 3):
			rospy.loginfo(choice)

			self.goalReached = self.moveToGoal(self.xOffice3, self.yOffice3)

		if (choice!='q'):

			if (self.goalReached):
				rospy.loginfo("Congratulations!")
				#rospy.spin()

				#sc.playWave(path_to_sounds+"ship_bell.wav");
				
				#rospy.spin()

			else:
				rospy.loginfo("Hard Luck!")
				#sc.playWave(path_to_sounds+"short_buzzer.wav");
		
		while choice != 'q':
			choice = self.choose()
			if (choice == '0'):

				goalReached = self.moveToGoal(xCafe, yCafe)
		
			elif (choice == '1'):

				goalReached = self.moveToGoal(xOffice1, yOffice1)

			elif (choice == '2'):
		
				goalReached = self.moveToGoal(xOffice2, yOffice2)
		
			elif (choice == '3'):

				goalReached = self.moveToGoal(xOffice3, yOffice3)

			if (choice!='q'):

				if (goalReached):
					rospy.loginfo("Congratulations!")
					rospy.spin()

					#sc.playWave(path_to_sounds+"ship_bell.wav");

				else:
					rospy.loginfo("Hard Luck!")
					#sc.playWave(path_to_sounds+"short_buzzer.wav");


	def shutdown(self):
        # stop turtlebot
        	rospy.loginfo("Quit program")
        	rospy.sleep()

	def moveToGoal(self,xGoal,yGoal):

		#define a client for to send goal requests to the move_base server through a SimpleActionClient
		ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

		#wait for the action server to come up
		while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
			rospy.loginfo("Waiting for the move_base action server to come up")
		

		goal = MoveBaseGoal

		#set up the frame parameters
		goal.target_pose.header.frame_id = "map"
		goal.target_pose.header.stamp = rospy.Time.now()

		# moving towards the goal*/

		goal.target_pose.pose.position =  Point(self.xGoal,self.yGoal,0)
		goal.target_pose.pose.orientation.x = 0.0
		goal.target_pose.pose.orientation.y = 0.0
		goal.target_pose.pose.orientation.z = 0.0
		goal.target_pose.pose.orientation.w = 1.0

		rospy.loginfo("Sending goal location ...")
		ac.sendGoal(goal)

		ac.wait_for_result()

		if(ac.get_result() != None):
			rospy.loginfo("You have reached the destination")
			return True
	
		else:
			rospy.loginfo("The robot failed to reach the destination")
			return False

if __name__ == '__main__':
    try:
	
	rospy.loginfo("You have reached the destination")
        map_navigation()
        rospy.spin()
    except:
        rospy.loginfo("map_navigation node terminated.")
