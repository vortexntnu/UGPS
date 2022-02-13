#!/usr/bin/env python

# import debugpy
# print("Waiting for VSCode debugger...")
# debugpy.listen(5678)
# debugpy.wait_for_client()

from getposition import main

#ROS imports
import rospy
from geometry_msgs.msg import Point

class UGPSNode:
    
    def __init__(self):
        ########################################
        ####Things you can change yourself####
        ########################################

        #Name of the node
        node_name = "ugps_position"

        #Subscribe topic
        position_topic = "/ugps/position"

        # ROS node init
        rospy.init_node(node_name)

        # Publisher to autonomous
        self.position_pub = rospy.Publisher(position_topic, Point, queue_size=1)

    def ugps_callback(self):
        position = main()

        p = Point()
        p.x = float(position['X'])
        p.y = float(position['Y'])
        p.z = float(position['Z'])

        self.position_pub.publish(p)

if __name__ == '__main__':
    while not rospy.is_shutdown():     
        try:
            ugps = UGPSNode()
            rospy.spin()
        except rospy.ROSInterruptException:
            pass