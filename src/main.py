import gradio

def upload_your_jalapeno(img):
    if img is None:
      return "Please upload a jalapeño photo."
    return "Your jalapeño heat rating is: 5/10"
    
    
demo = gradio.Interface(fn=upload_your_jalapeno, inputs="image", outputs="text", title="How hot is your jalapeno!!")
demo.launch()
