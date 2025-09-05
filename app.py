# --- debug: print versions to container logs ---
import fastai, torch, torchvision, gradio, numpy
print("fastai:", fastai.__version__)
print("torch:", torch.__version__)
print("torchvision:", torchvision.__version__)
print("gradio:", gradio.__version__)
print("numpy:", numpy.__version__)
# ----------------------------------------------

from fastai.learner import load_learner
import gradio as gr
from PIL import Image

# load your existing pickle (keep the filename you already have)
learn = load_learner("bear-export.pkl")

categories = ('Black', 'Grizzly', 'Teddy')

def classify_image(img):
    # If your model expects a fixed size, you can uncomment this resize:
    # if img.size != (192, 192):
    #     img = img.resize((192, 192), Image.BILINEAR)
    pred, idx, probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))

demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),   # Gradio 4 component (works on 3.x too)
    outputs=gr.Label(),            # Gradio 4 component (works on 3.x too)
    title="Bear Classifier",
    description="Black vs Grizzly vs Teddy"
)

if __name__ == "__main__":
    demo.launch()
