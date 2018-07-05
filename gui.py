# https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
from Tkinter import *
import threading
import os
from datetime import datetime
from time import sleep
from PIL import Image, ImageTk, ImageChops

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Xplore group bartender - Enjoy")

        # req screen and set to max
        self.request_screen_info()
        self.master.geometry(str(self.screen_width) + "x" + str(self.screen_height))

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # load a tmp img
        load = Image.open("img/noimg.png")
        render = ImageTk.PhotoImage(load)

        # use lbl for img
        self.img = Label(self, image= render)
        self.img.grid(row=0, rowspan=4, column=0, pady=(self.padding_img_y), padx=(self.padding_img_x))
        self.img.image = render

        #name label
        self.lblNameTxt = StringVar()
        self.lblName = Label(self, textvariable=self.lblNameTxt).grid(row=0, column=1, columnspan=2, pady=(self.padding_title_y), padx=(self.padding_title_y))

        #desc label
        self.lblDescriptionTxt = StringVar()
        self.lblDescription = Label(self, textvariable=self.lblDescriptionTxt).grid(row=1, column=1, columnspan=2, pady=(self.padding_title_y), padx=(self.padding_title_x))

        # #ingredients label
        self.lblIngredientsTxt = StringVar()
        self.lblingredients = Label(self, textvariable=self.lblIngredientsTxt).grid(row=2, column=1, pady=(5, 5), padx=(5, 5))
        self.lblIngredientsTxt.set("Ingredients")

        # render the labels for the ingriedents
        self.render_ingredients_labels(2, 3)


        Grid.rowconfigure(self, 2, weight=1)
        Grid.columnconfigure(self, 1, weight=1)

        self.set_dummy_data()

    def request_screen_info(self):
        #request screen settings
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        #own set parameters
        self.padding_img_y = 40
        self.padding_img_x = 40

        self.padding_title_y = 40
        self.padding_title_x = 40

        self.padding_description_y = 40
        self.padding_description_x = 40


    def render_ingredients_labels(self, startrow, startcolumn):
        names = ["lblIngredientOne", "lblIngredientTwo", "lblIngredientThree", "lblIngredientFour", "lblIngredientFive", "lblIngredientSix", "lblIngredientSeven", "lblIngredientEight"]


        #all ingiedensts label (not the cleanest way, but otherwise tkinters nags)
        self.lblIngredientOneTxt = StringVar()
        self.lblIngredientOne = Label(self, textvariable=self.lblIngredientOneTxt).grid(row=startrow, column=startcolumn, pady=(5, 5), padx=(5, 5))


        self.lblIngredientTwoTxt = StringVar()
        self.lblIngredientTwo = Label(self, textvariable=self.lblIngredientTwoTxt).grid(row=3, column=2, pady=(5, 5), padx=(5, 5))



    def update_ingredients(self):
        pass

    def set_dummy_data(self):
        self.lblNameTxt.set("Gin Tonic")
        self.lblDescriptionTxt.set("A popular mix between tonic and gin")
        self.set_img("img/gintonic.jpg")
        #self.lblIngredientOneTxt.set("Tonic")
        #self.lblIngredientTwoTxt.set("Gin")


    def set_img(self, full_img_name):
        y_height = self.screen_height - self.padding_img_x - self.padding_img_y
        x_height = int((self.screen_height - self.padding_img_x - self.padding_img_y) / 1.618)

        print(x_height)
        print(y_height)

        load = Image.open(full_img_name).resize((x_height, y_height),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        #set the img
        self.img.configure(image=render)
        self.img = render
        #self.img.place(x=0, y=0)


    def set_cocktail_data(self, cocktail):
        self.lblNameTxt.set(cocktail[""])
        self.lblDescriptionTxt.set(cocktail[""])
        self.show_img("img/" + cocktail[""])
        # self.lblIngredientOneTxt.set(cocktail[""])
        # self.lblIngredientTwoTxt.set(cocktail[""])




try:
    root = Tk()
    # root.geometry("400x300")
    app = Window(root)
    root.mainloop()

except Exception as ex:
    print(ex)



