#!/usr/bin/env python3

import rospy                        # This is the python library in ROS environment
from std_msgs.msg import String     # This is the type of message


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard you, your message is %s ", data.data) 
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    # this line declares that the node name is 'listener'.
    rospy.init_node('listener', anonymous=True)   

    # this line declares that the node subscribing to chatter topic and if the 
    # std_msgs.msg.String type messages is received the callback functions are invoked.
    rospy.Subscriber("chatter", String, callback) 

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()