
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.patches as patches
from Utils.PointTypes import points_to_xy
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data
from matplotlib.table import table as mpltable

def make_blank_canvas(size=[12,12],**kwargs):
    fig = plt.figure(**kwargs)
    fig.set_size_inches(size[0],size[1])
    return fig

def make_blank_plot(a=1,b=1,p=1,xlim=None,ylim=None,box=True,fig=None,**kwargs):

    if fig == None:
        fig = plt.gcf()
        
    ax = fig.add_subplot(a,b,p,**kwargs)
    
    
    # If no coordinate range is given fit everything into a square
    if not xlim and not ylim:
        pass
    # If only xrange is given fit a square
    elif not ylim:
        ax.set_xlim(xlim)
        ax.set_ylim(xlim)
    # If both are given fix the rectangle
    else:
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
    
    if box == False:
        ax.axis('off')
        
    ax.set_xticks([])
    ax.set_yticks([])
    return ax

# Convenience functions for titles
def title(text="",ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    ax.set_title(text,**kwargs)

def canvas_title(text="",fig=None,**kwargs):
    if fig == None:
        fig = plt.gcf()
    fig.suptitle(text,**kwargs)

# Text
def text(x,y,t,ax=None,**kwargs):
    if ax == None:
        ax = plt.gca()
    ax.text(x,y,t,**kwargs)
    
# Convinence for inserting images within the plot
# This definitely isn't the best way to do this
def image(path,x=0,y=0,scale=1,ax=None):
    if ax == None:
        ax = plt.gca()
        
    with get_sample_data(path) as file:
        arr_img = plt.imread(file, format='png')
    
    imagebox = OffsetImage(arr_img, zoom=scale)
    
    ab = AnnotationBbox(imagebox, [x,y],
                        xycoords='data',
                        boxcoords="offset points",
                        frameon=False)

    ax.add_artist(ab)