from bokeh.io import curdoc
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout

#create widget
text_input = TextInput(value='Enter text')
button = Button(label='Generate text')
output= Paragraph()

def update():
    output.text='Hello ' + text_input.value

button.on_click(update)

layout = layout([[button,text_input],[output]])

curdoc().add_root(layout)
