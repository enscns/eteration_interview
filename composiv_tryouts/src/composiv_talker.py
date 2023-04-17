#!/usr/bin/env python3

import rospy                        # This is the python library in ROS environment
from std_msgs.msg import String     # This is the type of message

def talker():

    # this line declares that the node publishing to chatter topic using the 
    # message type String which is actually the class std_msgs.msg.String.
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # this line declares that the node name is 'talker'
    rospy.init_node('talker', anonymous=True)

    rate = rospy.Rate(1) # 1hz

    #This while loop tells that these messages will be transmitted in a certain 
    #loop continuously, unless there is an external shutdown command.
    while not rospy.is_shutdown():
        hello_str = " hello world "
        rospy.loginfo(rospy.get_caller_id() + hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass