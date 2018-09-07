
.. _ria-r100-demo-apps:

=================
Demo Applications
=================

Tele-op
-------

* This step will guide you to control RIA-R100 manually
* RIA-R100 can be controlled either using joystick comes with robot or using keyboard from host PC.
* To control RIA with joystick follow steps that has mentioned in quick start step
* To control RIA with keyboard from host PC follow these steps
* In a terminal.


.. code-block:: bash

	$ roslaunch ria_teleop keyboard.launch


Mapping & Navigation
--------------------

* This step will guide to create mapping for navigating RIA by exploring environment.
* Working environment : INDOOR
* In separate terminal launch following files in host PC
* To create map

.. code-block:: bash

	$ roslaunch ria_navigation slam_gmapping.launch

**Note:** Can use either gmapping or hector slam

To view robot and mapping

.. code-block:: bash
	
	$ roslaunch ria_description description_complete.launch

.. code-block:: bash

	$ roslaunch ria_description view.launch


To Navigate robot

.. code-block:: bash

	$ roslaunch ria_navigation move_base.launch


Manipulation
------------


This page will be updated soon


GPU Based applications
----------------------

This page will be updated soon
