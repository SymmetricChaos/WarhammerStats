import pickle
import os
from UtilityFunctions import random_unit
from DrawingUtils import make_blank_canvas, make_blank_plot, image, text


class img_and_name:
    
    def __init__(self,x,y,path,name):
        self.x = x
        self.y = y
        self.path = path
        self.name = name
    
    def show(self):
        image(card_img_path,x=self.x,y=self.y)
        text(self.x,self.y+.3,R["name"],horizontalalignment="center",size=20)

if __name__ == '__main__':
    units = pickle.load( open( "unitsDF_clean.p", "rb" ) )

    make_blank_canvas()
    make_blank_plot(xlim=[-1,1])
    
    R = random_unit(units)
    card_img = R["unit_card"]
    
    
    print(card_img)
    
    cur_dir = os.getcwd()
    card_img_path = f"{cur_dir}\\UnitIcons\\{card_img}"
    
    
    I = img_and_name(0,0,card_img_path,R["name"])
    I.show()