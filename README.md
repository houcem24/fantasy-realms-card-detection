Fantasy Realms Card Game — Computer Vision Project

This project implements a computer vision system for the Fantasy Realms card game. The goal is to automatically recognize cards in hand / on the table, classify them, and assist game-scoring or digital interaction using vision algorithms.

🎯 Project Overview

Use image processing / deep learning techniques to detect and recognize card faces and symbols in the Fantasy Realms card game.

Enable automated scoring, rule enforcement, or augmented reality overlays based on recognized cards.

Support variations in lighting, card positions, occlusion, and camera angles.

📂 Repository Structure

Here’s a suggested (or observed) layout — adjust if your repo differs:

.
├── data/                    # images of cards (train / validation / test)
├── models/                  # saved weights / checkpoints
├── notebooks/               # experiments, visualization, testing
├── src/
│   ├── detection.py         # code for locating cards in an image
│   ├── classification.py    # card classification (which card it is)
│   ├── utils.py             # helper functions (preprocessing, augmentation)
│   └── inference.py         # pipeline: detect + classify full image
├── requirements.txt         # dependencies
├── README.md                # this file
├── LICENSE                  # license file
└── demo/                    # sample input images & output visualizations

🛠️ Methods & Workflow

Data collection & annotation

Capture or collect images of Fantasy Realms cards in varying conditions

Annotate bounding boxes and labels

Preprocessing & augmentation

Resize, normalize, augment (rotation, color jitter, etc.)

Card detection / localization

Use classical methods (contour detection, thresholding) or deep models (e.g. SSD, YOLO)

Card classification

For each detected region, apply a classifier (CNN or transfer learning) to predict which card

Post-processing & scoring logic

Combine recognized cards to compute game scores or validate hands

Handle misclassifications or uncertainties

Inference pipeline

Given new image → detect cards → classify → output structured results (card IDs, positions)

Optionally overlay bounding boxes and labels for visualization

Evaluation & metrics

Detection: IoU, precision/recall

Classification: accuracy, confusion matrix

Overall: correctness on full hands / game scoring

⚙️ Setup & Installation

Clone the repo:

git clone https://github.com/houcem24/Fantasy-Realms-Card-Game-Computer-Vision-Project.git
cd Fantasy-Realms-Card-Game-Computer-Vision-Project


Create a virtual environment and install dependencies:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Download / place annotated datasets into data/ folder.

Place any pretrained model files into models/ if required.

🚀 Usage & Inference

To run detection + classification on a sample image:

python src/inference.py --input demo/sample.jpg --output demo/out.json


You can use a notebook or script inside notebooks/ to explore results, visualize bounding boxes, or tune models.

📈 Results & Performance

Detection: (e.g. mean IoU, precision / recall)

Classification accuracy on test set

End-to-end scoring correctness: how often full hands / game outputs are correctly recognized

Visual examples: overlayed bounding boxes and labels for sample images

Include sample output images (before / after) in demo/ or embed in README.

🔮 Future Improvements

Use more advanced detection networks (e.g. transformers, attention-based models)

Improve classification with ensemble learning or better augmentation

Handle occlusions and overlapping cards more robustly

Deploy a mobile app / real-time camera-based version

Integrate error correction or human-in-the-loop validation

Extend to multiplayer tables / full gameplay scenes
