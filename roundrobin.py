from collections import deque

def robin(tickets):
    cooktime = 3         #this cooktime is for the code to know how long to process each order
    time = 0
    queue = deque()
    gantt = []
    completion_time = {}
    context_switches = 0

    for ticket in tickets:  #this is used to save the original duration
         ticket["remaining_time"] = ticket["cooking_duration"]

    tickets = sorted(tickets, key = lambda x: x["walk_in_time"])
    i = 0
    last_ticket_id = None

    while i < len(tickets) or queue:    #this while function adds the tickets onto the queue if the ticket's walk in time is less than the current time
         while i < len(tickets) and tickets[i]["walk_in_time"] <= time:
              queue.append(tickets[i])
              i += 1


         if not queue:  #this makes it so that if there is nothing in the queue, the current time will jump to the time of arrival of the next order.
              time = tickets[i]["walk_in_time"]
              continue
              
         ticket = queue.popleft()

         if last_ticket_id is not None and last_ticket_id != ticket["id"]: #this keeps track of context switches
            context_switches += 1
         last_ticket_id = ticket["id"]

         start_time = time

         cook = min(cooktime, ticket["remaining_time"])   #this chooses the smalllest among the cooktime, and the cooking duration. If the cook time is smaller, then it cooks for 3 minutes. If the duration is smaller, then if cooks for that duration.
         ticket["remaining_time"] -= cook                 
         time += cook
         end_time = time
         print(f"Current time: {time}, Ticket id({ticket['id']}) cooked for {cook} minutes")      #added this to visualise when things are happening

         gantt.append((ticket["id"], start_time, end_time))  #the cook time and end times are all kepts into the gantt chart

         while i < len(tickets) and tickets[i]["walk_in_time"] <= time:  #this is the same while as the one before, now we check if there has been any new orders since we updated the time.
              queue.append(tickets[i])
              i += 1

         if ticket["remaining_time"] == 0:    #if the ticket's duration is 0, this means it is finished.
            completion_time[ticket["id"]] = time
            print(f"Ticket id({ticket['id']}) finished cooking at time: {time}\n")
         else: 
              queue.append(ticket)
              print(f"Ticket id({ticket['id']}) has {ticket['cooking_duration']} minutes remaining to cook, goes to the back of queue.\n")

    print("\nGantt Chart / Timeline:")      #this is just formatting the gantt chart
    for task_id, start, end in gantt:
        print(f"| P{task_id} ({start}-{end}) ", end="")
    print("|")

    print("\nProcess Results:")
    total_turnaround = 0
    total_waiting = 0

    for ticket in tickets:   #this part calculates the completion time, turnaround time, and waiting time for all tickets, and displays it.
        id = ticket["id"]
        arrival = ticket["walk_in_time"]
        burst = ticket["cooking_duration"]
        completion = completion_time[id]

        turnaround = completion - arrival
        waiting = turnaround - burst

        total_turnaround += turnaround
        total_waiting += waiting

        print(f"Ticket {id}:")
        print(f"  Completion Time: {completion}")
        print(f"  Turnaround Time: {turnaround}")
        print(f"  Waiting Time: {waiting}\n")

    n = len(tickets)

    print("\nAverage Metrics:")     
    print(f"Average Turnaround Time: {total_turnaround / n:.2f}")
    print(f"Average Waiting Time: {total_waiting / n:.2f}")
    print(f"Context Switches: {context_switches}")


if __name__ == "__main__":
    # morning customers:
    # 1. Solo Trucker  
    # 2. Family of 4
    # 3. Local Sheriff
    morning_tickets = [
        {'id' : 1, 'walk_in_time': 0, 'cooking_duration': 5},
        {'id' : 2, 'walk_in_time': 3, 'cooking_duration': 9},
        {'id' : 3, 'walk_in_time': 6, 'cooking_duration': 6}
    ]
    
    robin(morning_tickets)
   
