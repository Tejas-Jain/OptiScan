from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "pic4.gif"
diagnoser_tool = current_dir / "pages" / "4_🔬_Diagnoser.py"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "OptiScan | Eye disease classifier"
PAGE_ICON = ":eye:"
PAGE_COLOR="dark"
NAME = "OptiScan"
DESCRIPTION = """
Precision Diagnosis for Brighter Tomorrow & Shaping the Future of Eye Health.
"""
EMAIL = "paltushar35@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/@Tushar_zi6ei",
    "LinkedIn": "https://www.linkedin.com/in/tushar-pal-7494b5203/",
    "GitHub": "https://github.com/Tushar-r12345",
    "Twitter": "https://twitter.com/Tushar48923527",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})",unsafe_allow_html=True)


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Our Vision")
st.write(
    """
- ✔️ Eye Disease Classifier: Accurate Diagnosis for Eye Conditions
- ✔️ Empowering Eye Health: AI-Based Eye Disease Classification System
- ✔️ Enhancing Eye Care: Automated Eye Disease Classifier for Early Detection
- ✔️ Transforming Eye Healthcare: Next-Generation Eye Disease Classifier
- ✔️ Precision Eye Disease Diagnosis: Cutting-Edge Classifier Technology
- ✔️ Revolutionizing Ophthalmology: State-of-the-Art Eye Disease Classifier
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("About Us")
st.write("---")

# --- JOB 1
st.write("🧬", "**About Us**")
st.write(
    """
- ► At Eye Disease Classifiers, our mission is to revolutionize the field of ophthalmology by leveraging cutting-edge technology to provide accurate and efficient diagnosis of eye diseases. 
- ► We are passionate about improving the lives of patients and empowering eye care professionals with advanced tools for early detection and precise classification of various eye conditions.
"""
)

# --- JOB 2
st.write('\n')
st.write("🔬", "**Advanced Classification Technology**")
st.write(
    """
- ► At Eye Disease Classifiers, we have developed a sophisticated classification system that utilizes state-of-the-art algorithms and deep learning models to analyze medical imaging data. 
- ► Our advanced technology enables accurate identification and classification of various eye diseases, including conditions such as glaucoma, diabetic retinopathy, macular degeneration, and more.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚑", "**Collaborative Approach**")
st.write(
    """
- ► We believe in the importance of collaboration and actively work alongside ophthalmologists, optometrists, and other eye care professionals to ensure the highest level of accuracy and reliability in our classifiers. 
- ► By combining medical expertise with our cutting-edge technology, we strive to deliver comprehensive solutions that support healthcare providers in making informed decisions and delivering personalized patient care.
"""
)

# --- JOB 3
st.write('\n')
st.write("🩺", "**Advancing Eye Health**")
st.write(
    """
- ► Through our dedication to advancing eye health, we aim to contribute to early disease detection, timely intervention, and improved treatment outcomes. 
- ► We are committed to ongoing research and development to enhance the capabilities of our classifiers and stay at the forefront of technological advancements in the field.
- ► Join us on our journey as we strive to make a positive impact on eye health by providing accurate, reliable, and efficient eye disease classifiers.
"""
)

# Page layout
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Contact Us")
st.write("Please fill out the form below to get in touch with us.")

# Contact form fields
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
submitted = st.button("Submit")

# Form submission handling
if submitted:
    if name and email and message:
        # Perform desired action with the form data (e.g., send email, store in database, etc.)
        st.success("Thank you for your message. We will get back to you soon!")
    else:
        st.warning("Please fill in all the required fields.")



# Footer text and links
footer_text = "copyright © 2023, All rights reserved.Created by Tushar Pal (SoloDeveloper_04) ! This is prototype only"
footer_text2= "Follow us on : "
github_link = "https://github.com/Tushar-r12345"
twitter_link = "https://twitter.com/Tushar48923527"

# Display footer
# st.write("---")
# st.write(f"---\n{footer_text}\n[Twitter]({twitter_link}) | [Instagram]({instagram_link})")

st.write(footer_text)
# st.write("[Twitter](" + twitter_link + ") | [Instagram](" + instagram_link + ")")
st.write(f"---\n{footer_text2}\n[Twitter]({twitter_link})  |  [Github]({github_link})")

