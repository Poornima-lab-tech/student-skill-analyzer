import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

st.set_page_config(
    page_title="Student Skill Analyzer",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Skill Analyzer")
st.write("Analyze your skills and discover the best career path.")

data = pd.read_csv("skills_dataset.csv")

X = data[['Programming','Communication','Analytics','Projects']]
y = data['Career']

model = DecisionTreeClassifier()
model.fit(X,y)

st.subheader("Enter Your Skills")

p = st.slider("Programming Skill",1,10)
c = st.slider("Communication Skill",1,10)
a = st.slider("Analytical Skill",1,10)
pr = st.number_input("Projects Completed",0,10)

if st.button("Analyze Skills"):
    
    sample = pd.DataFrame([[p,c,a,pr]],
    columns=['Programming','Communication','Analytics','Projects'])
    
    prediction = model.predict(sample)

    st.success("Recommended Career: " + prediction[0])
