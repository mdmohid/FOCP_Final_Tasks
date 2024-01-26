import sys

def analyze_log_file(file_path):  # defines a function that takes a file path as input and analyzes the contents of that file.
    try:
        with open(file_path, 'r') as file:  # open the file in read mode
            lines = file.readlines()
    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
        return
    except Exception as e:
        print(f'Error reading file: {e}')
        return
    
    # Initializing Variables for Cat Visits and duration:
    cat_visits = 0
    other_cats = 0
    total_time_in_house = 0
    durations = []

    for line in lines:   # Iterate through each line in the log file
        if line.startswith("OURS"): # Check if the line corresponds to a visit by our cat
            cat_visits += 1
            entry_time, exit_time = [int(item) for item in line.strip().split(',')[1:]] # Extract entry and exit times from the log entry
            duration = exit_time - entry_time
            durations.append(duration)
            total_time_in_house += duration
        elif line.startswith("THEIRS"): # Check if the line corresponds to a visit by another cat
            other_cats += 1

     # Check if there were no visits by our cat
    if cat_visits == 0:
        print("No cat visits found in the log.")
        return
    
    # calculation of duration by cat visits
    average_duration = sum(durations) / len(durations)
    longest_duration = max(durations)
    shortest_duration = min(durations)
    
    # Printing results
    Log_file = "\nLog File Analysis"
    print(Log_file)
    print(len(Log_file) * "=")
    print(f"\nCat Visits: {cat_visits}")
    print(f"Other Cats: {other_cats}\n")
    print(f"\nTotal Time in House: {total_time_in_house // 60} Hours, {total_time_in_house % 60} Minutes")
    print(f"\nAverage Visit Length: {int(average_duration)} Minutes")
    print(f"Longest Visit:        {longest_duration} Minutes")
    print(f"Shortest Visit:       {shortest_duration} Minutes")

if __name__ == "__main__":
    if len(sys.argv) != 2: # Check if the command line argument is missing
        print("Missing command line argument!")
    else:
        # Extract the file path from the command line argument and analyze the log file
        file_path = sys.argv[1]
        analyze_log_file(file_path)
