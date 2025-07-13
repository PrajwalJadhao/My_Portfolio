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

#Main title and Intro
st.title("Hi, I'm Prajwal Jadhao")
st.subheader("Data Analyst | Power BI Developer | Python Enthusiast")
st.write("Welcome to my portfolio website built with Streamlit.")


#Sidebar content
with st.sidebar:
    st.image(profile_pic, width=200)
    st.markdown("📄[Download Resume](resume.pdf)", unsafe_allow_html=True)
    st.markdown("📧 jadhaoprajwal054@gmail.com")
    st.markdown("🔗 https://www.linkedin.com/in/prajwal-jadhao-bb2a54298/")

#Skills section    
st.header("Skills")
st.markdown("""
- **Languages**: Python, SQL, Java, C#
- **Tools**: Power BI, Excel, Power Platform
- **Libraries**: Pandas, NumPy, Matplotlib, Streamlit
- **Concepts**: Data Cleaning, Visualization, Reporting, Entity Framework Core                
 """)

#Projects section    
st.header("Projects")
for project in projects:
    st.subheader(project["title"])
    st.write(project["description"])
    st.write("---")
        
#Footer
st.write("Made with ❤️ by Prajwal Jadhao using Streamlit.")