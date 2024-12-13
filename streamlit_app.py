import streamlit as st
import pandas as pd
import numpy as np

# Title and Introduction
st.title('Hello! Welcome to Career Compass')
st.info("We help you decide what you should study in the future with the help of our large datasets and accurate algorithms.")

# User Inputs
st.subheader("Try and answer as accurately as possible! Don't worry, these questions are helping you, not deciding your future.")
preferred_environment = st.selectbox("What is your preferred work environment?",
                                      ("Teaching and Training", "Remote/Work from Home", "On-site Industrial Work",
                                       "Desk Job", "Fieldwork", "Research Lab", "Creative Studio"))
salary_expect = st.slider("How much annual income do you expect from your job in the future? (INR)", 400000, 1250000, step=50000)
time_filter = st.slider("Maximum Years to Land a Job", 3, 8, step=1)
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Use st.multiselect for multiple selection
selected_options = st.multiselect("Select one or more options:", options)
st.write("You selected:", selected_options)

# # Data
# fields = ["Math", "CS", "Engg", "Med", "Arts", "Biz", "Sports Sci", "Journalism", "Law"]
# data = {
#     "Attribute": [
#         "Logical Thinking", "Creativity", "Time Management", "Critical Thinking", "Adaptability",
#         "Machine Learning", "Hardware Design", "Accounting/Finance", "Legal Research",
#         "Cooking", "Acting", "DIY Projects",
#         "Research-Oriented", "High-pressure Environment", "Creative Freedom",
#         "Mathematics Score", "Science Score", "Literature Score", "Social Science Score"
#     ],
#     "Category": [
#         "Soft Skill", "Soft Skill", "Soft Skill", "Soft Skill", "Soft Skill",
#         "Technical Skill", "Technical Skill", "Technical Skill", "Technical Skill",
#         "Hobby", "Hobby", "Hobby",
#         "Work Preference", "Work Preference", "Work Preference",
#         "Grade", "Grade", "Grade", "Grade"
#     ],
#     "Math": [0.9, 0.3, 0.7, 0.9, 0.5, 0.4, 0.3, 0.3, 0.3, 0.2, 0.2, 0.3, 0.9, 0.6, 0.4, 1.0, 0.8, 0.3, 0.3],
#     "CS": [0.8, 0.5, 0.6, 0.9, 0.7, 0.9, 0.6, 0.5, 0.3, 0.3, 0.4, 0.4, 0.8, 0.8, 0.6, 0.9, 0.8, 0.4, 0.3],
#     "Engg": [0.8, 0.6, 0.7, 0.8, 0.6, 0.8, 0.9, 0.5, 0.3, 0.4, 0.3, 0.4, 0.8, 0.8, 0.5, 0.8, 0.8, 0.3, 0.3],
#     "Med": [0.5, 0.4, 0.8, 0.7, 0.5, 0.6, 0.5, 0.3, 0.2, 0.5, 0.3, 0.4, 0.8, 0.9, 0.3, 0.8, 1.0, 0.3, 0.3],
#     "Arts": [0.3, 0.9, 0.8, 0.4, 0.7, 0.3, 0.2, 0.3, 0.4, 0.6, 0.9, 0.7, 0.6, 0.9, 0.9, 0.3, 0.4, 0.9, 0.8],
#     "Biz": [0.6, 0.7, 0.8, 0.7, 0.8, 0.6, 0.5, 0.9, 0.5, 0.6, 0.6, 0.5, 0.7, 0.7, 0.8, 0.7, 0.6, 0.7, 0.5],
#     "Sports Sci": [0.4, 0.5, 0.6, 0.5, 0.8, 0.3, 0.3, 0.3, 0.3, 0.6, 0.3, 0.6, 0.7, 0.6, 0.6, 0.4, 0.6, 0.4, 0.3],
#     "Journalism": [0.6, 0.8, 0.6, 0.7, 0.8, 0.4, 0.3, 0.3, 0.5, 0.4, 0.8, 0.4, 0.6, 0.5, 0.7, 0.4, 0.5, 0.9, 0.8],
#     "Law": [0.7, 0.5, 0.8, 0.9, 0.6, 0.3, 0.3, 0.5, 0.9, 0.3, 0.5, 0.3, 0.8, 0.8, 0.5, 0.5, 0.4, 0.8, 1.0]
# }
# df = pd.DataFrame(data)

# # Salaries and Years to Land a Job
# salaries = {"Math": 600000, "CS": 1200000, "Engg": 800000, "Med": 1500000, "Arts": 400000, "Biz": 900000, "Sports Sci": 500000, "Journalism": 450000, "Law": 950000}
# years_to_land = {"Math": 5, "CS": 4, "Engg": 4, "Med": 8, "Arts": 4, "Biz": 5, "Sports Sci": 4, "Journalism": 3, "Law": 5}

# # Decision Matrix Calculation
# weighted_df = df.copy()
# student_input = {"Logical Thinking": 0.8, "Creativity": 0.6, "Time Management": 0.7, "Critical Thinking": 0.9, "Adaptability": 0.8, "Mathematics Score": 1.0}
# for attr, weight in student_input.items():
#     weighted_df.loc[weighted_df["Attribute"] == attr, fields] *= weight

# ideal_solution = weighted_df[fields].max()
# negative_ideal_solution = weighted_df[fields].min()

# separation_ideal = np.sqrt(((weighted_df[fields] - ideal_solution) ** 2).sum(axis=0))
# separation_negative = np.sqrt(((weighted_df[fields] - negative_ideal_solution) ** 2).sum(axis=0))
# relative_closeness = separation_negative / (separation_ideal + separation_negative)
# ranking = relative_closeness.sort_values(ascending=False)

# # Filter Jobs
# def filter_jobs(time_filter, salary_filter):
#     filtered_jobs = []
#     for field in ranking.index:
#         if years_to_land[field] <= time_filter and salaries[field] >= salary_filter:
#             filtered_jobs.append(field)
#     return filtered_jobs

# # Display Output Dynamically

# filtered_jobs = filter_jobs(time_filter, salary_expect)

# st.subheader("Career Recommendations:")
# st.write(f"**Best Field**: {ranking.index[0]} (Salary: ₹{salaries[ranking.index[0]]}, Years to Land: {years_to_land[ranking.index[0]]})")
# if filtered_jobs:
#     st.write("**Other Suitable Fields:**")
#     for field in filtered_jobs:
#         st.write(f"{field}: Salary ₹{salaries[field]}, Years to Land {years_to_land[field]}")
# else:
#     st.write("No fields match the given filters.")
