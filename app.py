import streamlit as st

# Title of the app
st.title("Interactive Exercise Progression Tool")

# User input
exercise = st.text_input("Enter an exercise (e.g., Air Squat, Push-Up):")

# Progression logic
progressions = {
    "Air Squat": ["Assisted Sit-to-Stand", "Chair Tap Squat", "Air Squat", "Goblet Squat", "Jump Squat"],
    "Push-Up": ["Wall Push-Up", "Inclined Push-Up", "Knee Push-Up", "Standard Push-Up", "Clap Push-Up"]
}

if exercise:
    if exercise in progressions:
        st.subheader(f"Progressions for {exercise}:")
        for step in progressions[exercise]:
            st.write(f"- {step}")
    else:
        st.error("Exercise not found. Try 'Air Squat' or 'Push-Up'.")
else:
    st.info("Enter an exercise name above to see its progression.")
