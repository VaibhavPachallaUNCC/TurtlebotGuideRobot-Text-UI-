#!/usr/bin/env python
#Facing right
#orientation: { x: 0, y: 0, z: -0.755628311914, w: 0.655000652087 }

#Facing Left
#orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }

import os
import signal
places = ["Stair_A", "Elevators", "230", "230A", "230B", "231", "230C", "230D", "230E", "233", "222A", "202", "205A", "205B", "203", "204", "205C", "205D", "205E", "206", "207", "209", "210A", "210B", "211", "210C", "212", "210D", "210E", "200", "210F"]
valid = False
print "Where do you want to go?"
print places
dest = raw_input("> ")
for x in range(0, len(places)):
    if(dest == places[x]):
        valid = True
        #print "here"
while not (valid):
    print "Not valid location. Here are some valid locations:"
    print places
    print "Where do you want to go?"
    dest = raw_input("> ")
    for x in range(0, len(places)):
        if(dest == places[x]):
            #print "here"
            valid = True


if(dest == "Stair_A"):
        os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x: -2.14104175568, y: -28.9750289917, z: 0.0}, orientation: { x: 0, y: 0, z: 0.992481447445 , w: 0.122395165256 }}}'")
        

elif(dest == "230"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x: -1.52864086628, y: -29.9810161591, z: 0.0}, orientation: { x: 0, y: 0, z: -0.755628311914, w: 0.655000652087 }}}'")

elif(dest == "230A"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  -0.00490385014564, y: -30.339471817, z: 0.0}, orientation: { x: 0, y: 0, z: -0.755628311914, w: 0.655000652087 }}}'")

elif(dest == "230B"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  4.8593416214, y: -31.4331645966, z: 0.0}, orientation: { x: 0, y: 0, z: -0.755628311914, w: 0.655000652087 }}}'")
elif(dest == "231"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  4.8593416214, y: -30.5877723694, z: 0.0}, orientation: orientation: { x: 0, y: 0, z: 0.506483051702, w: 0.862249916404 }}}'")

elif(dest == "230C"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  7.83899593353, y: -31.8724327087, z: 0.0}, orientation: { x: 0, y: 0, z: -0.755628311914, w: 0.655000652087 }}}'")

elif(dest == "230D"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  9.21303462982, y: -32.1913032532, z: 0.0}, orientation: { x: 0, y: 0, z: -0.755628311914, w: 0.655000652087 }}}'")

elif(dest == "230E"):

    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  12.4356126785, y: -32.0772399902, z: 0.0}, orientation: { x: 0, y: 0, z: -0.755628311914, w: 0.655000652087 }}}'")

elif(dest == "233"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  12.565117836, y: -1.01156795025, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "222A"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  17.3230266571, y: -33.6913375854, z: 0.0}, orientation: {w:-.5}}}'")

elif(dest == "202"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  1.44326853752, y: -14.4686803818, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "205A"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  4.67893028259, y: -14.8104114532, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "205B"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  6.00613451004, y: -14.944065094, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "203"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  -0.306576251984, y: -1.01156795025, z: 0.0}, orientation: { x: 0, y: 0, z: -0.755628311914, w: 0.655000652087 }}}'")

elif(dest == "204"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  9.13915920258, y: -15.9403181076, z: 0.0}, orientation: { x: 0, y: 0, z: -0.755628311914, w: 0.655000652087 }}}'")

elif(dest == "205C"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  10.9818210602 , y: -15.5070743561, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "205D"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  12.3680973053 , y: -15.784201622, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "205E"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  15.6900596619, y: -16.1523189545, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "206"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  15.5906152725, y: -16.8610534668, z: 0.0}, orientation: { x: 0, y: 0, z: -0.755628311914, w: 0.655000652087 }}}'")

elif(dest == "207"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  20.8036746979, y: -16.8119411469, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "209"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  28.72631073, y: -18.1791572571, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "210A"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  33.6867637634, y: -18.8201980591, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "210B"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  36.8621864319, y: -19.3344249725, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "211"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  38.0199546814, y: -20.1322307587, z: 0.0}, orientation: { x: 0, y: 0, z: -0.755628311914, w: 0.655000652087 }}}'")

elif(dest == "210C"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  38.022769928, y: -19.3602561951, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "212"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  42.8537025452, y: -20.6985740662, z: 0.0}, orientation: { x: 0, y: 0, z: -0.755628311914, w: 0.655000652087 }}}'")

elif(dest == "210D"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  42.9759216309, y: -19.8840675354, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "210E"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  46.1004943848, y: -20.5957279205, z: 0.0}, orientation: { x: 0, y: 0, z: 0.506483051702 , w: 0.862249916404 }}}'")

elif(dest == "200"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x:  -1.2998970747, y: -26.8470535278, z: 0.0}, orientation: { x: 0, y: 0, z: 0.992481447445 , w: 0.122395165256 }}}'")

elif(dest == "210E"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x: 43.7105903625, y: -20.1204338074, z: 0.0}, orientation: { x: 0, y: 0, z: 0.660581051071 , w: 0.750754736892 }}}'")

#Need to fix
elif(dest == "Elevators"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x: 18.2642726898, y: -25.2108058929, z: 0.0}, orientation: { x: 0, y: 0, z: 0.992481447445 , w: 0.122395165256 }}}'")

elif(dest == "Women's Restroom"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x: 26.0277500153, y: -25.2108058929, z: 0.0}, orientation: { x: 0, y: 0, z: -0.0990895125443, w: 0.995078523788 }}}'")

elif(dest == "Men's Restroom"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x: 26.5333633423, y: -23.3122615814, z: 0.0}, orientation: { x: 0, y: 0, z: -0.0990895125443, w: 0.995078523788 }}}'")

elif(dest == "210G"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x: 46.9892692566, y: -20.6461830139, z: 0.0}, orientation: { x: 0, y: 0, z: 0.669996914731 , w: 0.742363882642 }}}'")


elif(dest == "210F"):
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: map}, pose: {position: {x: 46.6593284607, y: -20.5947780609, z: 0.0}, orientation: { x: 0, y: 0, z: 0.663196672097 , w: 0.748445171084 }}}'")

