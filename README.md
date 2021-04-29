# ros2_tasks

## Tasks
This repository consists of two tasks: 

- Task 1 : Create a ROS 2 project that uses publishers and subscribers to create service-like behavior for doubling a number.

- Task 2 : Send two numbers in your own custom message type and return the product as the answer.

Both tasks have been implemented in Python.

I have also written about my experience working with ROS2 [here](https://docs.google.com/document/d/1zQZfwXNsjbbSKEoRKHoLCIwhQXHF-vVJWha1dMV28Hs/edit?usp=sharing).

## Task 1 : 

- Created a package [Task1](https://github.com/withoutwaxaryan/ros2_tasks/tree/main/task1)
- Created 2 nodes, Node_A & Node_B, each of which consists of a publisher & a subscriber.
- Node_A consists of a Publisher, publishing on topic_1, Subscriber subscribing to topic_2.
- Node_B consists of a Publisher, publising on topic_2, Subscriber subscribing to topic_1.

When Node_A's publisher publishes a number (eg. 12) on topic_1, Node_B receives the message through its subscriber. Node_B then doubles the number and publishes
the doubled-number (24) on topic_2. Node_A's subscriber subscribes to topic_2 and receives the message and prints the result onto the terminal.

Here's the [Output of Task 1](https://github.com/withoutwaxaryan/ros2_tasks/blob/main/Outputs/task1.png).

## Task 2: 

- Created a service - client package [Task2_py](https://github.com/withoutwaxaryan/ros2_tasks/tree/main/task2_py) & [Interface](https://github.com/withoutwaxaryan/ros2_tasks/tree/main/interface) package.
- Client enters two numbers, and service publishes the log message that it received the request. Then the client receives the response as the product of the two numbers.
- Created a Custom Message (Int64) & Interface package for the service client task.
- Implemented in Python

Here's the [Output of Task 2](https://github.com/withoutwaxaryan/ros2_tasks/blob/main/Outputs/task2.png).


## References - [ROS2 Documentation](https://docs.ros.org/en/foxy/index.html)
