# CPSC351-HW


At a bustling Waffle House during the morning rush, the chef functions as the central processor, carefully managing a constant stream of incoming customer order tickets. Each ticket represents a process where the arrival time marks a customer sitting down, and the burst time signifies the minutes required to prepare their specific meal. To prevent food from getting cold and to ensure the diner remains profitable, the team must balance kitchen output with customer satisfaction using various scheduling strategies. Chefs are experimenting with First Come First Serve to mimic a natural line, Shortest Job First to maximize turnover, and Round Robin to ensure every patron sees progress on their plate. Through this simulation, the group aims to highlight the trade-offs of each method, such as the "convoy effect" of a coffee order stuck behind a large platter or the risk of "starvation" for customers ordering complex meals.


### First Come First Serve (FCFS)
First Come First Serve (FCFS) was chosen because it closely mimics how a natural line works. In a diner environment, customers operate on an intuitive social contract: the person who sits down first should be served first.


#### Input / Output Details
Input: Walk-in Time (Arrival Time): The exact moment a customer sits at the booth and places their order.

Input: Cooking Duration (Burst Time): The total minutes the chef needs at the griddle to prepare that specific meal

Output: Plate Served (Completion Time): The time the meal is finished and leaves the kitchen.

Output: Hangry Wait Time (Wait Time): The time a customer spends sitting at the table before their food starts cooking.

Output: Total Diner Time (Turnaround Time): The full duration from sitting down to being served


### RoundRobin

### Shortest Job First (SJF)




Explanation of chosen algorithms.
Input/output details, results, and comparisons.
Key analysis and insights.