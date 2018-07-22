
.. _ria-r100-simulation:

==============
Simulating RIA
==============

* RIA can be used in simulated environments regardless of real robot
* This step will guide to how to use RIA simulator
* Simulator package is included in RIA meta package that has been setup at installation step
* Run following in each terminal
* To start simulation:

.. code-block:: bash

	$ roslaunch ria_sim gazebo.launch

This will launch RIA’s simulation world. By default it is empty world. Can add different worlds by adding argument

.. code-block:: bash

	$ roslaunch ria_sim gazebo.launch world_name:=/worlds/willogarage.world


* To control manually

.. code-block:: bash

	$ roslaunch ria_sim keyboard.launch


* To generate map

.. code-block:: bash

	$ roslaunch ria_sim slam_gmapping.launch

* To navigate robot

.. code-block:: bash

	$  roslaunch ria_sim move_base.launch

* To visualize robot in rviz

.. code-block:: bash

	$ roslaunch ria_sim view.launch
