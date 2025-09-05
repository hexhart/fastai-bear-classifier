# 🐻 Bear Classifier (fastai + Gradio)

[![Hugging Face Space](https://img.shields.io/badge/Space-live-blue)](https://huggingface.co/spaces/hexhart/fastai-bear-classifier)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A simple **image classifier** built with [fastai](https://docs.fast.ai/) that can tell whether an image is a **Black Bear**, **Grizzly Bear**, or **Teddy Bear**.  
The model is wrapped in an interactive [Gradio](https://www.gradio.app/) app and deployed on [Hugging Face Spaces](https://huggingface.co/spaces).

---

## 🚀 Live Demo

👉 [Try it out on Hugging Face Spaces](https://huggingface.co/spaces/hexhart/fastai-bear-classifier)

<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/28de7d00-7063-414e-9cf3-8f5cbf3796cc" />

---

## ⚙️ Installation & Usage

Clone the repo and install dependencies:

```bash
git clone https://github.com/hexhart/fastai-bear-classifier.git
cd fastai-bear-classifier
pip install -r requirements.txt
```
Run the app:
```bash
python app.py
```
## 📂 Repository Structure
```bash
fastai-bear-classifier/
│
├── app.py             # Gradio app entry point
├── bear-export.pkl    # Pretrained fastai model
├── requirements.txt   # Dependencies
├── README.md          # Project documentation
└── images/            # (Optional) Screenshots or sample images
```
## 🧠 Model Details
- Architecture: ResNet-34 (transfer learning)
- Framework: fastai 2.x, PyTorch
- Dataset: Bear images from fastai’s [lesson dataset](https://course.fast.ai/?utm_source=chatgpt.com)
- Classes:
  - 🐻 Black Bear
  - 🐻‍❄️ Grizzly Bear
  - 🧸 Teddy Bear

## ⚠️ Limitations
- Only trained on three bear categories.
- May misclassify unrelated images as “bear.”
- No “not a bear” option (yet!).

## 🤝 Contributing
Got ideas for improvements? PRs and issues are welcome!

## ✨ Additional Notes:
Check out the configuration reference at https://huggingface.co/docs/hub/spaces#reference
__________________________________________
<p align="center"><img width="200" height="200" alt="Logo2m" src="https://github.com/user-attachments/assets/147e72b3-d07b-43d9-aa80-f49094e3b592" /></p>
<h4 align="center">You have reached the end of this README. Thank you.</h4>
