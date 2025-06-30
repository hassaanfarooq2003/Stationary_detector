# Stationary Detector using YOLOv5

This project is a web application that detects stationary items (Eraser, Pencil, Scale, Sharpener) in images using a custom-trained YOLOv5 model. It calculates the total bill based on detected items and displays the results in a user-friendly Streamlit interface.

---

## Features

- **Upload an image** containing stationary items.
- **Detects and counts**: Erasers, Pencils, Scales, Sharpeners.
- **Calculates total bill** based on item counts and predefined prices.
- **Visualizes detections** with bounding boxes.
- **Simple web interface** built with Streamlit.

---

## Directory Structure

```
.
├
│── app.py                 # Streamlit web app
│notebook.ipynb           #Jupyter notebook 
├── yolov5/
│   └── weights/
│       ├── best.pt            # Trained YOLOv5 model weights
│       └── last.pt
├
```

---

## Requirements

- Python 3.7+
- torch
- torchvision
- opencv-python
- pillow
- streamlit
- roboflow (for dataset download, if retraining)
- yolov5 (via torch.hub)

Install dependencies with:
```bash
pip install torch torchvision opencv-python pillow streamlit roboflow
```

---

## Setup & Usage

1. **Clone the repository and navigate to the project directory.**

2. **Ensure model weights are available:**
   - Place your trained YOLOv5 weights (`best.pt`) in `yolov5/weights/best.pt` or update the path in `app.py` accordingly.

3. **Run the Streamlit app:**
   ```bash
   streamlit run submission/app.py
   ```

4. **Open the provided local URL in your browser.**

5. **Upload an image** containing stationary items. The app will:
   - Display the uploaded image.
   - Show the total bill.
   - List the count of each detected item.
   - Show the image with detected items highlighted.

---

## Item Pricing

- **Eraser:** Rs. 5
- **Pencil:** Rs. 5
- **Scale:** Rs. 20
- **Sharpener:** Rs. 10

---

## Training the Model

- The model was trained using YOLOv5 and a custom dataset from Roboflow.
- See `notebook.py` for the full training and inference pipeline, including:
  - Downloading the dataset from Roboflow.
  - Training with YOLOv5.
  - Exporting and saving the trained weights.

---

## Notes

- The app loads the YOLOv5 model using `torch.hub`.
- For best results, use clear images with visible stationary items.
- You can retrain the model using your own dataset and update the weights file as needed.

---

## License

This project is for educational purposes. 
