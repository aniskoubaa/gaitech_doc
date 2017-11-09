
.. _gapter-mavlink-connect-with-ground-station:

=====================================================
GAPTER: Controlling Gapter from desktop using mavlink
=====================================================

Connect to wifi “gapter” from your desktop which will be shown in Wi-Fi list. If prompt for password type ``gapteredu``

* Open the terminal and connect to Gapter's computer by typing following

.. code-block:: bash

	user $: ssh gapter@192.168.1.1

If prompts for password, type ``gapteredu``

* Now in the same terminal type following

.. code-block:: bash

	odroid $: mavproxy.py --master=/dev/ttyUSB0 --baudrate 57600 --out 192.168.x.xx:5000  --aircraft MyCopter
	
You must enter your desktop's ip in place of  ``192.168.x.xx``

* You can notice heartbeat form Gapter which shows mavlink has been connected

* In order to fly Gapter you must keep Gapter in GUIDED MODE then giving command takeoff at desired altitude.

* We will test Gapter outdoor to fly at 3 meters height and make it land. 

* Type these lines in the same terminal

.. code-block:: bash

		MAV> load param /home/gapter/gapter_param/outdoor.param 
		MAV > mode GUIDED
		MAV> arm throttle
		MAV> takeoff 3

* Now you can notice Gapter hovering at 3 meters height. To land Gapter , mode should be changed to land mode

.. code-block:: bash

	MAV> mode LAND

* We have given arguments next to mavproxy.py where your ip address mentioned with port number. You can connect Gapter to your favorite mission planner by adding this port number at comm links of mission planner to UDP Link.

.. NOTE::
    To control Gapter indoor you must change parameters to indoor.
    ``MAV> load param /home/gapter/gapter_param/indoor.param``

    Then control follow rest of lines like outdoor control.


