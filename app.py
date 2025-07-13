import streamlit as st 
from PIL import Image
import json

#Page Configuration
st.set_page_config(page_title = "Data Analytics Portfolio", 
                   page_icon="📊",
                   layout="wide")
#Load Image
profile_pic = Image.open("Image/PrajwalJadhaoPhoto.jpg")


#Load projects data
with open("projects.json") as f:
    projects = json.load(f) 

#Sidebar content
with st.sidebar:
    st.image(profile_pic, width= 180)
    st.markdown("## Prajwal Jadhao")
    st.markdown("## Data Analyst")
    with open("resume.pdf","rb") as file:
        st.download_button("📄Download Resume", file, file_name="Prajwal_Jadhao_Resume.pdf")
    st.write("📧 jadhaoprajwal054@gmail.com")
    st.write("🔗[LinkedIn](https://www.linkedin.com/in/prajwal-jadhao-bb2a54298/)")
    st.markdown("---")
    st.header("Skills")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Languages:** Python, SQL, Java, C#")
        st.markdown("**Libraries:** Pandas, NumPy, Matplotlib, Streamlit")
    with col2:
        st.markdown("**Tools:** Power BI,  Excel, Power Platform, Tableau")
        st.markdown("**Concepts:** Data Analysis, Data Cleaning, Data Visualization, EDA, DSA")


#Main title and Intro
st.title("Hi, I'm Prajwal Jadhao")
st.subheader("Data Analyst | Power BI Developer | Python Enthusiast")
st.write("I'm a data analyst passionate about transforming raw data into actionable insights. I build dashboards, automate reports, and solve business problems using Python, SQL, Excel, and Power BI.")

#Projects section    
st.header("📁 Projects")
for project in projects:
    col1, col2 = st.columns([1,4])
    with col1:
       if project.get("image"):
           st.image(project["image"],width=120)
    with col2:
        st.subheader(project["title"])
        st.write(project["description"])
        if project.get("link"):
            st.markdown(f"[🔗 View Project]({project['link']})")
    st.markdown("---")

#Contact
st.header("📫 Contact")
col1, col2 = st.columns(2)
with col1:
    st.write("**Email:** jadhaoprajwal054@gmail.com")
    st.write("**LinkedIn:** [linkedin.com/in/prajwal-jadhao-bb2a54298](https://www.linkedin.com/in/prajwal-jadhao-bb2a54298/)")
with col2:
    st.write("**Location:** India")
    st.write("**Open to:** Full-time roles, freeelance projects")
st.markdown("---")
st.write("Made with ❤️ using Streamlit")
       
