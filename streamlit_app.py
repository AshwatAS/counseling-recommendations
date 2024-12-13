import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello! Welcome to career compass')
st.info("We help you decide what you should study in the future with the help of our large datasets and accurate algorithms.")

# Collect the name here

# Start with data collection
st.subheader("Try and answer as accurately as possible! Don't worry these questions are helping you, not deciding your future.")
preferred_environment=st.selectbox("What is your preferred work environment?",("Teaching and Training", "Remote/Work from Home", "On-site Industrial Work", "Desk Job", "Fieldwork", "Research Lab", "Creative Studio"))
salary_expect=st.slider("How much annual income do you expect from your job in the future?(INR)",400000,1500000,step=50000)

# Original Data
fields = ["Math", "CS", "Engg", "Med", "Arts", "Biz", "Sports Sci", "Journalism", "Law"]
data = {
    "Attribute": [
        "Logical Thinking", "Creativity", "Time Management", "Critical Thinking", "Adaptability",
        "Machine Learning", "Hardware Design", "Accounting/Finance", "Legal Research",
        "Cooking", "Acting", "DIY Projects",
        "Research-Oriented", "High-pressure Environment", "Creative Freedom",
        "Mathematics Score", "Science Score", "Literature Score", "Social Science Score"
    ],
    "Category": [
        "Soft Skill", "Soft Skill", "Soft Skill", "Soft Skill", "Soft Skill",
        "Technical Skill", "Technical Skill", "Technical Skill", "Technical Skill",
        "Hobby", "Hobby", "Hobby",
        "Work Preference", "Work Preference", "Work Preference",
        "Grade", "Grade", "Grade", "Grade"
    ],
    "Math": [0.9, 0.3, 0.7, 0.9, 0.5, 0.4, 0.3, 0.3, 0.3, 0.2, 0.2, 0.3, 0.9, 0.6, 0.4, 1.0, 0.8, 0.3, 0.3],
    "CS": [0.8, 0.5, 0.6, 0.9, 0.7, 0.9, 0.6, 0.5, 0.3, 0.3, 0.4, 0.4, 0.8, 0.8, 0.6, 0.9, 0.8, 0.4, 0.3],
    "Engg": [0.8, 0.6, 0.7, 0.8, 0.6, 0.8, 0.9, 0.5, 0.3, 0.4, 0.3, 0.4, 0.8, 0.8, 0.5, 0.8, 0.8, 0.3, 0.3],
    "Med": [0.5, 0.4, 0.8, 0.7, 0.5, 0.6, 0.5, 0.3, 0.2, 0.5, 0.3, 0.4, 0.8, 0.9, 0.3, 0.8, 1.0, 0.3, 0.3],
    "Arts": [0.3, 0.9, 0.8, 0.4, 0.7, 0.3, 0.2, 0.3, 0.4, 0.6, 0.9, 0.7, 0.6, 0.9, 0.9, 0.3, 0.4, 0.9, 0.8],
    "Biz": [0.6, 0.7, 0.8, 0.7, 0.8, 0.6, 0.5, 0.9, 0.5, 0.6, 0.6, 0.5, 0.7, 0.7, 0.8, 0.7, 0.6, 0.7, 0.5],
    "Sports Sci": [0.4, 0.5, 0.6, 0.5, 0.8, 0.3, 0.3, 0.3, 0.3, 0.6, 0.3, 0.6, 0.7, 0.6, 0.6, 0.4, 0.6, 0.4, 0.3],
    "Journalism": [0.6, 0.8, 0.6, 0.7, 0.8, 0.4, 0.3, 0.3, 0.5, 0.4, 0.8, 0.4, 0.6, 0.5, 0.7, 0.4, 0.5, 0.9, 0.8],
    "Law": [0.7, 0.5, 0.8, 0.9, 0.6, 0.3, 0.3, 0.5, 0.9, 0.3, 0.5, 0.3, 0.8, 0.8, 0.5, 0.5, 0.4, 0.8, 1.0]
}
df = pd.DataFrame(data)

# User Inputs
student_input = {
    "Logical Thinking": 0.8,
    "Creativity": 0.6,
    "Time Management": 0.7,
    "Critical Thinking": 0.9,
    "Adaptability": 0.8,
    "Machine Learning": 0.5,
    "Hardware Design": 0.4,
    "Accounting/Finance": 0.6,
    "Legal Research": 0.5,
    "Cooking": 0.3,
    "Acting": 0.2,
    "DIY Projects": 0.4,
    "Research-Oriented": 0.9,
    "High-pressure Environment": 0.7,
    "Creative Freedom": 0.8,
    "Mathematics Score": 1.0,
    "Science Score": 0.9,
    "Literature Score": 0.7,
    "Social Science Score": 0.6
}

# Add Salary Data (Estimates based on current market conditions in INR)
salaries = {
    "Math": 600000,
    "CS": 1200000,
    "Engg": 800000,
    "Med": 1500000,
    "Arts": 400000,
    "Biz": 900000,
    "Sports Sci": 500000,
    "Journalism": 450000,
    "Law": 950000
}

# Add Years to Land a Job
years_to_land = {
    "Math": 5,
    "CS": 4,
    "Engg": 4,
    "Med": 8,
    "Arts": 4,
    "Biz": 5,
    "Sports Sci": 4,
    "Journalism": 3,
    "Law": 5
}

# Weighted Decision Matrix
weighted_df = df.copy()
for attr, weight in student_input.items():
    weighted_df.loc[weighted_df["Attribute"] == attr, fields] *= weight

# Ideal Solutions
ideal_solution = weighted_df[fields].max()
negative_ideal_solution = weighted_df[fields].min()

# Separations
separation_ideal = np.sqrt(((weighted_df[fields] - ideal_solution) ** 2).sum(axis=0))
separation_negative = np.sqrt(((weighted_df[fields] - negative_ideal_solution) ** 2).sum(axis=0))

# Relative Closeness
relative_closeness = separation_negative / (separation_ideal + separation_negative)
ranking = relative_closeness.sort_values(ascending=False)

# New Inputs for Filters
def filter_jobs(time_filter, salary_filter):
    filtered_jobs = []
    for idx, field in enumerate(ranking.index):
        if idx == 0:  # Always include the top-ranked job
            filtered_jobs.append((field, True))  # Mark as "best field"
        elif len(filtered_jobs) - 1 < 3:  # Ensure at least 3 additional jobs
            if years_to_land[field] <= time_filter and salaries[field] >= salary_filter:
                filtered_jobs.append((field, False))  # Regular fields
    return filtered_jobs

# Display Results
def display_rankings_and_filters(time_filter, salary_filter):
    print("Ranked Fields (TOPSIS):")
    for field, score in ranking.items():
        print(f"{field}: {score:.2f}")
    
    print("\nFiltered Fields:")
    filtered = filter_jobs(time_filter, salary_filter)
    if len(filtered) == 1:  # Only the best field is present
        print("No fields match the given filters.")
        print(f"Best Field: {filtered[0][0]}: Salary ₹{salaries[filtered[0][0]]}, Years to Land {years_to_land[filtered[0][0]]}")
    else:
        for job, is_best in filtered:
            if is_best:
                print(f"{job} (Best Field): Salary ₹{salaries[job]}, Years to Land {years_to_land[job]}")
            else:
                print(f"{job}: Salary ₹{salaries[job]}, Years to Land {years_to_land[job]}")

