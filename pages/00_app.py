import streamlit as st
from utils import prediction


if not st.user.is_logged_in:
    st.error("Please log in to access the App")
    st.stop()

class_dict = {
    "ADI": "Adipose",
    "BACK": "Background",
    "DEB": "Debris",
    "LYM": "Lymphocytes",
    "MUC": "Mucus",
    "MUS": "Smooth Muscle",
    "NORM": "Normal Colon Mucosa",
    "STR": "Cancer-Associated Stroma",
    "TUM": "Colorectal Adenocarcinoma Epithelium"
}


def cancer_prediction():
    st.title("Human Colorectal Cancer Prediction")

    st.image(
        "https://cdn.scope.digital/Images/Articles/kolon-bagirsak-kanseri-belirtileri-ve-tedavisi-5628892.jpg?tr=w-630,h-420", 
        caption = "Human Colorectal Cancer Prediction")


    image = st.file_uploader(label="Upload an image",accept_multiple_files=False, help="Upload an image to classify them")


    if image:
        #validating the image type
        image_type = image.type.split("/")[-1]
        if image_type not in ['jpg','jpeg','png','jfif', 'tif', 'tiff']:
            st.error("Invalid file type : {}".format(image.type), icon="🚨")
        else:
            #displaying the image
            st.image(image, caption = "Uploaded Image")

            #getting the predictions
            with st.spinner("Wait for it...", show_time=True):
                label = prediction("featurized_best_model", image)

            tissue_class = class_dict[label]

            #displaying the predicted label
            st.success("Your Tissue Class is: **{}**".format(tissue_class))
    



if __name__ == '__main__':
    cancer_prediction()