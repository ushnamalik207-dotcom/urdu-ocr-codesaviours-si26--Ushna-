# Urdu OCR — Optical Character Recognition for Printed Urdu Text

An end-to-end Machine Learning pipeline and web application that extracts and digitizes printed Urdu text from document images using fine-tuned Vision Encoder-Decoder (TrOCR) architecture.

---

### 📌 Why This Matters
Urdu is a cursive, bidirectional script with complex font ligatures (Nastaliq & Naskh) and severe character overlap. Standard OCR engines (like default Tesseract) frequently struggle with Urdu script accuracy. This project addresses the low-resource barrier by providing an accurate, fine-tuned OCR solution to easily digitize printed Urdu literature, scanned books, and historical archives.

---

### 🌐 Live Demo & Video Walkthrough
* **Live Web App (Hugging Face Spaces):** [https://huggingface.co/spaces/Ushna-Alam219/Urdu-OCR-Demo](https://huggingface.co/spaces/Ushna-Alam219/Urdu-OCR-Demo)
* **Loom Video Walkthrough:** [Add your Loom Video URL here after recording]

---

### ⚙️ How It Works
1. **Image Preprocessing:** Scanned document images are loaded, converted to grayscale/RGB, resized, and normalized for standard tensor representation.
2. **Feature Extraction & Encoding:** Vision Transformer (ViT) processes image patches into high-dimensional visual feature vectors.
3. **Sequence Decoding (TrOCR):** An autoregressive language model decoder transforms visual embeddings into token sequences representing Urdu Unicode text.
4. **Interactive Deployment:** Built with an intuitive web interface for real-time image upload and instant text inference.

---

### 📊 Results & Performance
* **Model Backbone:** `microsoft/trocr-base-stage1` (Fine-tuned on curated Urdu text line datasets)
* **Performance Metric:** Achieved robust Character Error Rate (CER) reduction across clear and noisy printed Urdu document samples.

---

### 🚀 How to Run Locally

```bash
# 1. Clone the repository
git clone [https://github.com/ushnamalik207-dotcom/urdu-ocr-codesaviours-si26--Ushna-.git](https://github.com/ushnamalik207-dotcom/urdu-ocr-codesaviours-si26--Ushna-.git)
cd urdu-ocr-codesaviours-si26--Ushna-

# 2. Install required dependencies
pip install -r requirements.txt

# 3. Run the application
python app.py
## Week 5: Streamlit Web Application Deployment
- Developed and deployed an interactive Urdu OCR web app using Streamlit (`app.py`).
- Added deployment configuration and dependencies (`requirements.txt`).
- Enabled real-time Urdu text extraction from user-uploaded images.
