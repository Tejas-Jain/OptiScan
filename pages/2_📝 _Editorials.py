from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "pic5.gif"
profile_pic2 = current_dir / "assets" / "pic7.gif"
profile_pic3 = current_dir / "assets" / "pic10.png"
profile_pic4 = current_dir / "assets" / "pic9.png"

NAME = "Cataract"
DESCRIPTION = """
A cataract is a clouding of the natural lens inside the eye, which leads to a decrease in vision. 
"""
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

SOCIAL_MEDIA = {
    "Healthline": "https://www.healthline.com/health/cataract",
    "WebMD": "https://www.webmd.com/eye-health/cataracts/what-are-cataracts",
    "MSD ": "https://www.msdmanuals.com/en-in/professional/eye-disorders/cataract/cataract",
}



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Enlightenment")
st.write("----")
st.write(
    """
- ✔️ Blurred or cloudy vision in eye sight
- ✔️ Sensitivity to glare, especially in bright sunlight or while driving at night
- ✔️ Enhancing Eye Care: Automated Eye Disease Classifier for Early Detection
- ✔️ Aging: Cataracts are more common in older adults
- ✔️ Smoking and excessive alcohol consumption
- ✔️ Surgery involves removing the cloudy lens and replacing it with an artificial intraocular lens (IOL) implant.
- ✔️ Maintain a healthy lifestyle, including regular exercise and a proper balanced diet.
"""
)
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')


NAME = "Diabetic Retinopathy"
DESCRIPTION = """
Diabetic retinopathy is a complication of diabetes that affects the blood vessels in the retina. 
"""
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic2 = Image.open(profile_pic2)

SOCIAL_MEDIA = {
    "Mayo Clinic": "https://www.mayoclinic.org/diseases-conditions/diabetic-retinopathy/symptoms-causes/syc-20371611",
    "Medscape": "https://emedicine.medscape.com/article/1225122-overview",
    "NHS": "https://www.nhs.uk/conditions/diabetic-retinopathy/",
}



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic2, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Enlightenment")
st.write("----")
st.write(
    """
- ✔️ Diabetic retinopathy occurs due to long-term high blood sugar levels associated with diabetes
- ✔️ Poorly controlled blood sugar levels and high blood pressure
- ✔️ Proper diabetes management is crucial in preventing or slowing the progression of diabetic retinopathy
- ✔️ Regular eye examinations are important, especially for individuals with diabetes, to detect and monitor any changes in the retina
- ✔️ Treatment options for diabetic retinopathy may include laser therapy to seal leaking blood vessels
- ✔️ injections of medication into the eye to reduce abnormal blood vessel growth, or in severe cases, surgery
"""
)

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')



NAME = "Glaucoma"
DESCRIPTION = """
Glaucoma refers to a group of eye conditions that can damage the optic nerve, often due to increased pressure within the eye
"""
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic3 = Image.open(profile_pic3)

SOCIAL_MEDIA = {
    "Healthline": "https://www.healthline.com/health/glaucoma",
    "Webmd": "https://www.webmd.com/eye-health/glaucoma-eyes",
    "MedlinePlus": "https://medlineplus.gov/ency/article/001620.htm",
}



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic3, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Enlightenment")
st.write("----")
st.write(
    """
- ✔️ It can cause gradual vision loss and, if left untreated, can lead to permanent blindness.
- ✔️ In the early stages, glaucoma may not cause noticeable symptoms. It often progresses slowly and painlessly.
- ✔️ Loss of peripheral (side) vision, often unnoticed until significant vision loss has occurred
- ✔️ Tunnel vision, where only a small central area of vision remains
- ✔️ Treatment options may include eye drops to reduce IOP, oral medications, laser therapy, or surgery in more advanced cases.
- ✔️ Regular eye examinations, including measurement of intraocular pressure, are crucial for early detection of glaucoma.
- ✔️ Lifestyle modifications such as regular exercise, maintaining a healthy weight
"""
)

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')


NAME = "Normal"
DESCRIPTION = """
"Normal" in the context of eye health typically refers to the absence of significant eye conditions or impairments.
"""
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic4 = Image.open(profile_pic4)

SOCIAL_MEDIA = {
    "Healthline": "https://www.healthline.com/health/how-far-can-the-human-eye-see",
    "Medline Plus": "https://medlineplus.gov/ency/imagepages/19511.htm",
    "myvision.org": "https://myvision.org/education/perfect-vision/",
}



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic4, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Enlightenment")
st.write("----")
st.write(
    """
- ✔️ Visual acuity refers to the sharpness and clarity of vision
- ✔️ In individuals with normal vision, visual acuity is typically 20/20
- ✔️ Normal vision is usually associated with healthy eyes that have no significant structural abnormalities or diseases
- ✔️ Normal color vision allows individuals to perceive a wide range of colors and distinguish between different hues and shades accurately
- ✔️ Regular eye examinations with an eye care professional or ophthalmologist are recommended to ensure optimal eye health
- ✔️ Detect any changes in vision or underlying eye conditions
- ✔️ Individuals with normal vision do not have significant refractive errors or require corrective eyewear to achieve clear vision
"""
)


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


# Footer text and links
footer_text = "copyright © 2023, All rights reserved.Created by Tushar Pal (SoloDeveloper_04) ! This is prototype only"
footer_text2= "Follow us on : "
twitter_link = "https://twitter.com/Tushar48923527"
github_link = "https://github.com/Tushar-r12345"

# Display footer
# st.write("---")
# st.write(f"---\n{footer_text}\n[Twitter]({twitter_link}) | [Instagram]({instagram_link})")

st.write(footer_text)
# st.write("[Twitter](" + twitter_link + ") | [Instagram](" + instagram_link + ")")
st.write(f"---\n{footer_text2}\n[Twitter]({twitter_link})  |  [Github]({github_link})")