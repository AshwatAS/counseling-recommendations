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
#all the options' lists for input
hobbies = [
    "Astronomy",
    "Bird Watching",
    "Board Games",
    "Calligraphy",
    "Cooking",
    "Cycling",
    "Dance",
    "Drawing",
    "Fishing",
    "Gardening",
    "Hiking",
    "Knitting",
    "Music Composition",
    "Origami",
    "Painting",
    "Photography",
    "Pottery",
    "Reading",
    "Sculpting",
    "Woodworking",
    "Writing"
]
soft_skills = [
    "Adaptability",
    "Attention to Detail",
    "Collaboration",
    "Communication",
    "Conflict Resolution",
    "Creativity",
    "Critical Thinking",
    "Decision Making",
    "Empathy",
    "Interpersonal Skills",
    "Leadership",
    "Negotiation",
    "Problem-Solving",
    "Public Speaking",
    "Resilience",
    "Self-Motivation",
    "Stress Management",
    "Teamwork",
    "Time Management",
    "Work Ethic"
]
technical_skills = [
    "AR/VR Development",
    "Blockchain Development",
    "C++",
    "Cloud Computing",
    "Content Writing",
    "Cybersecurity",
    "Data Analysis",
    "Database Management",
    "Digital Marketing",
    "Game Design",
    "Graphic Design",
    "Java",
    "Machine Learning",
    "Mobile App Development",
    "Network Administration",
    "Python",
    "SEO",
    "Social Media Management",
    "UI/UX Design",
    "Web Development"
]
passion_areas = [
    "Automobiles",
    "Business Strategy",
    "Creative Arts",
    "Education",
    "Entrepreneurship",
    "Environmental Conservation",
    "Fashion",
    "Film & Media",
    "Fitness & Wellness",
    "Food & Culinary Arts",
    "Gaming",
    "Healthcare",
    "History & Culture",
    "Politics",
    "Science & Research",
    "Social Work",
    "Space Exploration",
    "Sports",
    "Technology",
    "Travel"
]
subjects = [
    "Accounting",
    "Anthropology",
    "Archaeology",
    "Architecture",
    "Art",
    "Biology",
    "Business Studies",
    "Chemistry",
    "Computer Science",
    "Data Science",
    "Economics",
    "Engineering",
    "English",
    "Environmental Science",
    "Ethics",
    "Geography",
    "History",
    "Law",
    "Linguistics",
    "Literature",
    "Mathematics",
    "Media Studies",
    "Medicine",
    "Music",
    "Nursing",
    "Pharmacology",
    "Philosophy",
    "Physical Education",
    "Physics",
    "Political Science",
    "Psychology",
    "Public Health",
    "Sociology",
    "Sports Science",
    "Statistics",
    "Theology",
    "Veterinary Science"
]

# Use st.multiselect for multiple selection
selected_hobbies = st.multiselect("Select one or more hobbies:", hobbies, max_selections=5)
selected_soft_skills=st.multiselect("Select one or more skills:",soft_skills)
selected_technical_skills=st.multiselect("Select one or more technical skills:",technical_skills)
selected_passion_areas=st.multiselect("Select one or more passion areas:",passion_areas, max_selections=3)
selected_subjects=st.multiselect("Select the subjects you have studied:",subjects,max_selections=9)
grades=[]
for i in selected_subjects:
  grade = st.slider(f"What was your percentage in {i}", 1, 100, step=1)
  grades.append(grade)

input_data={
  "preferred_environment": preferred_environment,
  "salary_expect": salary_expect,
  "years_for_job": time_filter,
  "hobbies": [selected_hobbies],
  "soft_skills": [selected_soft_skills],
  "technical_skills": [selected_technical_skills],
  "passion_areas": [selected_passion_areas],
  "grades": [grades]
}
input_df=pd.DataFrame(input_data,index=[0])
input_df

fields = ["Math", "Computer Science", "Engineering", "Medicine", "Arts", "Business", "Sports Science", "Journalism", "Law", "Environmental Science"]
data = {
    "Attribute": [
        "Painting", "Writing", "Photography", "Gardening", "Cooking",
        "Music Composition", "Dance", "Calligraphy", "Knitting",
        "Bird Watching", "Astronomy", "Woodworking", "Pottery",
        "Origami", "Sculpting", "Drawing", "Fishing", "Cycling",
        "Hiking", "Board Games", "Communication", "Teamwork",
        "Problem-Solving", "Leadership", "Adaptability",
        "Conflict Resolution", "Empathy", "Time Management",
        "Decision Making", "Negotiation", "Stress Management",
        "Public Speaking", "Creativity", "Collaboration",
        "Work Ethic", "Attention to Detail", "Interpersonal Skills",
        "Resilience", "Critical Thinking", "Self-Motivation", "Python",
        "Java", "C++", "Data Analysis", "Web Development",
        "Machine Learning", "Cloud Computing", "Database Management",
        "Cybersecurity", "Mobile App Development", "Network Administration",
        "Game Design", "AR/VR Development", "Robotics",
        "Blockchain Development", "Digital Marketing", "SEO",
        "Social Media Management", "Graphic Design", "UI/UX Design",
        "Teaching and Training", "Remote/Work from Home",
        "On-site Industrial Work", "Desk Job", "Fieldwork",
        "Research Lab", "Creative Studio", "Technology",
        "Creative Arts", "Sports", "Environmental Conservation",
        "Entrepreneurship", "Healthcare", "Education", "Travel",
        "Fashion", "Gaming", "Automobiles", "Social Work",
        "Science & Research", "Business Strategy", "Politics",
        "Fitness & Wellness", "Food & Culinary Arts", "Film & Media",
        "History & Culture", "Space Exploration", "Content Writing",
        "Mathematics", "Physics", "Chemistry", "Biology",
        "Computer Science", "English", "History", "Geography",
        "Economics", "Philosophy", "Psychology", "Sociology",
        "Political Science", "Environmental Science", "Statistics",
        "Business Studies", "Accounting", "Art", "Music",
        "Physical Education", "Law", "Medicine", "Engineering",
        "Literature", "Linguistics", "Anthropology", "Archaeology",
        "Ethics", "Theology", "Public Health", "Pharmacology",
        "Nursing", "Veterinary Science", "Architecture", "Media Studies",
        "Sports Science", "Data Science", "Reading"
    ],
     "Math": [0.13567, 0.23456, 0.32145, 0.12567, 0.23145, 0.22345, 0.12789, 0.10567, 0.13245, 0.13245, 0.87654, 0.65432, 0.30987, 0.34567, 0.22345, 0.34567, 0.24345, 0.34567, 0.34567, 0.13567, 0.43234, 0.27654, 0.76543, 0.34567, 0.43234, 0.34567, 0.54321, 0.65432, 0.43234, 0.31234, 0.54321, 0.65432, 0.34567, 0.54321, 0.65432, 0.76543, 0.54321, 0.43234, 0.76543, 0.65432, 0.98765, 0.87654, 0.76543, 0.54321, 0.65432, 0.76543, 0.65432, 0.54321, 0.76543, 0.54321, 0.65432, 0.43234, 0.65432, 0.76543, 0.87654, 0.54321, 0.65432, 0.54321, 0.43234, 0.65432, 0.43234, 0.54321, 0.76543, 0.54321, 0.65432, 0.76543, 0.54321, 0.87654, 0.43234, 0.54321, 0.76543, 0.54321, 0.76543, 0.43234, 0.54321, 0.43234, 0.54321, 0.76543, 0.54321, 0.87654, 0.43234, 0.65432, 0.54321, 0.43234, 0.54321, 0.65432, 0.87654, 0.43234, 0.98765, 0.87654, 0.76543, 0.76543, 0.87654, 0.54321, 0.65432, 0.54321, 0.43234, 0.54321, 0.54321, 0.43234, 0.76543, 0.67234, 0.91234, 0.41234, 0.75432, 0.35678, 0.26543, 0.54321, 0.65432, 0.54321, 0.74321, 0.23456, 0.54321, 0.65432, 0.54321, 0.76543, 0.65321, 0.43234, 0.54321, 0.76543, 0.23456, 0.74321, 0.43234, 0.43245, 0.98765, 0.54321
],
    "Computer Science": [0.05432, 0.34567, 0.20987, 0.13456, 0.13456, 0.12567, 0.15432, 0.15432, 0.10123, 0.10987, 0.23456, 0.30987, 0.13567, 0.32145, 0.13567, 0.22345, 0.13245, 0.34567, 0.23456, 0.23456, 0.64523, 0.45662, 0.98765, 0.54203, 0.34567, 0.43234, 0.65432, 0.54321, 0.86751, 0.43234, 0.55664, 0.54321, 0.23456, 0.43234, 0.86532, 0.92056, 0.65432, 0.54321, 0.76543, 0.54321, 0.87654, 0.98765, 0.87654, 0.65432, 0.76543, 0.98765, 0.76543, 0.65432, 0.76543, 0.43234, 0.54321, 0.54321, 0.76543, 0.98765, 0.98765, 0.43234, 0.54321, 0.43234, 0.54321, 0.76543, 0.54321, 0.43234, 0.54321, 0.43234, 0.76543, 0.65432, 0.43234, 0.98765, 0.54321, 0.43234, 0.65432, 0.43234, 0.54321, 0.75684, 0.43234, 0.54321, 0.76543, 0.75624, 0.43234, 0.98765, 0.54321, 0.43234, 0.43234, 0.54321, 0.65432, 0.54321, 0.98765, 0.54321, 0.94562, 0.98765, 0.76543, 0.54321, 0.99877, 0.43234, 0.54321, 0.43234, 0.54321, 0.43234, 0.43234, 0.54321, 0.54321, 0.43567, 0.93456, 0.92345, 0.61234, 0.21345, 0.34567, 0.43245, 0.54321, 0.75432, 0.87654, 0.23456, 0.54321, 0.32145, 0.23456, 0.43245, 0.42345, 0.65432, 0.87654, 0.54321, 0.34567, 0.65432, 0.32145, 0.54321, 0.98456, 0.43245
],
    "Engineering": [0.11458, 0.21345, 0.13245, 0.28976, 0.21567, 0.13456, 0.21789, 0.11432, 0.12145, 0.11234, 0.95673, 0.97543, 0.43654, 0.21345, 0.43245, 0.21789, 0.42123, 0.56789, 0.76543, 0.27654, 0.34567, 0.51234, 0.87654, 0.45678, 0.56432, 0.56789, 0.53245, 0.65432, 0.23456, 0.34567, 0.23456, 0.65432, 0.43234, 0.76543, 0.54321, 0.65432, 0.43234, 0.34567, 0.65432, 0.43234, 0.76543, 0.65432, 0.76543, 0.76543, 0.54321, 0.87654, 0.54321, 0.76543, 0.65432, 0.65432, 0.76543, 0.65432, 0.87654, 0.87654, 0.76543, 0.54321, 0.76543, 0.54321, 0.65432, 0.76543, 0.43234, 0.54321, 0.65432, 0.43234, 0.76543, 0.87654, 0.54321, 0.76543, 0.43234, 0.65432, 0.43234, 0.54321, 0.43234, 0.43234, 0.54321, 0.76543, 0.87654, 0.98765, 0.54321, 0.87654, 0.65432, 0.54321, 0.76543, 0.43234, 0.43234, 0.43234, 0.76543, 0.43234, 0.76543, 0.87654, 0.65432, 0.43234, 0.76543, 0.54321, 0.43234, 0.65432, 0.76543, 0.54321, 0.76543, 0.43234, 0.54321, 0.6789, 0.45321, 0.65432, 0.32145, 0.43234, 0.13245, 0.65432, 0.23654, 0.65432, 0.98765, 0.34234, 0.65432, 0.56789, 0.43245, 0.54321, 0.43234, 0.54321, 0.54321, 0.43245, 0.54321, 0.76543, 0.43245, 0.76543, 0.54321, 0.54321
],
    "Medicine": [0.07634, 0.10234, 0.11234, 0.62345, 0.91234, 0.21567, 0.34678, 0.12567, 0.21567, 0.34567, 0.38765, 0.43245, 0.34567, 0.14567, 0.21567, 0.13456, 0.34567, 0.34567, 0.52345, 0.21567, 0.21345, 0.43234, 0.94567, 0.53245, 0.47654, 0.34567, 0.76543, 0.54321, 0.54321, 0.24567, 0.65432, 0.34567, 0.54321, 0.54321, 0.76543, 0.43234, 0.76543, 0.76543, 0.43234, 0.65432, 0.43234, 0.34567, 0.43234, 0.87654, 0.43234, 0.54321, 0.43234, 0.65432, 0.54321, 0.76543, 0.43234, 0.54321, 0.43234, 0.54321, 0.43234, 0.65432, 0.43234, 0.76543, 0.54321, 0.54321, 0.76543, 0.43234, 0.43234, 0.65432, 0.43234, 0.76543, 0.43234, 0.43234, 0.76543, 0.76543, 0.87654, 0.76543, 0.98765, 0.76543, 0.43234, 0.43234, 0.43234, 0.43234, 0.87654, 0.76543, 0.43234, 0.76543, 0.54321, 0.65432, 0.54321, 0.76543, 0.54321, 0.76543, 0.54321, 0.76543, 0.98765, 0.98765, 0.43234, 0.43234, 0.76543, 0.54321, 0.54321, 0.76543, 0.87654, 0.76543, 0.65432, 0.76234, 0.43245, 0.58976, 0.42123, 0.56345, 0.65432, 0.76543, 0.43245, 0.98432, 0.76543, 0.24345, 0.43245, 0.43245, 0.76543, 0.65432, 0.54321, 0.87654, 0.43245, 0.65432, 0.76543, 0.54321, 0.76543, 0.65432, 0.65432, 0.4
],
    "Arts": [0.92745, 0.85673, 0.76522, 0.34789, 0.34657, 0.76548, 0.92456, 0.93987, 0.85987, 0.12456, 0.01243, 0.37654, 0.89765, 0.91654, 0.91234, 0.91234, 0.01234, 0.01245, 0.12434, 0.35678, 0.43234, 0.53456, 0.54321, 0.65432, 0.54321, 0.43234, 0.87654, 0.65432, 0.24578, 0.43234, 0.76543, 0.54321, 0.87654, 0.65432, 0.54321, 0.54321, 0.65432, 0.54321, 0.65432, 0.76543, 0.54321, 0.43234, 0.56445, 0.54321, 0.65432, 0.54321, 0.54321, 0.43234, 0.43234, 0.45235, 0.42568, 0.76543, 0.54321, 0.65432, 0.31256, 0.76543, 0.65432, 0.87654, 0.98765, 0.98765, 0.54321, 0.65432, 0.54321, 0.54321, 0.54321, 0.43234, 0.98765, 0.54321, 0.98765, 0.43234, 0.54321, 0.76543, 0.43234, 0.54321, 0.76543, 0.87654, 0.65432, 0.21245, 0.43234, 0.54321, 0.76543, 0.43234, 0.76543, 0.98765, 0.98765, 0.87654, 0.01245, 0.76543, 0.43234, 0.54321, 0.03545, 0.02454, 0.54321, 0.98765, 0.87654, 0.76543, 0.65432, 0.76543, 0.65432, 0.43234, 0.76543, 0.56234, 0.04568, 0.43568, 0.12344, 0.98432, 0.87234, 0.23456, 0.43567, 0.1234, 0.34567, 0.65432, 0.43245, 0.31234, 0.23456, 0.54321, 0.65432, 0.34558, 0.23456, 0.46587, 0.43556, 0.54321, 0.54321, 0.54321, 0.46787, 0.23456
],
    "Business": [0.01234, 0.34568, 0.23155, 0.12466, 0.34654, 0.34621, 0.34597, 0.34678, 0.24655, 0.43245, 0.23456, 0.56985, 0.23556, 0.42345, 0.52345, 0.46789, 0.34497, 0.23558, 0.25646, 0.51234, 0.76543, 0.67234, 0.65432, 0.75432, 0.41234, 0.34567, 0.45678, 0.43234, 0.65432, 0.54321, 0.34567, 0.76543, 0.54321, 0.43234, 0.34567, 0.65432, 0.76543, 0.43234, 0.87654, 0.54321, 0.65432, 0.54321, 0.43234, 0.65432, 0.87654, 0.76543, 0.65432, 0.54321, 0.54321, 0.76543, 0.76543, 0.43234, 0.54321, 0.76543, 0.65432, 0.87654, 0.76543, 0.76543, 0.43234, 0.76543, 0.65432, 0.54321, 0.65432, 0.76543, 0.43234, 0.54321, 0.54321, 0.76543, 0.54321, 0.54321, 0.43234, 0.87654, 0.54321, 0.76543, 0.54321, 0.76543, 0.76543, 0.76543, 0.54321, 0.76543, 0.98765, 0.65432, 0.87654, 0.54321, 0.76543, 0.65432, 0.54321, 0.65432, 0.65432, 0.76543, 0.54321, 0.65432, 0.65432, 0.54321, 0.65432, 0.23487, 0.98765, 0.23149, 0.46451, 0.48715, 0.76543, 0.11355, 0.54321, 0.91234, 0.92345, 0.24567, 0.65432, 0.65432, 0.76543, 0.54321, 0.65432, 0.34567, 0.76543, 0.423578, 0.65432, 0.54321, 0.87654, 0.42121, 0.76543, 0.24872, 0.23487, 0.76543, 0.76543, 0.76543, 0.87654, 0.24654
],
    "Sports Science": [0.09673, 0.21789, 0.21567, 0.93876, 0.61789, 0.01245, 0.75421, 0.12435, 0.34597, 0.87541, 0.13456, 0.45618, 0.32345, 0.26789, 0.39876, 0.35678, 0.93234, 0.73245, 0.84567, 0.45678, 0.56789, 0.76543, 0.76234, 0.34567, 0.56789, 0.52345, 0.34567, 0.76543, 0.43234, 0.65432, 0.54321, 0.34567, 0.76543, 0.65432, 0.43234, 0.76543, 0.65432, 0.76543, 0.76543, 0.76543, 0.76543, 0.65432, 0.76543, 0.76543, 0.54321, 0.65432, 0.65413, 0.42156, 0.76543, 0.34877, 0.45789, 0.34561, 0.76543, 0.43234, 0.54321, 0.54321, 0.43234, 0.65432, 0.76543, 0.65432, 0.43234, 0.76543, 0.54321, 0.43234, 0.76543, 0.65432, 0.76543, 0.65432, 0.76543, 0.76543, 0.54321, 0.43234, 0.43234, 0.43234, 0.65432, 0.32455, 0.34878, 0.24255, 0.76543, 0.54321, 0.24311, 0.23456, 0.54321, 0.76543, 0.54321, 0.54321, 0.34678, 0.45112, 0.76543, 0.65432, 0.76543, 0.54321, 0.76543, 0.76543, 0.54321, 0.76543, 0.43234, 0.76543, 0.76543, 0.65432, 0.43234, 0.76543, 0.34234, 0.36789, 0.12345, 0.34567, 0.25432, 0.98765, 0.34234, 0.54321, 0.87654, 0.76345, 0.34567, 0.76543, 0.87654, 0.76543, 0.43245, 0.98765, 0.65432, 0.12489, 0.54321, 0.74551, 0.87654, 0.98765, 0.54321, 0.76543
],
    "Journalism": [0.45123, 0.91234, 0.84523, 0.34234, 0.52345, 0.86789, 0.76543, 0.81234, 0.19876, 0.54795, 0.57689, 0.43234, 0.62345, 0.63456, 0.45671, 0.84567, 0.43245, 0.52345, 0.43245, 0.34567, 0.59876, 0.24567, 0.34567, 0.56789, 0.65432, 0.67234, 0.41234, 0.65432, 0.34567, 0.23456, 0.43234, 0.43234, 0.41234, 0.43234, 0.34567, 0.54321, 0.54321, 0.65432, 0.43234, 0.54321, 0.12554, 0.35465, 0.23456, 0.43234, 0.43234, 0.43234, 0.34567, 0.43234, 0.43234, 0.43234, 0.54321, 0.65432, 0.43234, 0.54321, 0.43234, 0.43234, 0.54321, 0.54321, 0.65432, 0.43234, 0.76543, 0.43234, 0.76543, 0.76543, 0.65432, 0.43234, 0.65432, 0.54321, 0.54321, 0.65432, 0.65432, 0.65432, 0.76543, 0.76543, 0.76543, 0.65432, 0.43234, 0.54321, 0.76543, 0.43234, 0.54321, 0.76543, 0.43234, 0.65432, 0.76543, 0.43234, 0.65432, 0.76543, 0.43234, 0.43234, 0.54321, 0.43234, 0.54321, 0.65432, 0.43234, 0.65432, 0.76543, 0.43234, 0.54321, 0.76543, 0.54321, 0.56789, 0.76543, 0.54321, 0.64321, 0.87654, 0.93234, 0.76543, 0.93234, 0.54321, 0.54321, 0.65432, 0.93234, 0.76543, 0.65432, 0.32145, 0.76543, 0.76543, 0.54321, 0.65432, 0.87654, 0.65432, 0.54321, 0.76543, 0.43234, 0.54321
],
    "Law": [0.20987, 0.42345, 0.31234, 0.21234, 0.32567, 0.31234, 0.42123, 0.18765, 0.12567, 0.23456, 0.12567, 0.24567, 0.23456, 0.16543, 0.23654, 0.32345, 0.12567, 0.43245, 0.21345, 0.18976, 0.75548, 0.42345, 0.65475, 0.65482, 0.34567, 0.45051, 0.54321, 0.34567, 0.466789, 0.76543, 0.54321, 0.86578, 0.54321, 0.56789, 0.86455, 0.43234, 0.43234, 0.23456, 0.65447, 0.65432, 0.43234, 0.76543, 0.54321, 0.54321, 0.65432, 0.65432, 0.43234, 0.76543, 0.54321, 0.54321, 0.76543, 0.76543, 0.65432, 0.76543, 0.65432, 0.65432, 0.76543, 0.43234, 0.43234, 0.76543, 0.65432, 0.76543, 0.65488, 0.75881, 0.76543, 0.54321, 0.43234, 0.76543, 0.43234, 0.76543, 0.54321, 0.76543, 0.43234, 0.87264, 0.54321, 0.54321, 0.54321, 0.65432, 0.43234, 0.65784, 0.65432, 0.87654, 0.54321, 0.43234, 0.43234, 0.87615, 0.43234, 0.43234, 0.76543, 0.76543, 0.76543, 0.65432, 0.76543, 0.54321, 0.86748, 0.54321, 0.54321, 0.76543, 0.76543, 0.54321, 0.79846, 0.21234, 0.53678, 0.43245, 0.57884, 0.62345, 0.54321, 0.64788, 0.99999, 0.65432, 0.32145, 0.54774, 0.23456, 0.54321, 0.43234, 0.78441, 0.54321, 0.35611, 0.76543, 0.54321, 0.54321, 0.76543, 0.75988, 0.54321, 0.76543, 0.94515
],
    "Environmental Science": [0.31567, 0.63123, 0.43789, 0.83245, 0.84234, 0.3218, 0.32145, 0.45678, 0.51234, 0.87955, 0.72345, 0.465711, 0.56789, 0.36789, 0.62345, 0.52345, 0.72345, 0.65432, 0.84567, 0.23456, 0.34567, 0.54321, 0.43234, 0.43234, 0.34567, 0.45321, 0.32145, 0.56789, 0.54321, 0.34567, 0.76543, 0.54321, 0.76543, 0.65432, 0.54321, 0.34567, 0.54321, 0.34567, 0.65432, 0.43234, 0.1244, 0.23445, 0.24554, 0.45877, 0.55412, 0.34677, 0.45977, 0.43234, 0.65432, 0.76543, 0.65432, 0.54321, 0.45787, 0.65432, 0.45784, 0.43234, 0.43234, 0.65432, 0.54579, 0.54321, 0.54321, 0.43234, 0.76543, 0.65432, 0.65432, 0.76543, 0.76543, 0.54321, 0.76543, 0.43234, 0.98765, 0.54321, 0.65432, 0.54321, 0.43234, 0.76543, 0.65432, 0.76543, 0.65432, 0.98765, 0.54321, 0.54321, 0.65432, 0.76543, 0.54321, 0.43234, 0.76543, 0.54321, 0.54321, 0.54321, 0.65432, 0.76543, 0.65432, 0.43234, 0.43234, 0.43234, 0.65432, 0.54321, 0.65432, 0.43234, 0.54321, 0.97856, 0.43234, 0.54234, 0.31456, 0.76543, 0.48765, 0.45678, 0.67234, 0.93234, 0.76543, 0.23456, 0.54321, 0.87654, 0.54321, 0.43245, 0.76543, 0.65432, 0.94321, 0.76543, 0.65432, 0.54321, 0.65432, 0.43234, 0.54321, 0.43245
]	
}

df = pd.DataFrame(data)

# User Inputs
student_input = {
    preferred_environment: 1.0,
    # "Logical Thinking": 0.8,
    # "Creativity": 0.6,
    # "Time Management": 0.7,
    # "Critical Thinking": 0.9,
    # "Adaptability": 0.8,
    # "Machine Learning": 0.5,
    # "Hardware Design": 0.4,
    # "Accounting/Finance": 0.6,
    # "Legal Research": 0.5,
    # "Cooking": 0.3,
    # "Acting": 0.2,
    # "DIY Projects": 0.4,
    # "Research-Oriented": 0.9,
    # "High-pressure Environment": 0.7,
    # "Creative Freedom": 0.8,
    # "Mathematics Score": 1.0,
    # "Science Score": 0.9,
    # "Literature Score": 0.7,
    # "Social Science Score": 0.6
}
for i in selected_hobbies:
  student_input.setdefault(i,1.0)
for i in selected_soft_skills:
  student_input.setdefault(i,1.0)
for i in selected_passion_areas:
  student_input.setdefault(i,1.0)
for i in selected_technical_skills:
  student_input.setdefault(i,1.0)
for i in range(len(selected_subjects)):
  student_input.setdefault(selected_subjects[i],grades[i]/100)
# Add Salary Data (Estimates based on current market conditions in INR)
salaries = {
    "Math": 600000,
    "Computer Science": 1200000,
    "Engineering": 800000,
    "Medicine": 1500000,
    "Arts": 400000,
    "Business": 900000,
    "Sports Science": 500000,
    "Journalism": 450000,
    "Law": 950000
}

# Add Years to Land a Job
years_to_land = {
    "Math": 5,
    "Computer Science": 4,
    "Engineering": 4,
    "Medicine": 8,
    "Arts": 4,
    "Business": 5,
    "Sports Science": 4,
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

# Filter Jobs based on Time and Salary
def filter_jobs(time_filter, salary_filter):
    filtered_jobs = []
    for idx, field in enumerate(ranking.index):
        # Ensure the field is in salaries and years_to_land dictionaries
        if field in salaries and field in years_to_land:
            if idx == 0:  # Always include the top-ranked job
                filtered_jobs.append((field, True))  # Mark as "best field"
            elif len(filtered_jobs) - 1 < 3:  # Ensure at least 3 additional jobs
                if years_to_land[field] <= time_filter and salaries[field] >= salary_filter:
                    filtered_jobs.append((field, False))  # Regular fields
    return filtered_jobs

# Display Rankings and Apply Filters
# def display_rankings_and_filters(time_filter, salary_filter):
#   st.title("Career Recommendations")
#   st.write("### Ranked Fields (TOPSIS):")
#   for field, score in ranking.items():
#       st.write(f"{field}: {score:.2f}")
  
#   st.write("### Filtered Fields:")
#   filtered = filter_jobs(time_filter, salary_filter)
#   if len(filtered) == 1:  # Only the best field is present
#       st.write("No fields match the given filters.")
#       st.write(f"**Best Field:** {filtered[0][0]} - Salary ₹{salaries[filtered[0][0]]}, Years to Land {years_to_land[filtered[0][0]]}")
#   else:
#       for job, is_best in filtered:
#           if is_best:
#               st.write(f"**{job} (Best Field):** Salary ₹{salaries[job]}, Years to Land {years_to_land[job]}")
#           else:
#               st.write(f"{job}: Salary ₹{salaries[job]}, Years to Land {years_to_land[job]}")
    # st.write("### Ranked Fields (TOPSIS):")
    # for field, score in ranking.items():
    #     st.write(f"{field}: {score:.2f}")
    
    # st.write("### Filtered Fields:")
    # filtered = filter_jobs(time_filter, salary_filter)
    # if len(filtered) == 1:  # Only the best field is present
    #     st.write("No fields match the given filters.")
    #     st.write(f"**Best Field:** {filtered[0][0]} - Salary ₹{salaries[filtered[0][0]]}, Years to Land {years_to_land[filtered[0][0]]}")
    # else:
    #     for job, is_best in filtered:
    #         if is_best:
    #             st.write(f"**{job} (Best Field):** Salary ₹{salaries[job]}, Years to Land {years_to_land[job]}")
    #         else:
    #             st.write(f"{job}: Salary ₹{salaries[job]}, Years to Land {years_to_land[job]}")

def display_rankings_and_filters(time_filter, salary_filter):
    st.write("Ranked Fields (TOPSIS):")
    for field, score in ranking.items():
        st.write(f"{field}: {score:.2f}")
    
    st.write("\nFiltered Fields:")
    filtered = filter_jobs(time_filter, salary_filter)
    if len(filtered) == 1:  # Only the best field is present
        st.write("No fields match the given filters.")
        st.write(f"Best Field: {filtered[0][0]}: Salary ₹{salaries[filtered[0][0]]}, Years to Land {years_to_land[filtered[0][0]]}")
    else:
        for job, is_best in filtered:
            if is_best:
                st.write(f"{job} (Best Field): Salary ₹{salaries[job]}, Years to Land {years_to_land[job]}")
            else:
                st.write(f"{job}: Salary ₹{salaries[job]}, Years to Land {years_to_land[job]}")

# Example Usage
time_filter = time_filter  # Example input for max years to land a job
salary_filter = salary_expect  # Example input for min salary

display_rankings_and_filters(time_filter, salary_filter)
