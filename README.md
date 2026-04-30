# CPSC351-HW


At a bustling Waffle House during the morning rush, the chef functions as the central processor, carefully managing a constant stream of incoming customer order tickets. Each ticket represents a process where the arrival time marks a customer sitting down, and the burst time signifies the minutes required to prepare their specific meal. To prevent food from getting cold and to ensure the diner remains profitable, the team must balance kitchen output with customer satisfaction using various scheduling strategies. Chefs are experimenting with First Come First Serve to mimic a natural line, Shortest Job First to maximize turnover, and Round Robin to ensure every patron sees progress on their plate. Through this simulation, the group aims to highlight the trade-offs of each method, such as the "convoy effect" of a coffee order stuck behind a large platter or the risk of "starvation" for customers ordering complex meals.

### Running The code
To run any algorithm run:
```python3 file_name.py```


### First Come First Serve (FCFS)
First Come First Serve (FCFS) was chosen because it closely mimics how a natural line works. In a diner environment, customers operate on an intuitive social contract: the person who sits down first should be served first.


#### Input / Output Details
Input: Walk-in Time (Arrival Time): The exact moment a customer sits at the booth and places their order.

Input: Cooking Duration (Burst Time): The total minutes the chef needs at the griddle to prepare that specific meal

Output: Plate Served (Completion Time): The time the meal is finished and leaves the kitchen.

Output: Hangry Wait Time (Wait Time): The time a customer spends sitting at the table before their food starts cooking.

Output: Total Diner Time (Turnaround Time): The full duration from sitting down to being served


### RoundRobin (RR)
Round Robin Algorithm was chosen for this because it treats every ticket/order the same, giving it 3 minutes to cook every time until complete. To change the orders, go to the main, and change the arrival times and cooking durations needed. The code will document each cook as it happens.

Input: Ticket ID (Process ID): The way to differentiate multiple ticket orders.

Input: Walk-in Time (Arrival Time): The exact moment a customer sits at the booth and places their order.

Input: Cooking Duration (Burst Time): The total minutes the chef needs at the griddle to prepare that specific meal

Output: Gantt (Gantt Chart): The time the meal is finished and leaves the kitchen.

Output: Plate Served (Completion Time): The time the meal is finished and leaves the kitchen.

Output: Hangry Wait Time (Wait Time): The time a customer spends sitting at the table before their food starts cooking.

Output: Total Diner Time (Turnaround Time): The full duration from sitting down to being served

Output: Average metrics: The average turnaround time, average waiting time, and context switches.


### Shortest Job First (SJF)

Shortest Job First (SJF) was chosen because it allows the chef to complete the most amount of orders possible in a shorter time frame. By prioritizing the shortest orders, the chef is able to feed more customers quickly.

Input: Order Ticket (Process ID), unique customer tickets for each order.

Input: Arrival Time, the time in minutes that the customer is seated and places their order.

Input: Cook time (Burst time), the time in minutes that it takes the chef to complete an order.

Output: Gantt (Gantt Chart), chart displaying the times for when each order was being created.

Output: Completion Time, the time the food is finished being prepared and served to the customer.

Output: Turnaround Time, the total time from when the customer arrived to when their food was served. 

Output: Waiting Time, the time the customer had to wait before their food started being prepared.

Output: Average Metrics, the average turnaround time and average waiting time.
