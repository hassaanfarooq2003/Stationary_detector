import streamlit as st
from PIL import Image
import os
import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/exp/weights/best.pt', force_reload=True)
model.conf = 0.025
def calculate_bill(image_path, model):
    frame = cv2.imread(image_path)
    results = model(frame)
    TOTAL = 0
    class_counts = {}  

    for i in results.pandas().xyxy[0]['class']:
        class_counts[i] = class_counts.get(i, 0) + 1  
        if i == 1:  
            TOTAL += 5
        elif i == 2:  
            TOTAL += 20
        elif i == 3:
            TOTAL += 10
        else:  
            TOTAL += 5 

    return TOTAL, class_counts  


def main():
    st.title("Bill Calculator from Image")
    st.write("Upload an image of the items to calculate the total bill.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
#   Eraser
# - Pencil
# - Scale
# - Sharpener
    
    
    if uploaded_file is not None:
        temp_dir = "temp"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
            
        image_path = os.path.join(temp_dir, uploaded_file.name)
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

        total_bill,class_counts = calculate_bill(image_path, model)
        st.write(f"Total Bill: Rs.{total_bill}")
        st.write("Object Counts:")
        for cls, count in class_counts.items():
            if cls == 0:
                cls = "Eraser"
            if cls == 1:
                cls = "Pencil"
            if cls == 2:
                cls = "Scale"
            if cls == 3:
                cls = "Sharpener"
            st.write(f"{cls}: {count} items")


        image = Image.open(image_path)
        st.image(image, caption="Uploaded Image")

        results = model(image_path)  
        results.render()

        st.image(results.ims[0], caption="Detected Items")

if __name__ == "__main__":
    main()