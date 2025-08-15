import subprocess

# Utility function to run pip install
def install(package):
    subprocess.check_call(["pip", "install", package])

# 1. Install OpenCV first
print("Installing OpenCV...")
install("opencv-python")

# 2. Machine Learning & Deep Learning Core Libraries
ml_dl_libs = [
    "numpy",
    "pandas",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "xgboost",
    "lightgbm",
    "tensorflow",
    "torch",
    "torchvision",
    "torchaudio",
    "keras",
]

# 3. NLP Libraries
nlp_libs = [
    "nltk",
    "spacy",
    "transformers",
    "datasets",        # HuggingFace Datasets
    "sentence-transformers",
]

# 4. Computer Vision Libraries
cv_libs = [
    "imageio",
    "scikit-image",
    "Pillow",
    "mediapipe",
    "ultralytics",     # YOLOv8
    "pycocotools",
]

# 5. Utility Libraries
utils = [
    "tqdm",
    "jupyterlab",
    "notebook",
    "ipywidgets",
]

# Combine all
all_packages = ml_dl_libs + nlp_libs + cv_libs + utils

# Install all other packages
for pkg in all_packages:
    print(f"Installing {pkg}...")
    install(pkg)

print("\n✅ All packages installed successfully!")
