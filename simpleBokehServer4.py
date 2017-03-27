from bokeh.plotting import figure
from bokeh.models.annotations import LabelSet
from bokeh.models import ColumnDataSource
from bokeh.io import curdoc
from bokeh.models.widgets import TextInput, Button, Paragraph, Select
from bokeh.layouts import layout, widgetbox
import pandas as pd
from bokeh.embed import components

# elements = pd.read_excel(r'C:\Users\tweatherall\Desktop\elements.xlsx',sheetname='Sheet1')
source_original = ColumnDataSource(dict(atomic_radius=[1,2,3,4,5],
        boiling_point=[6,7,8,9,10],
        standard_state=['gas','solid','liquid','solid','gas'],
        color=['yellow','red','orange','red','yellow'],
        van_der_Waals_radius=[0.1,0.2,0.3,0.4,0.5]))


source = ColumnDataSource(dict(atomic_radius=[1,2,3,4,5],
        boiling_point=[6,7,8,9,10],
        standard_state=['gas','solid','liquid','solid','gas'],
        color=['yellow','red','orange','red','yellow'],
        van_der_Waals_radius=[0.1,0.2,0.3,0.4,0.5]))


#create the figure
fig = figure()

#elements = pd.DataFrame(e)

# elements.dropna(inplace=True)
# #create color mapping
# element_color = {'gas':'yellow','liquid':'orange','solid':'red'}
# #add color column to elements datafarme
# elements['color'] = [element_color[standard_state] for standard_state in elements['standard_state']]

#convert elements dataframe into ColumnDataSource object, segment by solid, liquid, gas types
# solid = ColumnDataSource(elements['standard_state']=='solid'])
# gas = ColumnDataSource(elements['standard_state']=='gas'])
# liquid = ColumnDataSource(elements['standard_state']=='liquid'])

#create glyphs
# fig.circle(x='atomic radius',y='boiling point',size=[(s/10) for s in source.data['van_der_Waals_radius']],color='color',source=source)
# fig.circle(x='atomic radius',y='boiling point',size=[(s/10) for s in liquid.data['van_der_Waals_radius']],color='color',source=liquid)
# fig.circle(x='atomic radius',y='boiling point',size=[(s/10) for s in gas.data['van_der_Waals_radius']],color='color',source=gas)

#add labels for glyphs
label=LabelSet(x='atomic_radius',y='boiling_point',text='standard_state',x_offset=5,y_offset=5, source=source)
# solid_label=LabelSet(x='atomic_radius',y='boiling_point',text='standard_state',x_offset=5,y_offset=5, source=solid)
# liquid_label=LabelSet(x='atomic_radius',y='boiling_point',text='standard_state',x_offset=5,y_offset=5, source=liquid)
# gas_label=LabelSet(x='atomic_radius',y='boiling_point',text='standard_state',x_offset=5,y_offset=5, source=gas)

fig.add_layout(label)
# fig.add_layout(solid_label)
# fig.add_layout(liquid_label)
# fig.add_layout(gas_label)

fig.circle(x='atomic_radius',y='boiling_point',color='color',source=source)

#create filtering function
def filter_data(attr,old,new):
    if select_data.value == 'all':
            source.data={key:[value for value in source_original.data[key]] for key in source_original.data}
    else:
        source.data={key:[value for i,value in enumerate(source_original.data[key]) if source_original.data['standard_state'][i]==select_data.value] for key in source_original.data}
    print(select_data.value)

#create label function
def update_labels(attr,old,new):
    label.text=select.value


#create select widget
options_data=[('solid','Solid'),('liquid','Liquid'),('gas','Gas'), ('all','All')]
select_data = Select(title='Show State',options=options_data)
select_data.on_change('value',filter_data)

options=[('boiling_point','Boiling Point'),('standard_state','Standard State'),('color','Color')]
select = Select(title='Attribute',options=options)
select.on_change('value',update_labels)

#create layout and add curdoc
# layout=layout([[select,select_data]])
layout = widgetbox(select, select_data)

scriptw, w = components(layout)
script, d = components(fig)
print(scriptw,w)
print(script,d)
curdoc().add_root(fig)
curdoc().add_root(layout)
