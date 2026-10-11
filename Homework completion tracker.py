print("HOMEWORK COMPLETION TRACKER")
print("---------------------------")

# Ask how many homework tasks there are
total_tasks = int(input("How many homework tasks do you have? "))

# Loop variable: how many tasks are finished
completed = 0

# While loop repeats until all tasks are complete
while completed < total_tasks:
    print(f"\nYou have completed {completed} out of {total_tasks} tasks.")

    done_now = input("Did you finish a task? (yes/no/stop): ").lower()

    if done_now == "yes":
        completed += 1
        print("Nice work — keep going!")
    elif done_now == "no":
        print("Okay, keep trying.")
    elif done_now == "stop":
        print("Loop stopped early using break.")
        break
    else:
        print("Invalid input — try again.")

# Final message
print("\nTRACKER FINISHED")
print(f"Total tasks completed: {completed} out of {total_tasks}")
