
.. _ria-r100-internal-components:

===============================
Internal Components and Details
===============================


.. figure:: images/ria_r100_internal_fig01.png
    :align: center

    Fig 1.Internal view of RIA-R100

Internal Pc
-----------

RIA-R100 Is integrated with Intel i5 Z370 chipset over Gigabyte Mini ITX board. It can be replaced with any kind of processors based on chipset preference. 

Following are complete set of specifications related to Internal PC:

Processor: Intel® Core™ i5-8400 Processor, 9M Cache, up to 4.00 GHz
RAM: 8Gb 
Memory: 120 Gb SSD
Mother Board: Gigabyte Z370N WIFI

* USB3.0 = 4 (one used by Joystick)
* HDMI =1 Using HDMI 2.0 interface
* Dual Channel DDR4, Two Memory Slots – (8GB Fixed at one slot)
* Supports Intel ® OptaneTM Technology
* Supports graphics card slot transfer 2x8 mode expansion card
* Intel ® USB 3.1 Gen1 Type-CTM Interface
* Realtek flagship audio chip supporting smart power amplifier technology
* Intel ® wireless card that supports high-speed 802.11ac 5G WIFI and Bluetooth 4.2
* Dual Intel® Gigabit High Speed ​​Network Card + cFos Network Management Software
* Network Interface Upgrade Strengthens Anti-Static and Anti-Surge Functions
* Two high-speed NVMe M.2 SSD slot designs using PCI-E 3.0 x4 high-speed channels (supports PCI-E channel and SATA channel M.2 SSD)
* Gigabyte Smart Fan Technology with Smart Fan Shutdown
* Using graphics slot alloy armor
* Mainboard components upgrade anti-vulcanization technology			


.. image:: images/ria_r100_internal_fig02.png
    :align: center


.. figure:: images/ria_r100_internal_fig03.png
    :align: center

    Fig 2. Internal PC

Power Ports
-----------
	
RIA-R100 is embedded with three power ports with different ratings 24V, 12V and 5V fused with 5A each. Two power slots 12V and 5V has been fixed at sensor deck which are quite sufficient for powering up sensors like LIDAR, RGBD and others. One power slot 24V is fixed at control panel. It is quite suitable for integrating manipulators and other hardware devices. If necessary this power slot can be fused up to 30A. 
	

There are other power converters which are embedded for PC and Router

Wi-Fi router
------------

.. figure:: images/ria_r100_internal_fig04.png
    :align: center

    Fig 3. Wi-Fi Router

Wi-Fi router with 4 LAN ports and 1 WAN port is fixed inside robot where one LAN port is connected to robot’s wan slot and one connected to LAN extension port where it will be available at sensor deck to have direct access to PC which some sensors need to communicate via LAN. Since there are two WAN ports available in PC one of WAN port is extended to rear control panel allowing user to access internet for updating or downloading packages. 


Fuses 
-----

RIA-R100 is completely fused with 100A from main battery connection and each component inside robot used are fused at their required currents. All fuses can be accessed underside of control panel where one 100A and one 60A main fuses are connected for overall robot and motor controller. There will be a small fuse box with multiple fuses rating from 5A to 30A. These were connected to several components mostly with 5A. Once current is overloaded at 100A and 60A power flow will be disconnected and can reconnected by sliding the lock. If current overloaded with 5A slots they have to be replaced. 

Motor controller
----------------
	
RIA-R100 base has been embedded by a differential drive motor controller with two motors left and right attached to it with no additional power module for motors. It is also capable to read encoders from each motor and thus control speed of robot. Drivers and PID for these motor controllers has been developed at Gaitech Robotics and encoders has been set according to wheel size and speed of motor. So, don’t change these values. Power supplied to this motor controller has been fused at 60A to avoid damage.
