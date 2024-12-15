let habitName;
let timer;
let habitList = [];
let habitCount = 0;

// Function to add habit
document.getElementById("addHabit").onclick = function() {
    habitName = document.getElementById("habitName").value;
    timer = document.getElementById("reminderTime").value;
    habitList.push({habitNumber: habitCount, habitName: habitName, habitTime: timer});
    habitCount++;
    window.alert("Habit added successfully");
    console.log(habitList); // Debug: Log the habit list
}

// Function to check habit times
function checkHabitTimes() {
    let currentTime = new Date().toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' });
    console.log(`Current Time: ${currentTime}`); // Debug: Log the current time
    habitList.forEach(habit => {
        console.log(`Checking habit: ${habit.habitName} at ${habit.habitTime}`); // Debug: Log habit check
        if (habit.habitTime === currentTime) {
            window.alert(`Time to do your habit: ${habit.habitName}`);
        }
    });
}

// Every minute
setInterval(checkHabitTimes, 60000);