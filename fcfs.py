def survive_the_morning_rush(ticket_stack):
    # Line up by arrival time so we handle the first folks first
    ticket_stack.sort(key=lambda x: x['walk_in_time'])

    clock_on_the_wall = 0
    
    for ticket in ticket_stack:
        # If the cook is standing around waiting for a customer, jump the clock forward
        if clock_on_the_wall < ticket['walk_in_time']:
            clock_on_the_wall = ticket['walk_in_time']
        
        ticket['griddle_start'] = clock_on_the_wall
        
        # Figure out when the plate is ready and how long the customer was in the building
        ticket['plate_served'] = ticket['griddle_start'] + ticket['cooking_duration']
        ticket['total_diner_time'] = ticket['plate_served'] - ticket['walk_in_time']
        
        # 'Wait time' is just total time minus the time spent actually cooking
        ticket['hangry_wait_time'] = ticket['total_diner_time'] - ticket['cooking_duration']
        
        # The griddle is tied up until this plate is served
        clock_on_the_wall = ticket['plate_served']

    return ticket_stack

def results(completed_orders):
    # Printing the header for the shift report
    print("\n WAFFLE HOUSE ORDER LOG (FCFS)")
    print(f"{'Booth':<8} | {'Arrival':<8} | {'Cook Time':<10} | {'Served':<8} | {'Total Stay':<10} | {'Wait'}")
    
    total_waiting_time = 0
    total_stay_time = 0
    
    for order in completed_orders:
        total_waiting_time += order['hangry_wait_time']
        total_stay_time += order['total_diner_time']
        
        print(f"Booth {order['id']:<2} | {order['walk_in_time']:<8} | {order['cooking_duration']:<10} | "
              f"{order['plate_served']:<8} | {order['total_diner_time']:<10} | {order['hangry_wait_time']}")

    # Crunch the averages to see how the morning went
    avg_wait = total_waiting_time / len(completed_orders)
    avg_stay = total_stay_time / len(completed_orders)
    
    print("\n")
    print("--- ORDER UP! ---")
    print(f"Average Wait: {round(avg_wait, 2)} minutes")
    print(f"Average Total Stay:   {round(avg_stay, 2)} minutes")

if __name__ == "__main__":
    # Our morning crowd: a trucker, a family, and the law.
    morning_tickets = [
        {'id': 1, 'walk_in_time': 0, 'cooking_duration': 5},
        {'id': 2, 'walk_in_time': 3, 'cooking_duration': 9},
        {'id': 3, 'walk_in_time': 6, 'cooking_duration': 6}
    ]
    
    final_orders = survive_the_morning_rush(morning_tickets)
    results(final_orders)