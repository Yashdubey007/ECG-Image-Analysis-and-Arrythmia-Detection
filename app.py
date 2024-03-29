import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

 
model_dir = 'C:/Users/ASUS/Desktop/myenv'   

 
model = tf.saved_model.load(model_dir)

import streamlit as st
from PIL import Image

 
background_image_path = 'C:/Users/ASUS/Downloads/heart.jpg'

 
st.set_page_config(
    page_title="My Streamlit App with Background Image",
    page_icon="🌈",
    layout="wide",
    initial_sidebar_state="expanded",
)

 
background_image = Image.open(background_image_path)

 
st.image(
    background_image,
    caption="",
    use_column_width=True,
    output_format="auto",
)

 
st.title("ECG Analysis App")
st.write("Welcome to the ECG analysis app.")

 
extended_category_descriptions = {
    'N': {
        'Description': "Normal sinus rhythm.",
        'Symptoms': "No noticeable irregularities in the heartbeat.",
        'Causes': "A healthy heart and normal conduction system.",
        'Prevalence': "Common in healthy individuals.",
        'Clinical Significance': "Indicates a healthy heart rhythm.",
        'Treatment': "No specific treatment required.",
        'References': "For more information, refer to source Basic ECG Interpretation by Lisa Leonard (Departmental Lead Emergency Department PRISMA Health)."
    },
    'S': {
        'Description': "Supraventricular arrhythmia.",
        'Symptoms': "May include palpitations, rapid heartbeat, or fluttering sensations.",
        'Causes': "Can result from stress, caffeine, or underlying heart conditions.",
        'Prevalence': "Relatively common arrhythmia.",
        'Clinical Significance': "Typically benign, but may require evaluation.",
        'Treatment': "May require lifestyle changes or medication.",
        'References': "For more information, refer to source Basic ECG Interpretation by Lisa Leonard (Departmental Lead Emergency Department PRISMA Health)."
    },
    'V': {
        'Description': "Ventricular arrhythmia.",
        'Symptoms': "May include irregular and rapid heartbeat, dizziness, or fainting.",
        'Causes': "Often associated with heart diseases or abnormalities.",
        'Prevalence': "Less common than supraventricular arrhythmias.",
        'Clinical Significance': "May be life-threatening and requires evaluation.",
        'Treatment': "Treatment depends on the specific type and underlying cause.",
        'References': "For more information, refer to source Basic ECG Interpretation by Lisa Leonard (Departmental Lead Emergency Department PRISMA Health)."
    },
    'F': {
        'Description': "Atrial flutter (AFL).",
        'Symptoms': "Rapid, regular heartbeat, palpitations, and shortness of breath.",
        'Causes': "Often associated with heart diseases or structural problems.",
        'Prevalence': "Relatively common arrhythmia.",
        'Clinical Significance': "May require evaluation and treatment.",
        'Treatment': "May involve medication or procedures to control heart rate.",
        'References': "For more information, refer to source Basic ECG Interpretation by Lisa Leonard (Departmental Lead Emergency Department PRISMA Health)."
    },
    'Q': {
        'Description': "Unknown arrhythmia category.",
        'Symptoms': "Varies depending on the specific arrhythmia.",
        'Causes': "May result from various factors.",
        'Prevalence': "N/A.",
        'Clinical Significance': "Requires further evaluation for proper diagnosis.",
        'Treatment': "Treatment depends on the specific diagnosis.",
        'References': "For more information, refer to source Basic ECG Interpretation by Lisa Leonard (Departmental Lead Emergency Department PRISMA Health)."
    }
}

 
uploaded_file = st.file_uploader("Upload an ECG image", type=["jpg", "jpeg", "png"])

 
if uploaded_file is not None:
    
    st.image(uploaded_file, caption="Uploaded ECG Image", use_column_width=True)

     
    if st.button("Make Predictions"):
         
        image = Image.open(uploaded_file)
        image = image.convert("RGB")
        image = image.resize((128, 128))
        image = np.array(image, dtype=np.float32)
        image = image / 255.0
        image = np.expand_dims(image, axis=0)

         
        predictions = model(image)

         
        categories = ['N', 'S', 'V', 'F', 'Q']
        predicted_category = categories[np.argmax(predictions)]

        
        st.write(f"Prediction: {predicted_category}")
        description = extended_category_descriptions.get(predicted_category, {})
        st.write("Category Description: ", description.get("Description", "Description not available"))
        st.write("Symptoms: ", description.get("Symptoms", "Symptoms not available"))
        st.write("Causes: ", description.get("Causes", "Causes not available"))
        st.write("Prevalence: ", description.get("Prevalence", "Prevalence not available"))
        st.write("Clinical Significance: ", description.get("Clinical Significance", "Clinical Significance not available"))
        st.write("Treatment: ", description.get("Treatment", "Treatment not available"))
        st.write("References: ", description.get("References", "References not available"))
