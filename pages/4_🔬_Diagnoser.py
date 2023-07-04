import collections
import streamlit as st
from PIL import Image
import numpy as np
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from pdfdocument.document import PDFDocument
import base64
from io import BytesIO
from pathlib import Path


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

# Define the class labels for your model
classes = ['cataract', 'diabetic_retinopathy', 'glaucoma', 'normal']


class ConvNet(nn.Module):
    def __init__(self, num_classes=4):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=12, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(num_features=12)
        self.relu1 = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2)
        self.conv2 = nn.Conv2d(in_channels=12, out_channels=20, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(num_features=20)
        self.relu2 = nn.ReLU()
        self.conv3 = nn.Conv2d(in_channels=20, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.bn3 = nn.BatchNorm2d(num_features=32)
        self.relu3 = nn.ReLU()
        self.fc = nn.Linear(in_features=75 * 75 * 32, out_features=num_classes)

    def forward(self, input):
        output = self.conv1(input)
        output = self.bn1(output)
        output = self.relu1(output)
        output = self.pool(output)
        output = self.conv2(output)
        output = self.bn2(output)
        output = self.relu2(output)
        output = self.conv3(output)
        output = self.bn3(output)
        output = self.relu3(output)
        output = output.view(-1, 32 * 75 * 75)
        output = self.fc(output)
        return output


# Load the pre-trained PyTorch model
if torch.cuda.is_available():
    model = torch.load('best_checkpoint4.model')
else:
    model = torch.load('best_checkpoint4.model', map_location=torch.device('cpu'))
# Check if the model is an OrderedDict
if isinstance(model, collections.OrderedDict):
    # If it is an OrderedDict, extract the model parameters
    model_state_dict = model
    model = ConvNet()  # Replace ConvNet with your actual model class
    model.load_state_dict(model_state_dict)
else:
    # If it's already a model object, proceed as usual
    model.eval()


# Function to preprocess the image
def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((150, 150))
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    image = transform(image).unsqueeze(0)
    return image


# Function to predict the disease
def predict_disease(image_path):
    image = preprocess_image(image_path)

    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs.data, 1)

    predicted_class = classes[predicted.item()]
    return predicted_class

def main():
    # Set the title and layout of the app
    st.title("Disease Prediction")

    # Create a file uploader widget
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    # Create input fields for name, age, gender, and blood group
    name = st.text_input("Name")
    age = st.text_input("Age")
    gender = st.text_input("Gender")
    bg = st.text_input("Blood Group")

    if uploaded_file is not None:
        # Display the selected image
        image = Image.open(uploaded_file)
        image = image.resize((300, 300))
        st.image(image, caption='Selected Image', use_column_width=True)

        # Predict the disease
        predicted_class = predict_disease(uploaded_file)

        # Display the predicted disease label
        st.subheader("Predicted Disease  :  {}".format(predicted_class))

    st.subheader("Enter Information")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Blood Group:", bg)

    # Add a "Print as PDF" button
    if st.button("Print as PDF"):
        # Create a PDF document
        pdf_buffer = BytesIO()
        pdf = PDFDocument(pdf_buffer)

        # Add the information to the PDF document
        pdf.init_report()
        pdf.h1("Predicted Disease")
        pdf.p(predicted_class)
        pdf.h1("Entered Information")
        pdf.p(f"Name: {name}")
        pdf.p(f"Age: {age}")
        pdf.p(f"Gender: {gender}")
        pdf.p(f"Blood Group: {bg}")
        pdf.generate()

        # Save the PDF file
        pdf_buffer.seek(0)
        b64_data = base64.b64encode(pdf_buffer.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64_data}" download="prediction_report.pdf">Download PDF</a>'
        st.markdown(href, unsafe_allow_html=True)


# Run the Streamlit application
if __name__ == '__main__':
    main()


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
st.write(f"{footer_text2}\n[Twitter]({twitter_link})  |  [Github]({github_link})")


# def main():
#     # Set the title and layout of the app
#     st.title("Disease Prediction")
#
#     # Create a file uploader widget
#     uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
#
#     # Create input fields for name and credentials
#     name = st.text_input("Name")
#     age = st.text_area("Age")
#     gender = st.text_area("Gender")
#     bg = st.text_area("Blood Group")
#
#     if uploaded_file is not None:
#         # Display the selected image
#         image = Image.open(uploaded_file)
#         image = image.resize((300, 300))
#         st.image(image, caption='Selected Image', use_column_width=True)
#
#         # Predict the disease
#         predicted_class = predict_disease(uploaded_file)
#
#         # Display the predicted disease label
#         st.subheader("Predicted Disease")
#         st.write(predicted_class)
#
#     st.subheader("Enter Information")
#     st.write("Name : ", name)
#     st.write("Age : ",age)
#     st.write("Gender : ", gender)
#     st.write("Blood Group : ", bg)
#
#     # # Add a "Print" button
#     # if st.button("Print"):
#     #     # Print the predicted disease and entered information
#     #     print(uploaded_file)
#     #     print("Predicted Disease:", predicted_class)
#     #     print("Name:", name)
#     #     print("Age : ", age)
#     #     print("Gender : ", gender)
#     #     print("Blood Group : ", bg)
#
#     # Add a "Print as PDF" button
#     if st.button("Print as PDF"):
#         # Create a PDF document
#         pdf_buffer = BytesIO()
#         pdf = PDFDocument(pdf_buffer)
#
#         # Add the information to the PDF document
#         pdf.init_report()
#         pdf.h1("Predicted Disease")
#         pdf.p(predicted_class)
#         pdf.h1("Entered Information")
#         pdf.p(f"Name: {name}")
#         pdf.p(f"Age: {age}")
#         pdf.p(f"Gender: {gender}")
#         pdf.p(f"Blood Group: {bg}")
#
#         # Convert image to base64 and embed in the PDF
#         # Convert image to base64 and embed in the PDF
#         if uploaded_file is not None:
#             image_data = uploaded_file.read()
#             image_base64 = base64.b64encode(image_data).decode()
#             pdf.add_page().image(image_base64, caption="Selected Image")
#
#         pdf.generate()
#
#         # Save the PDF file
#         pdf_buffer.seek(0)
#         b64_data = base64.b64encode(pdf_buffer.read()).decode()
#         href = f'<a href="data:application/octet-stream;base64,{b64_data}" download="prediction_report.pdf">Download PDF</a>'
#         st.markdown(href, unsafe_allow_html=True)
#
# #         # Provide a download link to the generated PDF file
# #         st.success("PDF generated successfully!")
# #         st.markdown(get_download_link("prediction_report.pdf", "Download PDF"), unsafe_allow_html=True)
# #
# #
# # def get_download_link(file_path, link_text):
# #     with open(file_path, "rb") as file:
# #         data = file.read()
# #     b64_data = base64.b64encode(data).decode()
# #     href = f'<a href="data:application/octet-stream;base64,{b64_data}" download="{file_path}">{link_text}</a>'
# #     return href
#
# # Run the Streamlit application
# if __name__ == '__main__':
#     main()
