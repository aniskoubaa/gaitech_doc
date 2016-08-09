
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees


class map_navigation():
	
	# declare the coordinates of interest 
	xCafe = 15.50
	yCafe = 10.20
	xOffice1 = 27.70
	yOffice1 = 12.50
	xOffice2 = 30.44
	yOffice2 = 12.50
	xOffice3 = 35.20
	yOffice3 = 13.50

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
		choice = input()
		return choice

	def __init__(self):

		# initiliaze
        	rospy.init_node('map_navigation', anonymous=False)
		
		choice = self.choose()
		if (choice == '0'):

			goalReached = moveToGoal(xCafe, yCafe)
		
		elif (choice == '1'):

			goalReached = moveToGoal(xOffice1, yOffice1)

		elif (choice == '2'):
		
			goalReached = moveToGoal(xOffice2, yOffice2)
		
		elif (choice == '3'):

			goalReached = moveToGoal(xOffice3, yOffice3)

		if (choice!='q'):

			if (goalReached):
				rospy.loginfo("Congratulations!")
				#rospy.spin()

				#sc.playWave(path_to_sounds+"ship_bell.wav");
				
				#rospy.spin()

			else:
				rospy.loginfo("Hard Luck!")
				#sc.playWave(path_to_sounds+"short_buzzer.wav");
			
		while True:
			choice = self.choose()
			if (choice == '0'):

				goalReached = moveToGoal(xCafe, yCafe)
		
			elif (choice == '1'):

				goalReached = moveToGoal(xOffice1, yOffice1)

			elif (choice == '2'):
		
				goalReached = moveToGoal(xOffice2, yOffice2)
		
			elif (choice == '3'):

				goalReached = moveToGoal(xOffice3, yOffice3)

			if (choice!='q'):

				if (goalReached):
					rospy.loginfo("Congratulations!")
					rospy.spin()

					#sc.playWave(path_to_sounds+"ship_bell.wav");

				else:
					rospy.loginfo("Hard Luck!")
					#sc.playWave(path_to_sounds+"short_buzzer.wav");

		return 0


	def moveToGoal(xGoal,yGoal):

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

		goal.target_pose.pose.position =  Point(xGoal,yGoal,0)
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
    except rospy.ROSInterruptException:
        rospy.loginfo("map_navigation node terminated.")
