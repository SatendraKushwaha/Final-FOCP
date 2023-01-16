#program to calculate best time runner
import time

#prints the output
print("Park Run Timer")
print("~~~~~~~~~~~~~~************~~~~~~~~~~~~~~")

print("WELCOME and Let's go!")


 # initialize variables
total_runners = 0
total_time = 0
fastest_time = 0
slowest_time = 0
best_time_here = 0
best_time_here_runner = 0

 # ask user to enter data
while True:
    data = input("> ")
    if data == "END":
        break
     
    # get the runner number and a time.
    parts = data.split("::")
    
    if len(parts) != 2:
      print("Error in data stream. Ignoring. Carry on.")
      continue
    runner_number = parts[0]
    time = int(parts[1])
    # adds total runners and time.
          
    total_runners += 1
            
    total_time += time
           
    #if else condition is to satisfy the condition.       
    if fastest_time == 0 or time < fastest_time:
            fastest_time = time
            best_time_here_runner = runner_number
            
    if slowest_time == 0 or time > slowest_time:
            slowest_time = time
    
if total_runners == 0:
    print("No data found. Nothing to do. What a pity.")
else: 
    # calculates the average time.
    average_time = total_time / total_runners
  # converts average time to minutes and seconds.
    
    average_time_minutes = int(average_time / 60)
    average_time_seconds = int(average_time % 60)

 # converts fastest time to minutes and seconds.
    fastest_time_minutes = int(fastest_time / 60)
    fastest_time_seconds = int(fastest_time % 60)

 # converts slowest time to minutes and seconds.

    slowest_time_minutes = int(slowest_time / 60)
    slowest_time_seconds = int(slowest_time % 60)

# prints the results.

    print(f"Total Runners: {total_runners}")
    print(f"Average Time:  {average_time_minutes} minutes, {average_time_seconds} seconds")
    print(f"Fastest Time:  {fastest_time_minutes} minutes, {fastest_time_seconds} seconds")
    print(f"Slowest Time:  {slowest_time_minutes} minutes, {slowest_time_seconds} seconds")

    print(f"Best Time Here: Runner #{best_time_here_runner}")