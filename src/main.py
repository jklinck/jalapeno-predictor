import gradio as gr
import base64
import tensorflow as tf

model = tf.keras.models.load_model('models/mobilenetv2_model.keras')
class_names = ['hot', 'mild', 'medium']

def upload_your_jalapeno(img):
    if img is not None:
        img = tf.image.resize(img, [180, 180]).numpy()
        img = img.reshape((1,180,180,3)).astype('float') / 255
        prediction = model.predict(img)
        predicted_index = prediction[0].argmax()
        confidence = prediction[0][predicted_index] * 100
        return f"{class_names[predicted_index]} ({confidence:.1f}% confidence)"
    else:
        return "Please upload a jalapeño photo."

with open("img/validate/mild/P001_a.jpg", "rb") as f:
    img_data1 = base64.b64encode(f.read()).decode("utf-8")

with open("img/validate/hot/P064_a.jpg", "rb") as f:
    img_data2 = base64.b64encode(f.read()).decode("utf-8")

with open("img/validate/hot/P065_a.jpg", "rb") as f:
    img_data3 = base64.b64encode(f.read()).decode("utf-8")

with open("img/train/medium/P037_a.jpg", "rb") as f:
    img_data4 = base64.b64encode(f.read()).decode("utf-8")

with gr.Blocks(css="body, .gradio-container { background-color: #E5FFCC !important; }") as demo:
    gr.HTML("<h1 style='text-align:center; color:red;'>How hot is your jalapeño!!</h1>")
    inp = gr.Image(height=200)
    out = gr.Textbox()
    inp.change(fn=upload_your_jalapeno, inputs=inp, outputs=out)
    gr.HTML(f"""
    <div style="display:flex; gap:10px;">
        <img src='data:image/jpeg;base64,{img_data1}' width='300'>
        <img src='data:image/jpeg;base64,{img_data4}' width='300'>
        <img src='data:image/jpeg;base64,{img_data3}' width='300'>
        <img src='data:image/jpeg;base64,{img_data2}' width='300'>
    </div>
""")
demo.launch()
