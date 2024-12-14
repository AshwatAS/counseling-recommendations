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
    "Math": [0.37454,0.02058,0.21185,0.30754,0.12204,0.06958,0.38868,0.17224,0.1631,0.11959,0.03143,0.08975,0.00744,0.41741,0.06245,0.30827,0.36778,0.27756,0.34107,0.0931,0.54203,0.54873,0.85761,0.79481,0.74046,0.29445,0.61501,0.80936,0.89001,0.0305,0.05168,0.43897,0.54923,0.35597,0.49162,0.50314,0.38817,0.10078,0.91816,0.99051,0.70312,0.81931,0.79158,0.84299,0.68484,0.87715,0.11753,0.01215,0.6294,0.45566,0.69816,0.61342,0.59413,0.8129,0.95405,0.52016,0.70408,0.51399,0.45914,0.13883,0.16894,0.03931,0.18452,0.71335,0.02007,0.88692,0.3561,0.77337,0.41707,0.32368,0.53259,0.76023,0.93834,0.16427,0.46268,0.1169,0.55167,0.11063,0.49395,0.15335,0.70724,0.08484,0.10285,0.2246,0.01309,0.06708,0.87553,0.37331,1,0.89997,0.20789,0.59029,0.86847,0.13936,0.27406,0.60052,0.0828,0.66367,0.33424,0.79942,0.18513,0.22121,1,0.03701,0.53949,0.4747,0.37368,0.29631,0.38635,0.94273,0.95784,0.31583,0.88875,0.72342,0.22468,0.30836,0.82582,0.61693,0.36299,0.06735,0.75826,0.42618,0.35086,0.3941,0.96862,0.69654],
    "Computer Science": [0.25071,0.26991,0.03949,0.17052,0.29518,0.27513,0.27135,0.19872,0.1233,0.41324,0.43641,0.16122,0.49609,0.22211,0.25178,0.23956,0.33231,0.01659,0.11347,0.69722,0.08414,0.6919,0.96831,0.50264,0.95393,0.3851,0.39005,0.81011,0.938,0.03735,0.83135,0.07846,0.7146,0.75785,0.47347,0.85649,0.64329,0.01822,0.79674,0.41262,0.90255,0.95006,0.98962,0.96151,0.98664,0.9584,0.84921,0.96988,0.89575,0.62013,0.5361,0.71824,0.68089,0.99972,0.60617,0.85218,0.21296,0.78365,0.98003,0.64087,0.27859,0.79941,0.20935,0.89521,0.72208,0.53711,0.98652,0.89677,0.2579,0.42544,0.05182,0.59564,0.18123,0.81457,0.30138,0.03983,0.31172,0.84645,0.54272,0.58623,0.15254,0.7389,0.00463,0.25244,0.66354,0.74996,0.95329,0.27074,0.67189,0.8557,0.02653,0.26806,1,0.83493,0.55418,0.66504,0.60315,0.33683,0.77091,0.6947,0.5419,0.68767,0.29735,0.59627,0.79072,0.52894,0.68408,0.23361,0.08941,0.64965,0.9691,0.22444,0.95565,0.49588,0.34781,0.53701,0.12887,0.28119,0.34187,0.58217,0.02459,0.45139,0.15106,0.22995,0.9766,0.48152],
    "Engineering": [0.13199,0.13244,0.29214,0.06505,0.03439,0.3395,0.12874,0.00552,0.3309,0.46079,0.31436,0.1297,0.318,0.11987,0.29725,0.14489,0.43353,0.51209,0.32469,0.60042,0.16163,0.65196,0.99367,0.5769,0.91486,0.85114,0.14008,0.86707,0.37558,0.8226,0.54064,0.02535,0.6602,0.01439,0.1732,0.65869,0.45825,0.09444,0.62894,0.87202,0.80525,0.95061,0.99121,0.61822,0.77427,0.72422,0.74604,0.74316,0.75454,0.67738,0.70953,0.93273,0.96991,0.99664,0.72864,0.55191,0.13637,0.39654,0.49262,0.18188,0.17701,0.6279,0.37047,0.51168,0.21145,0.58684,0.60577,0.88023,0.17089,0.50761,0.3366,0.47158,0.0665,0.6652,0.74761,0.62771,0.24849,0.82749,0.2518,0.50589,0.57629,0.12466,0.3335,0.14086,0.17804,0.20991,0.82439,0.644,0.91971,0.99022,0.98144,0.82415,0.99455,0.3844,0.55142,0.17537,0.24535,0.43257,0.1066,0.27215,0.37295,0.74406,0.9244,0.23001,0.31875,0.93907,0.76827,0.04209,0.41758,0.60774,1,0.22382,0.36213,0.08105,0.67802,0.69747,0.33512,0.63181,0.63262,0.34588,0.02212,0.16362,0.43233,0.2131,0.97092,0.11732],
    "Medicine": [0.59866,0.21234,0.36636,0.34889,0.70932,0.69483,0.15675,0.41546,0.06356,0.56128,0.50857,0.40812,0.11005,0.33762,0.30088,0.48945,0.53577,0.2265,0.77734,0.6331,0.79855,0.22427,0.86772,0.69252,0.37016,0.31692,0.51833,0.91324,0.99398,0.36019,0.63743,0.36265,0.87993,0.81607,0.83385,0.96293,0.54562,0.88301,0.47747,0.77641,0.42646,0.47344,0.49442,0.10112,0.37064,0.60635,0.58337,0.69114,0.62756,0.18812,0.3138,0.36606,0.34212,0.35543,0.3717,0.36094,0.31454,0.22209,0.32875,0.34567,0.0887,0.08176,0.98452,0.53211,0.9275,0.84544,0.23723,0.52451,0.66864,0.24241,0.13441,0.41184,0.94112,0.52307,0.30272,0.33491,0.24395,0.39729,0.3457,0.81145,0.40672,0.92084,0.39817,0.17639,0.96107,0.49805,0.44076,0.40873,0.80411,0.99718,0.98304,0.40941,0.79986,0.52569,0.82974,0.91441,0.3893,0.21494,0.97514,0.59023,0.73222,0.83943,0.97106,0.12057,0.62589,0.79878,0.41777,0.01787,0.27912,1,0.62775,0.53697,0.80952,0.62018,0.56573,0.68014,0.74351,0.9598,0.93203,0.99092,0.82361,0.39481,0.54362,0.03113,0.64478,0.62519],
    "Arts": [0.75602,0.88182,0.75607,0.96563,0.65878,0.7979,0.58093,0.90686,0.81098,0.77097,0.70757,0.6334,0.92794,0.94291,0.98484,0.98565,0.89029,0.64517,0.25794,0.33903,0.99643,0.71218,0.2652,0.19524,0.01546,0.16949,0.87737,0.51134,0.57828,0.12706,0.72609,0.99598,0.65487,0.046,0.3985,0.07057,0.94146,0.07119,0.73507,0.3408,0.02005,0.03184,0.05756,0.08411,0.8128,0.1112,0.06217,0.0277,0.08431,0.0637,0.08473,0.24522,0.03833,0.06899,0.01813,0.27665,0.35059,0.86236,0.6334,0.89679,0.12064,0.87358,0.61825,0.60717,0.11976,0.43166,0.10178,0.4104,0.92938,0.91484,0.76337,0.54887,0.57447,0.95883,0.93221,0.83927,0.03353,0.7973,0.1816,0.01811,0.42413,0.8699,0.5374,0.49837,0.14866,0.20514,0.40076,0.92539,0.79992,0.66809,0.42142,0.55205,0.02521,0.97168,0.99992,1,0.88869,0.03118,0.72819,0.36097,0.99656,0.70558,0.14427,0.07695,0.48598,1,0.42136,0.98772,0.94473,0.23067,0.99491,0.59294,0.85524,0.68326,0.26703,0.61861,0.16076,0.63401,0.10251,0.04574,0.48864,0.69368,0.41973,0.75167,0.06102,0.88557],
    "Business": [0.45991,0.3534,0.03514,0.05084,0.19252,0.32187,0.1427,0.12901,0.12518,0.0538,0.11929,0.67146,0.12711,0.1232,0.03689,0.14206,0.3353,0.17437,0.15998,0.64921,0.8092,0.93725,0.84399,0.99245,0.92832,0.5568,0.24077,0.70152,0.83594,0.72224,0.77585,0.7597,0.7379,0.94073,0.71585,0.74242,0.5861,0.61898,0.60348,0.93076,0.59552,0.59845,0.54953,0.70097,0.59725,0.59263,0.7187,0.71296,0.50116,0.40335,0.16262,0.02637,0.03869,0.13477,0.35816,0.60348,0.68992,0.64952,0.24015,0.27396,0.56078,0.32087,0.76891,0.14741,0.59053,0.22758,0.15286,0.35238,0.08676,0.1200,0.08996,1.0000,0.14183,0.5772,0.39957,0.69403,0.56989,0.14992,0.90845,0.67212,0.99644,0.49884,0.41986,0.31893,0.31462,0.19069,0.35964,0.45615,0.87854,0.20498,0.39267,0.13613,0.32247,0.17231,0.011,0.18314,0.75567,0.26226,0.49549,0.49158,0.35878,0.12525,0.88421,1,0.98586,0.97071,0.13758,0.22777,0.1674,0.17653,0.1739,0.15009,0.48086,0.17613,0.17863,0.65272,0.11797,0.23999,0.13723,0.17154,0.17041,0.42077,0.13853,0.16853,0.62622,0.73031],
    "Sports Science": [0.05808,0.30424,0.19967,0.30461,0.31171,0.08849,0.14092,0.77127,0.72961,0.52273,0.41038,0.80367,0.81801,0.51879,0.60956,0.67214,0.32078,0.69094,0.81722,0.72596,0.10147,0.3254,0.97301,0.28077,0.42818,0.93615,0.69702,0.7983,0.4656,0.76999,0.5163,0.40895,0.55435,0.85546,0.63509,0.02651,0.96119,0.84488,0.28203,0.85841,0.3892,0.29321,0.44153,0.07276,0.986,0.01135,0.28571,0.0738,0.04545,0.58366,0.91093,0.37646,0.41482,0.84965,0.11356,0.13402,0.39224,0.14707,0.07586,0.66756,0.20633,0.06108,0.46253,0.53262,0.59359,0.28378,0.24596,0.11204,0.57161,0.28863,0.32235,0.83062,0.13977,0.39245,0.38389,0.62007,0.76246,0.22925,0.58339,0.93212,0.93437,0.59128,0.34635,0.91485,0.08535,0.03655,0.15524,0.71597,0.65275,0.29315,0.81744,0.29447,0.26868,0.01839,0.13689,0.51892,0.71905,0.59508,0.6884,0.91731,0.69228,0.18058,0.86204,0.33987,0.23296,0.76719,0.23878,0.38433,0.61341,0.22049,0.39624,0.09149,0.08699,0.85121,0.79743,0.15861,0.83213,0.77985,0.68789,0.97349,0.6833,0.08238,0.39759,0.86436,0.13124,0.20052																																																																																																																													
],
    "Journalism": [0.86618,0.52476,0.51423,0.09767,0.52007,0.19598,0.8022,0.07404,0.63756,0.42754,0.75555,0.18657,0.86073,0.70302,0.50268,0.76162,0.18652,0.38674,0.5552,0.89711,0.6635,0.74649,0.3931,0.02432,0.96665,0.69603,0.70248,0.64996,0.54264,0.21582,0.32296,0.17329,0.61172,0.70366,0.0453,0.58578,0.90535,0.02327,0.17744,0.42899,0.01084,0.32866,0.8877,0.82186,0.75338,0.46866,0.8686,0.55385,0.28096,0.07773,0.82254,0.81055,0.27341,0.24735,0.67157,0.02878,0.43747,0.92659,0.12888,0.17232,0.36427,0.27688,0.74747,0.24247,0.6791,0.36308,0.16068,0.39786,0.27998,0.58124,0.80987,0.96503,0.79527,0.8166,0.54355,0.53346,0.87677,0.72225,0.40085,0.56513,0.92557,0.399,0.34695,0.36239,0.99687,0.47207,0.18193,0.65892,0.23818,0.89634,0.34182,0.94845,0.54163,0.9143,0.90002,0.04697,0.29712,0.05143,0.43483,0.13682,0.8492,0.56795,0.84455,0.72477,0.0244,0.40193,0.11047,0.67965,0.16703,0.18644,0.75824,0.87746,0.40845,0.49515,0.65845,0.88087,0.50747,0.10698,0.06784,0.96888,0.4459,0.6805,0.27422,0.47321,0.03253,0.49159																																																																																																																													
],
    "Law": [0.60112,0.43195,0.59241,0.68423,0.54671,0.04523,0.07455,0.35847,0.88721,0.02542,0.2288,0.89256,0.00695,0.36363,0.05148,0.23764,0.04078,0.93673,0.52965,0.88709,0.00506,0.64963,0.89205,0.64547,0.96362,0.57006,0.35949,0.70197,0.28654,0.62289,0.79519,0.15644,0.4196,0.47417,0.37461,0.94023,0.19579,0.81447,0.75061,0.75087,0.90538,0.67252,0.35092,0.70624,0.37626,0.0563,0.2236,0.9693,0.95041,0.97439,0.9498,0.98728,0.05638,0.45054,0.52031,0.75514,0.90416,0.49212,0.12805,0.19229,0.50342,0.8062,0.03668,0.26924,0.78917,0.64592,0.18657,0.96947,0.76949,0.15436,0.25464,0.1243,0.20163,0.43913,0.90647,0.89389,0.34208,0.72004,0.46201,0.69665,0.45084,0.05476,0.7375,0.58059,0.5022,0.56484,0.86179,0.0271,0.09944,0.013,0.25942,0.76361,0.63348,0.11775,0.87389,0.16628,0.5664,0.49637,0.2464,0.95024,0.24967,0.91549,0.3191,0.06536,0.8701,0.47988,0.35462,0.21825,1,0.77958,0.69602,0.2656,0.37269,0.48059,0.85058,0.87184,0.00639,0.76103,0.30096,0.74965,0.27363,0.65451,0.98398,0.96819,0.92085,0.06421																																																																																																																													
],
    "Environmental Science": [0.70807,0.29123,0.04645,0.44015,0.18485,0.32533,0.98689,0.11587,0.47221,0.10789,0.07698,0.53934,0.51075,0.97178,0.27865,0.72822,0.59089,0.13752,0.24185,0.77988,0.16081,0.84922,0.63114,0.17711,0.85301,0.09718,0.29359,0.79579,0.59083,0.08535,0.27083,0.25024,0.24773,0.09783,0.62586,0.57547,0.06936,0.28185,0.80683,0.75454,0.09129,0.75237,0.11707,0.08135,0.0835,0.11882,0.96322,0.5231,0.89026,0.98621,0.72572,0.15042,0.86472,0.12916,0.77232,0.62031,0.34826,0.25824,0.1519,0.04087,0.69039,0.74826,0.25244,0.37728,0.49844,0.57078,0.2851,0.86551,0.18704,0.48114,0.6815,0.73087,0.16366,0.37694,0.62424,0.7886,0.82126,0.64115,0.94728,0.9225,0.11324,0.3352,0.45222,0.63226,0.59539,0.06571,0.94612,0.22197,0.24317,0.08551,0.37969,1,0.25789,0.57652,0.59741,0.73803,0.47605,0.59684,0.8191,0.44601,0.48942,1,0.82892,0.31529,0.02127,0.62751,0.28724,0.94996,0.23167,0.35013,0.1539,0.12951,0.25975,0.59241,0.86729,0.02925,0.28704,0.54127,0.70817,0.13009,0.99712,0.27326,0.40933,0.18553,0.61665,0.58197																																																																																																																													
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
