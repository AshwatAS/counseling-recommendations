import streamlit as st
import pandas as pd
import numpy as np

# Import the TOPSIS logic from the uploaded file
# Ensure the TOPSIS_V5.py file is in the same directory as this Streamlit script
try:
    from TOPSIS_V5 import df, student_input, salaries, years_to_land, filter_jobs
except ImportError:
    st.error("Error importing TOPSIS_V5 module. Ensure the file exists and includes required functions and variables.")
    st.stop()

# Validate that imported variables are initialized
if not all([isinstance(df, pd.DataFrame), isinstance(student_input, dict), 
            isinstance(salaries, dict), isinstance(years_to_land, dict)]):
    st.error("TOPSIS_V5.py variables (df, student_input, salaries, years_to_land) must be properly defined.")
    st.stop()

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

# Get user attributes (default values from `student_input`)
st.subheader("Rate the following skills (0.0 to 1.0):")
user_inputs = {}
for attr in student_input.keys():
    default_value = student_input.get(attr, 0.5)  # Use default of 0.5 if key is missing
    user_inputs[attr] = st.slider(attr, 0.0, 1.0, default_value)

# Run TOPSIS Algorithm on user input
if st.button("Find Best Career Path"):
    try:
        # Update the weights based on user inputs
        weighted_df = df.copy()
        for attr, weight in user_inputs.items():
            if attr in weighted_df["Attribute"].values:
                weighted_df.loc[weighted_df["Attribute"] == attr, df.columns[2:]] *= weight
            else:
                st.error(f"Attribute '{attr}' is missing in the dataset.")
                st.stop()

        # Calculate Ideal Solutions
        ideal_solution = weighted_df.iloc[:, 2:].max()
        negative_ideal_solution = weighted_df.iloc[:, 2:].min()

        # Separations
        separation_ideal = np.sqrt(((weighted_df.iloc[:, 2:] - ideal_solution) ** 2).sum(axis=1))
        separation_negative = np.sqrt(((weighted_df.iloc[:, 2:] - negative_ideal_solution) ** 2).sum(axis=1))

        # Relative Closeness
        relative_closeness = separation_negative / (separation_ideal + separation_negative)
        ranking = pd.Series(relative_closeness, index=weighted_df["Attribute"]).sort_values(ascending=False)

        # Filter jobs based on user constraints
        filtered_jobs = filter_jobs(time_to_land_job, salary_expect)

        # Display the ranked fields
        st.subheader("Ranked Career Fields:")
        for field, score in ranking.items():
            st.write(f"{field}: {score:.2f}")

        # Display the filtered results
        st.subheader("Filtered Career Recommendations:")
        if len(filtered_jobs) == 0:  # No matching jobs found
            st.warning("No fields match the given filters.")
        else:
            for job, is_best in filtered_jobs:
                if is_best:
                    st.write(f"**{job} (Best Field)**: Salary ₹{salaries[job]}, Years to Land {years_to_land[job]}")
                else:
                    st.write(f"{job}: Salary ₹{salaries[job]}, Years to Land {years_to_land[job]}")
    except Exception as e:
        st.error(f"An error occurred during processing: {e}")
