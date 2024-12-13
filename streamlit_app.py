import streamlit as st
import pandas as pd
import numpy as np

# Title and Description
st.title("Hello! Welcome to Career Compass")
st.info("We help you decide what you should study in the future with the help of our large datasets and accurate algorithms.")

# Subheader for Instructions
st.subheader("Try and answer as accurately as possible! Don't worry these questions are helping you, not deciding your future.")

# User Inputs
preferred_environment = st.selectbox(
    "What is your preferred work environment?",
    ("Teaching and Training", "Remote/Work from Home", "On-site Industrial Work", "Desk Job", 
     "Fieldwork", "Research Lab", "Creative Studio")
)
salary_expect = st.slider(
    "How much annual income do you expect from your job in the future? (INR)", 
    400000, 1500000, step=50000
)

# Original Data and Additional Data
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

# Weighted Decision Matrix
student_input = {
    "Logical Thinking": 0.8, "Creativity": 0.6, "Time Management": 0.7, "Critical Thinking": 0.9,
    "Adaptability": 0.8, "Machine Learning": 0.5, "Hardware Design": 0.4, "Accounting/Finance": 0.6,
    "Legal Research": 0.5, "Cooking": 0.3, "Acting": 0.2, "DIY Projects": 0.4,
    "Research-Oriented": 0.9, "High-pressure Environment": 0.7, "Creative Freedom": 0.8,
    "Mathematics Score": 1.0, "Science Score": 0.9, "Literature Score": 0.7, "Social Science Score": 0.6
}
weighted_df = df.copy()
for attr, weight in student_input.items():
    weighted_df.loc[weighted_df["Attribute"] == attr, fields] *= weight

# Ideal and Negative Ideal Solutions
ideal_solution = weighted_df[fields].max()
negative_ideal_solution = weighted_df[fields].min()
separation_ideal = np.sqrt(((weighted_df[fields] - ideal_solution) ** 2).sum(axis=0))
separation_negative = np.sqrt(((weighted_df[fields] - negative_ideal_solution) ** 2).sum(axis=0))
relative_closeness = separation_negative / (separation_ideal + separation_negative)
ranking = relative_closeness.sort_values(ascending=False)

# Display Rankings
st.subheader("Top Career Recommendations")
for field, score in ranking.items():
    st.write(f"{field}: {score:.2f}")
