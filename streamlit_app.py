# import streamlit as st

# st.title('Hello! Welcome to career compass')
# st.info("We help you decide what you should study in the future with the help of our large datasets and accurate algorithms.")

# # Collect the name here

# # Start with data collection
# st.subheader("Try and answer as accurately as possible! Don't worry these questions are helping you, not deciding your future.")
# preferred_environment=st.selectbox("What is your preferred work environment?",("Teaching and Training", "Remote/Work from Home", "On-site Industrial Work", "Desk Job", "Fieldwork", "Research Lab", "Creative Studio"))
# salary_expect=st.slider("How much annual income do you expect from your job in the future?(INR)",400000,1500000,step=50000)



import streamlit as st
import pandas as pd
import numpy as np

# Import the TOPSIS logic from the uploaded file
# Ensure the TOPSIS_V5.py file is in the same directory as this Streamlit script
from TOPSIS_V5 import df, student_input, salaries, years_to_land, ranking, filter_jobs

st.title('Hello! Welcome to Career Compass')
st.info("We help you decide what you should study in the future with the help of our large datasets and accurate algorithms.")

# Collect user inputs
st.subheader("Try and answer as accurately as possible! Don't worry these questions are helping you, not deciding your future.")

# Preferred work environment
preferred_environment = st.selectbox("What is your preferred work environment?", 
                                     ("Teaching and Training", "Remote/Work from Home", "On-site Industrial Work", 
                                      "Desk Job", "Fieldwork", "Research Lab", "Creative Studio"))

# Expected salary
salary_expect = st.slider("How much annual income do you expect from your job in the future? (INR)", 400000, 1500000, step=50000)

# Years to land a job
time_to_land_job = st.slider("How many years are you willing to invest in education and preparation for your career?", 1, 10, step=1)

# Get user attributes (mocked or manually entered)
st.subheader("Rate the following skills (0.0 to 1.0):")
user_inputs = {}
for attr in student_input.keys():
    user_inputs[attr] = st.slider(attr, 0.0, 1.0, student_input[attr])

# Run TOPSIS Algorithm on user input
if st.button("Find Best Career Path"):
    # Update the weights based on user inputs
    weighted_df = df.copy()
    for attr, weight in user_inputs.items():
        weighted_df.loc[weighted_df["Attribute"] == attr, df.columns[2:]] *= weight

    # Calculate Ideal Solutions
    ideal_solution = weighted_df.iloc[:, 2:].max()
    negative_ideal_solution = weighted_df.iloc[:, 2:].min()

    # Separations
    separation_ideal = np.sqrt(((weighted_df.iloc[:, 2:] - ideal_solution) ** 2).sum(axis=0))
    separation_negative = np.sqrt(((weighted_df.iloc[:, 2:] - negative_ideal_solution) ** 2).sum(axis=0))

    # Relative Closeness
    relative_closeness = separation_negative / (separation_ideal + separation_negative)
    ranking = relative_closeness.sort_values(ascending=False)

    # Filter jobs based on user constraints
    filtered_jobs = filter_jobs(time_to_land_job, salary_expect)

    # Display the ranked fields
    st.subheader("Ranked Career Fields:")
    for field, score in ranking.items():
        st.write(f"{field}: {score:.2f}")

    # Display the filtered results
    st.subheader("Filtered Career Recommendations:")
    if len(filtered_jobs) == 1:  # Only the best field is present
        st.warning("No fields match the given filters.")
        best_field = filtered_jobs[0][0]
        st.write(f"Best Field: **{best_field}**: Salary ₹{salaries[best_field]}, Years to Land {years_to_land[best_field]}")
    else:
        for job, is_best in filtered_jobs:
            if is_best:
                st.write(f"**{job} (Best Field)**: Salary ₹{salaries[job]}, Years to Land {years_to_land[job]}")
            else:
                st.write(f"{job}: Salary ₹{salaries[job]}, Years to Land {years_to_land[job]}")
