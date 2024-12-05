emotions = {
    "happy": 0,
    "sad": 0,
    "stressed": 0,
    "excited": 0
}

try:
    N = int(input("Enter a time period in days you want to record your emotions for: "))
    if N <= 0:
        raise ValueError("Time period must be a positive integer.")
except ValueError as e:
    print(f"Invalid input. {e}")
    exit()


i = 0
while i < N:
    user_mood = input(f"Day {i + 1}: How are you feeling today? (happy, sad, stressed, excited) ").lower().strip()

    if user_mood in emotions:
        emotions[user_mood] += 1
        i += 1
    else:
        print("Invalid input. Please select one of the four emotions given in the question.")

happy_percentage = emotions["happy"]/N * 100
sad_percentage = emotions["sad"]/N * 100
stressed_percentage = emotions["stressed"]/N * 100
excited_percentage = emotions["excited"]/N * 100

print(f"Your Mood this week was {happy_percentage} % happy, {sad_percentage} % sad, {stressed_percentage}% stressed, and {excited_percentage}% excited.")