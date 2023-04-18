# Eteration Case Report

In this document, there is a report prepared for the case given by the Eteration company. In the first part of the report, information about personal characteristics will be given, while in the second part, the method which is used for communication of two nodes in the ROS environment will be mentioned.

## Section 1 

The following has been scored on a scale of 1 to 5 as "how much of it I have or how much I can achieve."

•	Ability to read/write/think/understand in English  **(Score : 4)**

•	Ability to be physically present at the office when required (the consistency matters) **(Score : 5)**

•	Ability to get your way out in a Linux environment. **(Score : 4)**

•	Ability to understand a logical set of instructions (whether it is a tutorial or an article with academic foundations). **(Score : 4)**

•	Ability to ask questions without hesitation or any long/overdue personal over-thinking  **(Score : 4)**

•	Ability to work in a transparent manner (audacity to say 'this is not done' or 'i did not do it' instead of hiding and ghosting in a dark room) **(Score : 4)**

•	Having a development environment on top of a Linux distro, using an Ubuntu LTS: 18.04 or 20.04 (#general) **(Score : 5)**

•	Beginner/intermediate skills of scripting in Python (preferable) or C++ (#ros, #general). **(Score : 5)**

•	Ability to use command line interface (a terminal) in a *nix based environment (#general) **(Score : 4)**

•	Ability to contribute and to collaborate with others via Git (#general) **(Score : 3)**

•	Ability to read and debug a code segment (#general) **(Score : 4)**

•	Basic understanding of web and web technologies (#general) **(Score : 2)**

•	Basic understanding of robots and/or robotics (#ros) **(Score : 4)**

•	Having a basic understanding of communication in a distributed architecture (#ros). **(Score : 5)**

•	Having a basic understanding of how a pub-sub information flow works (#ros). **(Score : 5)**

•	Having a basic understanding of OOP (#general, #ros).**(Score : 3)**

## Section 2

In this section of the report, it will be explained how two nodes communicate with each other in the ROS environment. For this study, [wiki.ros.org](wiki.ros.org) site was used.

Nodes publish to topics in order to transmit information to other nodes. Likewise, they subscribe to topics in order to receive information from other nodes. Topics are a kind of channels that contain messages.

In this study, the following steps are applied for the communication of two nodes:

•	A ROS package named composiv_tryouts was created. 

•	The node 'talker' that will publish is created in the [composive_talker.py](https://github.com/enscns/eteration_interview/blob/feature/enes_cansu_16042023/composiv_tryouts/src/composiv_talker.py) file inside this package. This node publishes a message of type std_msgs.msg.String in a topic named 'chatter'. 

•	Then, a node named 'listener' was created in [composive_listener.py](https://github.com/enscns/eteration_interview/blob/feature/enes_cansu_16042023/composiv_tryouts/src/composiv_listener.py) and this node subscribed to the 'chatter' topic. The 'listener' node notifies users that it has subscribed to the 'chatter' topic with the 'callback' function. 

•	A launch file named [composive_tryouts.launch](https://github.com/enscns/eteration_interview/blob/feature/enes_cansu_16042023/composiv_tryouts/launch/composiv_tryouts.launch) has been created to run these two files together. When this file is run, the communication between the two nodes is provided through the 'chatter' topic.

Messages coming to the terminal screen when the launch file is run are shown in figure 1.

![WhatsApp Image 2023-04-18 at 01 45 36](https://user-images.githubusercontent.com/64541116/232639877-5e5aa510-48e4-42a7-991a-3a723f6f873c.jpeg)

Figure 1

With the help of ROS's rqt_graph tool, it can be seen whether nodes and topics are published in the ROS environment and whether they communicate with each other. Figure 2 shows the rqt_graph representation of the above study.

![image](https://user-images.githubusercontent.com/64541116/232639925-e9f6ba24-b0b7-413f-bd7c-7bd1288f8ef6.png)

Figure 2: rqt_graph representation



