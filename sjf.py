# CPSC 351 MW 4-5:15pm
# Group 7
# SJF (Non-preemptive) Implementation


class OrderTicket:
    def __init__(self, pid, arrival_time, cook_time):
        self.pid = pid  # process ID
        self.arrival_time = arrival_time
        self.cook_time = cook_time
        
        # Outputs to calculate
        self.completion_time = 0
        self.turnaround_time = 0    # time from arrival to completion
        self.waiting_time = 0   # time in queue before execution


def sjf_restaurant_orders(orders):
    num_orders = len(orders)
    completed_orders = 0
    current_time = 0
    gantt_chart = []
    
    # Sort orders by arrival time, and set all to incomplete
    orders.sort(key=lambda x: x.arrival_time)
    is_completed = [False] * num_orders
    
    while completed_orders != num_orders:
        # Find orders that have arrived and still need to be cooked
        available_orders = []
        for i in range(num_orders):
            if orders[i].arrival_time <= current_time and not is_completed[i]:
                available_orders.append((orders[i], i))     # track index so we can mark order completed later
        
        # If there are no arrived orders to be cooked, the chef waits (idle)
        if not available_orders:
            # Skip ahead to the next incoming order
            next_arrival = min([orders[i].arrival_time for i in range(num_orders) if not is_completed[i]])
            gantt_chart.append(f"IDLE [{current_time}m - {next_arrival}m]")     # update chart
            current_time = next_arrival
            continue
        
        # Sort current orders by shortest cook time, if tied, sort by arrival time, if still tied, sort by pid
        available_orders.sort(key=lambda x: (x[0].cook_time, x[0].arrival_time, x[0].pid))
        
        # Select the shortest available job
        current_order, order_index = available_orders[0]
        
        # Cook meal, record cook times
        start_time = current_time
        current_time += current_order.cook_time     # skip to end of cook time (complete order)
        gantt_chart.append(f"{current_order.pid} [{start_time}m - {current_time}m]")    # update chart
        
        # Calculate outputs for the completed order
        current_order.completion_time = current_time
        current_order.turnaround_time = current_order.completion_time - current_order.arrival_time
        current_order.waiting_time = current_order.turnaround_time - current_order.cook_time
        
        # Mark order as completed
        is_completed[order_index] = True
        completed_orders += 1

    # Display Output (Gantt chart + statistics)
    dashes = "-" * len(gantt_chart) * 17
    line = "=" * 14
    print(line + " GANTT CHART / TIMELINE " + line)
    print(dashes)
    print("|  " + " | ".join(gantt_chart) + "  |")
    print(dashes)

    print(f"\n{'Process ID':<10} | {'Arrival':<8} | {'Burst':<6} | {'Completion':<11} | {'Turnaround':<11} | {'Waiting':<8}")
    print("-" * 70)
    
    total_turnaround = 0
    total_waiting = 0
    
    # Sort by Process ID for display, calculate total turnaround and waiting times
    for order in sorted(orders, key=lambda x: x.pid): 
        print(f"{order.pid:<10} | {order.arrival_time:<8} | {order.cook_time:<6} | {order.completion_time:<11} | {order.turnaround_time:<11} | {order.waiting_time:<8}")
        total_turnaround += order.turnaround_time
        total_waiting += order.waiting_time
        
    print(f"\nAverage Turnaround Time: {total_turnaround / num_orders:.2f} minutes")
    print(f"Average Waiting Time:    {total_waiting / num_orders:.2f} minutes\n")


if __name__ == "__main__":
    restaurant_orders = [
        OrderTicket("P1", 0, 8), # arrives immediately, takes 8 mins
        OrderTicket("P2", 1, 2), # arrives at 1 min, takes 2 mins
        OrderTicket("P3", 3, 4) # arrives at 3 mins, takes 4 mins
    ]
    sjf_restaurant_orders(restaurant_orders)