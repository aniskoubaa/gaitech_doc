
.. _network-configuration:

============================================
GAPTER: Network Configuration and Connection
============================================

In this tutorial, we present the different connection modes to Gapter using WiFi Hotspot (default configuration) or through a WiFi router to connect to Internet. 


.. NOTE::

   In this tutorial you will learn how to:

      * connect to Gapter using its default WiFi Hot Spot
      * configure Gapter to connect to Internet using WiFi router infrastructure
      * connect to Gapter through WiFi router
   
   For any query, please feel free to post your questions in the `Gaitech EDU Forum <http://forum.gaitech.hk/>`_


To provide flexibility to end-users, Gapter provides two possible network configuration modes:

* **WiFi Hotspot mode:** In this mode, the copter creates an adhoc network named ``gapternet`` that the user can connect to it through its compter or laptop using ``ssh``.
* **WiFi infrastructure mode:** in this mode, the copter connects to a WiFi router network that must be specified in advance. Users then can connect to the copter using ``ssh``.

.. NOTE::
    If you want to connect Gapter to Internet, then you must use the **infrastructure** mode. 
    If you want to have point-to-point communication with Gapter, then use the **WiFi Hotspot** mode. 



WiFi Hotspot Mode
=================
By default, Gapter comes with a WiFi hotspot. 
In this case, to connect to Gapter, you need to look for available WiFi networks, and connect to ``gapternet`` network.

.. WARNING::
    Remember that in this mode, there is no Internet connection.  

Once this is done, you just need to use ``ssh`` to connect to the drone as follow through a terminal.

.. code-block:: bash
   
   ssh gapter@10.0.0.1

Note that the default ip address of gapter is ``10.0.0.1``, and your laptop connects to that ``gapternet``, 
it will be assigned th IP address ``10.0.0.2``.
You will be request for a password. The password is ``gaitech``. 

Now you are connected to the copter and you can navigate inside the ubuntu file system, run ROS programs, etc. 

As mentioned before, this mode does not have Internet connection. So, you cannot do any operation that requires Internet. 
If you need Internet to download new packages or software inside Gapter, you need to configure the WiFi infrastructure mode as explained below. 

WiFi Infrastructure Mode
========================

To work in WiFi infrastructure mode, you first need to have a WiFi router to which the copter will connect. 

The connection to the WiFi network will use ``wpa_supplicant`` network configuration tool. 

STEP1. Specify the WiFi Network
_______________________________

First, connect to Gapter in hotspot mode, and in the terminal write:

.. code-block:: bash
   
   wpa_passphrase network-ssid network-password

.. WARNING::
   Change the name of the ssid and the password of the network, with your network credentials. 

You will get an output similar to

.. code-block:: bash
    
    network={
      ssid="ssid-name"
      #psk="password"
      psk=9b3dfa68a71033a672d01c961c03415ae47bfd8cadede26127be40aab43b5c75
   } 
   
Then, save this into a file called ``wpa_supplicant.conf`` as follows:

.. code-block:: bash
   
   sudo nano /boot/wpa_supplicant.conf 
   
The nano terminal command editor will open, and you need to edit or copy/paste the network information into that file. 

.. NOTE::
   We saved  ``wpa_supplicant.conf`` in the /boot/ directory so that you can edit this file from your laptop on the MicroSD card without having to login again to the copter and change the network configuration of the WiFi infrastructure network.
   To do so, just insert the MicroSD card into your laptop, edit the file by putting the information of the new network you want to connect to, and put the MicroSD card back to the copter. 
   In the next restart, the copter will automatically connect to the new WiFi network.
   
STEP2. Modify Network Interfaces
________________________________

Gapter was pre-configured to work in a WiFi hostpost. We need to change the interfaces defined in ``/etc/network/interfaces`` to enable the infastructure mode. 
When you are connected to Gapter in Hotspot mode, in the terminal edit the ``/etc/network/interfaces`` file as follow:

.. code-block:: bash
   
   sudo nano /etc/network/interfaces
   
You will the following configuration that corresponds to the default hotspot mode:

.. code-block:: bash
   
   #for loopback interface
   auto lo 
   iface lo inet loopback
   
   #for ethernet
   auto eth0 
   iface eth0 inet dhcp
    
   #for wifi in hotspot mode
   auto wlan0
   iface wlan0 inet static
   address 10.0.0.1
   netmask 255.255.255.0
   
To enable the WiFi infrastructure, we need to change the specification of ``wlan0`` as follow

.. code-block:: bash
   
   #for loopback interface
   auto lo 
   iface lo inet loopback
   
   #for ethernet
   auto eth0 
   iface eth0 inet dhcp
   
   #for wifi in hotspot mode
   allow-hotplug wlan0
   iface wlan0 inet dhcp
   wpa-conf /boot/wpa_supplicant.conf
   
   #default route
   iface default inet dhcp

With these changes, when you restart Gapter, it will automatically connect to the WiFi network defined in ``/boot/wpa_supplicant.conf``.
The IP address of the copter will be assigned automatically by the WiFi router, as DHCP is used.

It is possible to define a ``static`` or ``manual`` IP address, but DHCP dynamic IP address assignment is recommended.  
Now, your drone is connected to Internet and you can download any software or package from Internet. 
In addition, you can make your drone streams MAVLink data to a server on the Internet. 

.. NOTE::
   When WiFi instructure is configured, remember that you can easily modify the network to which you want to connect, by simply
   inserting the MicroSD card into your laptop and access the file ``/boot/wpa_supplicant.conf`` and modify network setting by editingt it.
   In the next restart, Gapter will automatically connect to the new network.
 

STEP3. Connect to Gapter
________________________

Once this is done, you can now connect to your Gapter drone.
First, you need to know what is the IP address assigned to your drone. If DHCP is enabled, then you can enter to the admin page of your router and try to identify which IP address was assigned by the router to your drone.
if this IP address is for example 192.168.100.13, then you can connect to the drone using ``ssh`` as follow through a terminal.

.. code-block:: bash
   
   ssh gapter@192.168.100.13
   
   .. WARNING::
   Make sure to use the correct IP address of the drone to connect to it. 
   

What do after connection to Gapter?
===================================

After connecting to Gapter, you can perform any terminal linux command on Odroid XU4 onboard computer, installing new software, working with ROS, developing programs, ...
It is recommended to use the ``nano`` editor to edit program on the terminal. 
You can find examples for developing programs for Gapter in :ref:`software-tutorials`.




 
