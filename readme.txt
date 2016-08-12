                                                TurtlebotGuideRobot-Text-UI-
                                                    By: Vaibhav Pachalla 

Note: Application tested to run on Ubuntu 14.04 64x

    I have Turtlebot Guide Robot with text interface designed to be used to guide visitors to various computer
science offices in Woodward Hall at UNC Charlotte. I have used the Turtlebot robot platform to map an area
of Woodword Hall at UNC Charlotte. I then wrote a python program that could transmit destinations to the 
Turtlebot robot.
 

Prerequisites to run the program:

    1. Follow this tutorial to install the necessary software on the Turtlebot:               http://wiki.ros.org/turtlebot/Tutorials/indigo/Turtlebot%20Installation
    2. Follow this tutorial to install the necessary software on your PC:
    http://wiki.ros.org/turtlebot/Tutorials/indigo/PC%20Installation
    3. Network configuration between Turtlebot and PC:
    http://wiki.ros.org/turtlebot/Tutorials/indigo/Network%20Configuration
    4. Install turtlebot_navigation package on turtlebot computer:
    run the following command "sudo apt-get install ros-<your ros distro (eg. indigo, jade, kinetic, etc.)>-turtlebot-navigation

How to run this application:
1. Clone this git directory on to your Workstation and onto your Turtlebot computer
2. Bringup Turtlebot (http://wiki.ros.org/turtlebot_bringup/Tutorials/indigo/TurtleBot%20Bringup)
3. On the Turtlebot, run the follwing command "export TURTLEBOT_MAP_FILE=/path/to/TurtlebotGuideRobot-Text-UI-/Directory/mapV3.yaml"
4. On Turtlebot computer, run "roslaunch turtlebot_navigation amcl_demo.launch"
5. On your computer, run RVIZ:
Pre-Groovy
rosrun rviz rviz -d `rospack find turtlebot_navigation`/nav_rviz.vcg
Groovy or later
roslaunch turtlebot_rviz_launchers view_navigation.launch --screen
6. On RVIZ, set the 2D pose estimate:
When starting up, the TurtleBot does not know where it is. To provide it its approximate location on the map:
    Click the "2D Pose Estimate" button
    Click on the map where the TurtleBot approximately is and drag in the direction the TurtleBot is pointing. 
You will see a collection of arrows which are hypotheses of the position of the TurtleBot. The laser scan should line up approximately with the walls in the map. If things don't line up well you can repeat the procedure. 
(Snippet of text from this tutorial:http://wiki.ros.org/turtlebot_navigation/Tutorials/Autonomously%20navigate%20in%20a%20known%20map)
7. On your computer or the Turtlebot computer, run go.py. To make go.py an executable, run the following command:"chmod +rwx go.py".
8. Now run go.py: "./go.py"
9. Type a valid destination into the prompt, and then press ^C (control C) when the Turtlebot reaches its destination or
if the Turtlebot must be halted.

