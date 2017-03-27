from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter, Select
from bokeh.plotting import figure
from random import randrange
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from math import radians
from pytz import timezone
from bokeh.layouts import layout


#create webscraping function
def extract_value(market_name='okcoinCNY'):
    r = requests.get(r'http://bitcoincharts.com/markets/'+ market_name +'.html',headers={'User-Agent':'Google Chrome/56.0.2924.87'})
    c = r.content
    soup = BeautifulSoup(c,'lxml')
    value_raw=float(soup.find('p').span.text)
    return value_raw

#creeate periodic callback function
def update():
    new_data = dict(x=[datetime.now()],y=[extract_value(select.value)])
    source.stream(new_data,rollover=15)
    print(source.data)

#need to define an intermediate callback function (to call the update function) that accepts the required positional args (attr,old,new) so you can indirectly call the update function on the select.on_change() method without having to pass in the required args, because we dont need/cant use those args here
def update_callback(attr,old,new):
    source.data = dict(x=[],y=[]) # this is a trick that will clear all of the residual data left over from the previously selected market, so that when you chanage the widget, only the data for the selected widget will appear on the graph
    update()

TOOLS="pan,wheel_zoom,box_zoom,reset,save,hover,crosshair"

#create figure
fig = figure(tools=TOOLS)
fig.xaxis.formatter = DatetimeTickFormatter(formats=dict(
seconds = ['%Y-%m-%d-%H-%M-%S-%Z'],
minsec = ['%Y-%m-%d-%H-%M-%S'], #ensures smooth transition between seconds to minutes when second cycle restarts
minutes = ['%Y-%m-%d-%H-%M-%S'],
hourmin = ['%Y-%m-%d-%H-%M-%S'],  #ensures smooth transition between minutes to hours when minute cycle restarts
hours = ['%Y-%m-%d-%H-%M-%S'],
days = ['%Y-%m-%d-%H-%M-%S'],
months = ['%Y-%m-%d-%H-%M-%S'],
years = ['%Y-%m-%d-%H-%M-%S']
))


fig.xaxis.major_label_orientation = radians(90)

#create ColumnDataSource
source = ColumnDataSource(dict(x=[],y=[]))

#create glyphs
fig.circle(x='x',y='y',color='blue',line_color='yellow',source=source)
fig.line(x='x',y='y',source=source)

#create the select widget
options = [('okcoinCNY','okcoin CNY'),('btcnCNY','BTCN China')]
select = Select(title='Market Name',value='okcoinCNY',options=options)
select.on_change('value',update_callback)

#add figure to curdoc and configure callback
layout = layout([[fig],[select]])
curdoc().add_root(layout)
curdoc().add_periodic_callback(update,2000)
