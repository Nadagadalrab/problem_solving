input_steps = input("Enter your daily steps in a month separated by space: ")
steps_strings = input_steps.split()
steps = list(map(int, steps_strings))
highest_steps = max(steps)
lowest_steps = min(steps)
average_steps = sum(steps)/len(steps)
sorted_steps = sorted(steps, reverse=True)
print("the highest day steps: ", highest_steps)
print("The lowest day steps", lowest_steps)
print("the average is: ", average_steps)
print("Sorting from the highest to the lowest: ", sorted_steps)