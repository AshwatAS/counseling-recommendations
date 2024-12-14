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

#fields = ["Math", "Computer Science", "Engineering", "Medicine", "Arts", "Business", "Sports Science", "Journalism", "Law", "Environmental Science"]


attributes=[
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
    ]
# User Inputs
student_input = {
    attributes.index(preferred_environment): 10,
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
  student_input.setdefault(attributes.index(i)+1,10)
for i in selected_soft_skills:
  student_input.setdefault(attributes.index(i)+1,10)
for i in selected_passion_areas:
  student_input.setdefault(attributes.index(i)+1,10)
for i in selected_technical_skills:
  student_input.setdefault(attributes.index(i)+1,10)
for i in range(len(selected_subjects)):
  student_input.setdefault(attributes.index(selected_subjects[i])+1,round(grades[i]/100)*10)
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


def topsis_decision(matrix, weights):
    # Step 1: Normalize the decision matrix
    norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))

    # Step 2: Apply the weights
    weighted_matrix = norm_matrix * weights

    # Step 3: Determine ideal best and ideal worst values
    ideal_best = weighted_matrix.max(axis=0)
    ideal_worst = weighted_matrix.min(axis=0)

    # Step 4: Calculate distances to the ideal best and worst
    distance_to_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    distance_to_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

    # Step 5: Calculate the performance score
    scores = distance_to_worst / (distance_to_best + distance_to_worst)

    # Return scores
    return scores

# Main function to run the program
def run_topsis_from_csv(file_path):
    # Load the CSV file
    data = pd.read_csv("https://raw.githubusercontent.com/AshwatAS/counseling-recommendations/refs/heads/master/Logically_Adjusted_CSV_Data__Fixed_.csv")
    
    # Extract attributes and fields
    attributes = data['Unnamed: 0']
    fields = data.columns[1:]
    decision_matrix = data.iloc[:, 1:].values

    # Prompt user to select attributes dynamically
    # print("Available attributes:")
    # for idx, attr in enumerate(attributes):
    #     print(f"{idx + 1}. {attr}")

    selected_indices = []
    while True:
      
        try:
          
            #choices = input("\nEnter the numbers of the attributes you'd like to select (comma-separated): ")
            selected_indices = list(student_input.keys())
            st.write(selected_indices)
          
            if all(0 <= idx < len(attributes) for idx in selected_indices):
                break
            else:
                st.write("Invalid selection. Try again.")
        except ValueError:
            st.write("Please enter valid numbers.")

    selected_attributes = [attributes[idx] for idx in selected_indices]

    # Get skill levels for each selected attribute
    skill_levels = []
    for attr in selected_attributes:
        while True:
            try:
                level = float(input(f"Enter your skill level for {attr} (0-10): "))
                if 0 <= level <= 10:
                    skill_levels.append(level / 10)  # Normalize skill level
                    break
                else:
                    print("Skill level must be between 0 and 10.")
            except ValueError:
                print("Please enter a valid number.")

    # Map selected attributes to their rows in the decision matrix
    filtered_matrix = decision_matrix[selected_indices, :]

    # Run TOPSIS
    scores = topsis_decision(filtered_matrix.T, [1.0 for i in range(len(selected_attributes))])  # Transpose for field-wise calculation
    field_ranking = sorted(zip(fields, scores), key=lambda x: x[1], reverse=True)

    # Output results
    st.write("\nField Rankings (Best to Worst):")
    for rank, (field, score) in enumerate(field_ranking, 1):
        st.write(f"{rank}. {field} (Score: {score:.4f})")
    st.write(f"\nYour best field is: {field_ranking[0][0]}")

# Run the program
if __name__ == "__main__":
    # Replace 'your_file_path.csv' with your actual file path
    file_path = "Logically_Adjusted_CSV_Data__Fixed_.csv"
    run_topsis_from_csv(file_path)

