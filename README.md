# How hot is your jalapeño!!

![Gradio GUI](img/gradio_gui.png)

A transfer learning model that classifies jalapeño peppers into three heat categories — **hot**, **medium**, or **mild** — from a single photo. Upload an image of your jalapeño and get an instant prediction with confidence score via an interactive Gradio web interface. 

> **Note:** Jalapeño heat levels are visually graded and not an exact science. A pepper's appearance does not always correlate with its actual heat level. Predictions should be treated as estimates only.

---

## How It Works

The model is a transfer learning model trained on labeled jalapeño images organized into three classes:

| Class | Description |
|-------|-------------|
| hot | High capsaicin, visually mature peppers |
| medium | Moderate heat level |
| mild | Low heat, typically less mature peppers |

Images are resized to **224x224 pixels** and normalized before being passed through the network. The model outputs a softmax probability across the three classes, and the highest confidence prediction is returned.

### Model Architecture

- Input: 224x224 RGB image
- Random horizontal flip (data augmentation)
- ImageNet normalization (prepocess_input)
- MobileNetV2 base model pretrained on ImageNet (frozen, transfer learning)
- GlobalAveragePooling2D
- Fully connected Dense layer (128 units, ReLU)
- Dropout (0.3)
- Output: Dense layer (3 units, Softmax)

I tested other augmentation layers such as GaussianNoise, zoom and rotation and found all of them degraded the accuracy of the model. Once I add more images I will test them again for further updates of the model.

---

## Dependencies

**macOS — with Poetry:**
```bash
poetry install
```

**macOS — with pip:**
```bash
pip install tensorflow-macos==2.16.2 tensorflow-metal==1.2.0 gradio==6.10.0
```

**Windows / Linux — with pip:**
```bash
pip install tensorflow gradio
```

| Package | Version | Purpose |
|---------|---------|---------|
| `tensorflow-macos` / `tensorflow` | 2.16.2 | Model training and inference |
| `tensorflow-metal` | 1.2.0 | Mac GPU acceleration |
| `gradio` | 6.10.0 | Web-based GUI |

Python **3.10** or higher is required.

---

## Project Structure

```
jalapeno-predictor/
├── img/
│   ├── train/             # Training images 
│   │   ├── hot/
│   │   ├── medium/
│   │   └── mild/
│   ├── validate/          # Validation images 
│   │   ├── hot/
│   │   ├── medium/
│   │   └── mild/
│   └── gradio_gui.png
├── models/
│   └── mobilenetv2_model.keras
├── notebooks/
│   └── mobilenetv2.ipynb
├── src/
│   └── main.py
├── LICENSE
├── README.md
├── pyproject.toml
└── poetry.lock
```

---

## Training the Model

> **Note:** A pre-trained model is included in `models/`. If you just want to run the app, skip to [Running the App](#running-the-app).

Open and run `mobilenetv2.ipynb` from the notebooks directory. The notebook will:

1. Load images from manually curated `img/train` and `img/validate` directories (80/20 split)
2. Train the model for 20 epochs
3. Save the trained model as `models/mobilenetv2_model.keras`

---

## Running the App

```bash
python3 src/main.py
```

Then open the local URL printed in your terminal (e.g. `http://127.0.0.1:7860`). Upload a photo of a jalapeño and the model will return a prediction like:

```
medium (44.1% confidence)
```

---

## Dataset

203 labeled jalapeño images split across three classes, sourced and organized locally. I was unable to find a good dataset and thus I created this one organically by purchasing peppers at 
multiple grocery stores. They were picked based upon my years of experience cooking with hot peppers and categorized according to my interpretation of what constitutes a hot, medium or mild pepper. I also learned quite a lot about photography (I am a complete novice) and created a photo box in order to control light and shadows for taking the best possible pictures and creating a good dataset.
