Ex1_OOP
# Object Oriented Programming - Exercise 1

This task is dedicated to learning python when it is actually a sequel to task 0 (performed in java).
Similar to task 0, this task also opens up an algorithm for a system of smart elevators of a high-rise building.
In this task the challenge will focus on the offline version of the problem - meaning all the readings are given to us in advance, and we are only required to embed each reading in a benevolent manner (so that the rule of waiting for elevators is reduced to a minimum). In fact, the current task focuses mainly on the challenge of assigning a "call" to the elevator, but in order to perform this task properly we will also need to understand and simulate the movement of the elevators.

B.json and Calls.csv files represents the building and all the calls for the given scenario, in return, the algo will output a calls.csv file with elevator allocated to each call in the last column.

## Literature Overview - Elevator's Algorithms

- Wikipedia | Elevator algorithm: Wikipedia gives an overview on the elevator algorithm and the idea of the SCAN algorithm. [https://en.wikipedia.org/wiki/Elevator_algorithm]

- GeeksForGeeks | Smart Elevator: On GeeksForGeeks a students covers the topic and suggets a perspective on the problem and it's possible solution. [https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup]

- Disk Scheduling Algorithms: Digging deeper, we look into the Disk Scheduling Algorithm and it’s need and purposes.
[https://www.lnjpitchapra.in/wp-content/uploads/2020/04/file_5e97ef5088ac0.pdf]


## Algorithm Overview

Initialization:

- Building

- Calls list

- Elevators source locations

- Elevators departure time

- Elevators destinations

- Elevators arrival time

Elevator Allocating:
 
* for each call in calls array:
  * for each elevator in elevators array: 
    * calculate estimated arrival time of elevator to to its desired destination based on: call time, source locations and destination locations. set minimum arrival time and save with elevator index
  * if the call source and destination can fit inside current elevator process:
    * update the estimated arrival time of the current elevator destination to the current time plus another stop duration
  * if the call source can fit in the current process but call's destination does not:
    * update elevator's destination to the call's destination and update the time to minimum time
  * if both source and destination can not fit into the current elevator process:
    * update elevator's start location to call's source location
    * update elevator arrival time to start location to sum of: current destination arrival time, time from current destination to the call's source, another stop time
    * update elevator's destination floor to call's destination
    * update elevator's time of arrival to destination to minimum time

## Assignment Links

1. Github link: https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex1
2. Google's doc: https://docs.google.com/document/d/1D4aW2vRaKjwtSBY1gDyCC6SNRE5TRGwMerGIXUMkI_Y/edit?usp=sharing
3. Testing jar: https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex1/libs
4. Reporting form: https://docs.google.com/forms/d/e/1FAIpQLSffojCP9ftLSlk58_opDf-OpcLXvmuYzoQ3N_EQGtfozXjfjA/viewform?usp=sf_link
5. The Google sheet with the reported results: https://docs.google.com/spreadsheets/d/1fyFWvU_8d8UeaiUdyDujfgvt2dMs2mzzLd9QgUb33Wc/edit?usp=sharing
6. Submitting your work: https://docs.google.com/forms/d/e/1FAIpQLSe_NEppdfWbO9HTfbS9Yrlsd5ZQ-IWExYxAofACAHqM7uA5jA/viewform?usp=sf_link