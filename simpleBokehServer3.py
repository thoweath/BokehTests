from bokeh.plotting import figure
from bokeh.models.annotations import LabelSet
from bokeh.models import ColumnDataSource
from bokeh.io import curdoc
from bokeh.models.widgets import TextInput, Button, Paragraph, Select
from bokeh.layouts import layout

#create ColumnDataSource
source1 = ColumnDataSource(dict(average_grades=['B+','A','D-'],
                            exam_grades=['A+','C','D'],
                            student_names=['Tom','John','Andy']))

source2 = ColumnDataSource(dict(average_grades=['B','C','F'],
                            exam_grades=['F','A','B+'],
                            student_names=['Thomas','Jonathan','Andrew']))

#create the figure
fig1 = figure(x_range=['F','D-','D','C-','C','C+','B-','B','B+','A-','A','A+'],
            y_range=['F','D-','D','C-','C','C+','B-','B','B+','A-','A','A+'])

fig2 = figure(x_range=['F','D-','D','C-','C','C+','B-','B','B+','A-','A','A+'],
            y_range=['F','D-','D','C-','C','C+','B-','B','B+','A-','A','A+'])

#add labels for glyphs
labels1=LabelSet(x='average_grades',y='exam_grades',text='student_names',x_offset=5,y_offset=5, source=source1)
fig1.add_layout(labels1)

labels2=LabelSet(x='average_grades',y='exam_grades',text='student_names',x_offset=5,y_offset=5, source=source2)
fig2.add_layout(labels2)

#create glyphs
fig1.circle(x='average_grades',y='exam_grades',source=source1,size=8)
fig2.circle(x='average_grades',y='exam_grades',source=source2,size=8)

#create function
def update_fig(attr,old,new):
    if select1.value == 'fig2':
        curdoc().add_root(fig2)


#create select widget
options=[('fig1','fig1'),('fig2','fig2')]
select1 = Select(title='Attribute',options=options)
select2 = Select(title='Attribute',options=options)
select3 = Select(title='Attribute',options=options)
select1.on_change('value',update_fig)

#create layout and add curdoc
layout=layout([[select1, select2, select3]])
curdoc().add_root(fig1)
# curdoc().add_root(fig2)
curdoc().add_root(layout)
