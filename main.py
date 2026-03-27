import gradio as gr
import base64
import tensorflow as tf

model = tf.keras.models.load_model('model.h5')

def upload_your_jalapeno(img):
    if img is not None:
        image = image.reshape((1,28,28,1)).astype('float') / 255
        prediction = model.predict(image)
        return prediction
    else:
        return "Please upload a jalapeño photo."

with open("img/Mild/P001_a.JPG", "rb") as f:
    img_data1 = base64.b64encode(f.read()).decode("utf-8")

with open("img/Hot/P064_a.JPG", "rb") as f:
    img_data2 = base64.b64encode(f.read()).decode("utf-8")

with open("img/Hot/P065_a.JPG", "rb") as f:
    img_data3 = base64.b64encode(f.read()).decode("utf-8")

with open("img/medium/P037_a.JPG", "rb") as f:
    img_data4 = base64.b64encode(f.read()).decode("utf-8")

with gr.Blocks() as demo:
    gr.HTML("<h1 style='text-align:center; color:red;'>How hot is your jalapeño!!</h1>")
    inp = gr.Image()
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