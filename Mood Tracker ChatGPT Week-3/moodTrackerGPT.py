from collections import deque
import random

# Initialize the emotion counts
emotions = {
    "happy": 0,
    "sad": 0,
    "stressed": 0,
    "excited": 0
}

# Sliding window to track the last 7 days
last_7_days = deque(maxlen=7)

try:
    N = int(input("Enter a time period in days you want to record your emotions for: "))
    if N <= 0:
        raise ValueError("Time period must be a positive integer.")
except ValueError as e:
    print(f"Invalid input. {e}")
    exit()

# Input emotions and update counts
for i in range(N):
    user_mood = input(f"Day {i + 1}: How are you feeling today? (happy, sad, stressed, excited) ").lower().strip()

    if user_mood in emotions:
        # If the deque is full, remove the oldest mood from the counts
        if len(last_7_days) == 7:
            old_mood = last_7_days.popleft()
            emotions[old_mood] -= 1

        # Add the new mood
        last_7_days.append(user_mood)
        emotions[user_mood] += 1
    else:
        print("Invalid input. Please select one of the four emotions given in the question.")
        continue

# Calculate percentages for the last 7 days
total = sum(emotions.values())  # Sum of the last 7 days
if total > 0:
    happy_percentage = emotions["happy"] / total * 100
    sad_percentage = emotions["sad"] / total * 100
    stressed_percentage = emotions["stressed"] / total * 100
    excited_percentage = emotions["excited"] / total * 100

    print(f"\nYour Mood in the last 7 days was {happy_percentage:.2f}% happy, "
          f"{sad_percentage:.2f}% sad, {stressed_percentage:.2f}% stressed, "
          f"and {excited_percentage:.2f}% excited.")
else:
    print("No data recorded for the last 7 days.")

# Predict mood for the next week
predicted_emotions = {emotion: 0 for emotion in emotions}
for day in range(7):  # Predict for 7 days
    # Use the last 7 days' probabilities to predict
    if total > 0:
        mood_prediction = random.choices(
            population=list(emotions.keys()),
            weights=[emotions["happy"], emotions["sad"], emotions["stressed"], emotions["excited"]],
            k=1
        )[0]
        predicted_emotions[mood_prediction] += 1

# Display predicted mood for the next week
print("\nPredicted Mood for the next 7 days:")
for mood, count in predicted_emotions.items():
    print(f"{mood.capitalize()}: {count} days")
