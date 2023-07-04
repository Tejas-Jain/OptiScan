# import streamlit as st
#
# NAME = "Make Appointment"
# st.title(NAME)
#
# st.write("---")
# # Name
# name = st.text_input("Name")
#
# # Contact
# contact = st.text_input("Contact")
#
# # Gender
# gender = st.selectbox("Gender", ["Male", "Female", "Other"])
#
# # State
# state = st.selectbox("State", ["Delhi", "Mumbai", "Chennai"])
#
# # Lab Names
# lab_names = st.selectbox("Lab Names", ["ClearView Research", "OptiVision Labs", "VisionPlus Research", "EyeExcel Labs"])
#
# def reset_state():
#     # Reset your application state here
#     # For example, you can reset variables or clear cached data
#     st.session_state.my_variable = None
#     st.session_state.my_cached_data = {}
#
# # Submit button
# submit_button = st.button("Submit")
#
# # Handling form submission
# if submit_button:
#     with st.container():
#         st.write("Appointment Details :")
#         st.write("Name : ", name)
#         st.write("Contact : ", contact)
#         st.write("Gender : ", gender)
#         st.write("State : ", state)
#         st.write("Lab Name : ", lab_names)
#
# # Form submission handling
# if submit_button:
#     if name and contact and gender and state and lab_names:
#         # Perform desired action with the form data (e.g., send email, store in database, etc.)
#         st.success("Thank you for your message. We will get back to you soon!")
#     else:
#         st.warning("Please fill in all the required fields.")


# import streamlit as st
#
# NAME = "Make Appointment"
# st.title(NAME)
#
# st.write("---")
# # Name
# name = st.text_input("Name")
#
# # Contact
# contact = st.text_input("Contact")
#
# # Gender
# gender = st.selectbox("Gender", ["Male", "Female", "Other"])
#
# # State
# state = st.selectbox("State", ["Delhi", "Mumbai", "Chennai"])
#
# # Lab Names
# lab_names = st.selectbox("Lab Names", ["ClearView Research", "OptiVision Labs", "VisionPlus Research", "EyeExcel Labs"])
#
# def reset_state():
#     # Reset your application state here
#     # For example, you can reset variables or clear cached data
#     st.session_state.name = None
#     st.session_state.contact = None
#     st.session_state.gender = None
#     st.session_state.state = None
#     st.session_state.lab_names = None
#
# # Submit button
# submit_button, reset_button = st.beta_columns([1, 1])
# if submit_button.button("Submit"):
#     with st.container():
#         st.write("Appointment Details:")
#         st.write("Name:", name)
#         st.write("Contact:", contact)
#         st.write("Gender:", gender)
#         st.write("State:", state)
#         st.write("Lab Name:", lab_names)
#
#         # Perform desired action with the form data (e.g., send email, store in database, etc.)
#         if name and contact and gender and state and lab_names:
#             st.success("Thank you for your message. We will get back to you soon!")
#         else:
#             st.warning("Please fill in all the required fields.")
#
# if reset_button.button("Reset"):
#     reset_state()
#
# # Form submission handling


import streamlit as st
from pathlib import Path


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

NAME = "Make Appointment"
st.title(NAME)

st.write("---")
# Name
name = st.text_input("Name")

# Contact
contact = st.text_input("Contact")

# Gender
gender = st.selectbox("Gender", ["Male", "Female", "Other"])

# Date
date = st.date_input("Date")

# State
state = st.selectbox("State", ["Delhi", "Mumbai", "Chennai"])

# Lab Names
lab_names = st.selectbox("Lab Names", ["ClearView Research", "OptiVision Labs", "VisionPlus Research", "EyeExcel Labs"])

def reset_state():
    # Reset your application state here
    # For example, you can reset variables or clear cached data
    st.session_state.name = None
    st.session_state.contact = None
    st.session_state.gender = None
    st.session_state.date = None
    st.session_state.state = None
    st.session_state.lab_names = None

# Submit and Reset buttons in the same line using st.columns
col1, col2 = st.columns(2)
if col1.button("Submit"):
    with st.container():
        st.write("Appointment Details:")
        st.write("Name:", name)
        st.write("Contact:", contact)
        st.write("Gender:", gender)
        st.write("Date:", date.strftime("%Y-%m-%d"))
        st.write("State:", state)
        st.write("Lab Name:", lab_names)

        # Perform desired action with the form data (e.g., send email, store in database, etc.)
        if name and contact and gender and state and lab_names:
            st.success("Thank you for your message. We will get back to you soon!")
        else:
            st.warning("Please fill in all the required fields.")

if col2.button("Reset"):
    reset_state()


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
st.write(f"\n{footer_text2}\n[Twitter]({twitter_link})  |  [Github]({github_link})")

# Form submission handling
# Increase button width using custom CSS styling
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)



