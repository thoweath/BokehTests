from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from random import randrange

#create figure
fig = figure(x_range=(0,11),y_range=(0,11))

#create ColumnDataSource
source = ColumnDataSource(dict(x=[],y=[]))

#create glyphs
fig.circle(x='x',y='y',color='blue',line_color='yellow',source=source)
fig.line(x='x',y='y',source=source)

#creeate periodic callback function
def update():
    new_data = dict(x=[randrange(1,10)],y=[randrange(1,10)])
    source.stream(new_data,rollover=15)
    print(source.data)

#add figure to curdoc and configure callback
curdoc().add_root(fig)
curdoc().add_periodic_callback(update,1000)
