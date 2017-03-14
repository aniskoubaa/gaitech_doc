.. _gapter-py-square-run-demos:

=======================
Square run - Python
=======================

This demo illustrate how to make Gapter moves on squares

First launch the simulation, see following links for further details: 

`erlerobotics.com`_

`coins-lab.org`_

.. _erlerobotics.com: http://docs.erlerobotics.com/simulation/vehicles/erle_copter/tutorial_1 

.. _coins-lab.org: http://wiki.coins-lab.org/index.php?title=Simulation_of_Erle_Copter

.. figure:: images/py_square_run_demo_fig_1.png
    :align: center
    :width: 400pt

    Figure 1: Launch the simulator

After launching the simulator, Take off the drone:

.. code-block:: bash

	# in the MAVProxy prompt:
	mode GUIDED
	arm throttle
	takeoff 2

.. figure:: images/py_square_run_demo_fig_2.png
    :align: center
    :width: 400pt

    Figure 2: Drone taking off

Then, in new terminal, launch the ROS node for square run:

.. code-block:: bash

	rosrun gapter_py square_run.py 

.. figure:: images/py_square_run_demo_fig_3.png
    :align: center
    :width: 400pt

    Figure 3: Drone square run

.. figure:: images/py_square_run_demo_fig_4.png
    :align: center
    :width: 400pt

    Figure 4: Drone square run


Code explaination
-----------------

.. code-block:: python

 import rospy
 from std_msgs.msg import String
 from geometry_msgs.msg import TwistStamped

 if __name__ == '__main__':
    rospy.init_node('moving', anonymous=True)
    square_pub = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel', TwistStamped, queue_size=10)
    square = TwistStamped()
    
    try:
        while not rospy.is_shutdown():
            
            square.twist.linear.x=0.5
            square.twist.linear.y=0
            square_pub.publish(square)
            rospy.sleep(5)

            square.twist.linear.x=0;
            square.twist.linear.y=0;
            square_pub.publish(square);
            rospy.sleep(2);
            
            square.twist.linear.x=0;
            square.twist.linear.y=0.5;
            square_pub.publish(square);
            rospy.sleep(5);
            
            square.twist.linear.x=0;
            square.twist.linear.y=0;
            square_pub.publish(square);
            rospy.sleep(2);
            
            square.twist.linear.x=-0.5;
            square.twist.linear.y=0;
            square_pub.publish(square);
            rospy.sleep(5);
            
            square.twist.linear.x=0;
            square.twist.linear.y=0;
            square_pub.publish(square);
            rospy.sleep(2);
            
            square.twist.linear.x=0;
            square.twist.linear.y=-0.5;
            square_pub.publish(square);
            rospy.sleep(5);
            
            square.twist.linear.x=0;
            square.twist.linear.y=0;
            square_pub.publish(square);
            rospy.sleep(2);

    except rospy.ROSInterruptException:
        pass

