Ex1_OOP
# Object Oriented Programming - Exercise 1

authors: 
- Itamar Caspi: 315874982
- Elior Buskila 205493323

This task is dedicated to learning python when it is actually a sequel to task 0 (performed in java).
Similar to task 0, this task also opens up an algorithm for a system of smart elevators of a high-rise building.
In this task the challenge will focus on the offline version of the problem - meaning all the readings are given to us in advance, and we are only required to embed each reading in a benevolent manner (so that the rule of waiting for elevators is reduced to a minimum). In fact, the current task focuses mainly on the challenge of assigning a "call" to the elevator, but in order to perform this task properly we will also need to understand and simulate the movement of the elevators.

B.json and Calls.csv files represents the building and all the calls for the given scenario, in return, the algo will output a calls.csv file with elevator allocated to each call in the last column.

## Literature Overview - Elevator's Algorithms

- Wikipedia | Elevator algorithm: Wikipedia gives an overview on the elevator algorithm and the idea of the SCAN algorithm. [https://en.wikipedia.org/wiki/Elevator_algorithm]

- On-line Algorithms versus Off-line Algorithms for the Elevator: In most scheduling problems, if the problem were off-line, i.e. we know the arrival time of a request, then we can find the optimal schedule. But in reality this is not the case and we need to use some heuristics or strategies or on-line algorithms for scheduling.  The question is which strategy is better.
 [https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele...]

- This report investigates how effective different elevator group control
strategies are on a system with two elevators, and which optimizations that
can improve the performance of these strategies.
[https://www.diva-portal.org/smash/get/diva2:668654/FULLTEXT01.pdf]


## Algorithm Overview

Initialization:

- Reading the input files from the users
- Creating a list from the calls


Elevator Allocating:

* while calls list is not empty:
  * for each elevator:
   *   gets a workload capacity according to the elevator's efficiency
   *   the elevator is assigned calls according to its capacity at any given time
 
## UML
![WhatsApp Image 2021-11-19 at 13 00 30](https://user-images.githubusercontent.com/74679553/142613739-2084b6e0-8e4e-4e17-8149-133f2eb918df.jpeg)

## Assignment Links

1. Github link: https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex1
2. Google's doc: https://docs.google.com/document/d/1D4aW2vRaKjwtSBY1gDyCC6SNRE5TRGwMerGIXUMkI_Y/edit?usp=sharing
3. Testing jar: https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex1/libs
4. Reporting form: https://docs.google.com/forms/d/e/1FAIpQLSffojCP9ftLSlk58_opDf-OpcLXvmuYzoQ3N_EQGtfozXjfjA/viewform?usp=sf_link
5. The Google sheet with the reported results: https://docs.google.com/spreadsheets/d/1fyFWvU_8d8UeaiUdyDujfgvt2dMs2mzzLd9QgUb33Wc/edit?usp=sharing
6. Submitting your work: https://docs.google.com/forms/d/e/1FAIpQLSe_NEppdfWbO9HTfbS9Yrlsd5ZQ-IWExYxAofACAHqM7uA5jA/viewform?usp=sf_link
