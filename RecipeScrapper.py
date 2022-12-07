#!/usr/bin/env python3
import tkinter
from recipe_scrapers import scrape_me

gui = tkinter.Tk()
gui.geometry("500x700")  # size of the window by default
gui.title("Super Recipe App 900")

url = tkinter.StringVar().get
''''''
scraper_recipe = scrape_me(
    'https://altonbrown.com/recipes/bourbon-pecan-pie/')


def scraper():
    tfield.delete("1.0", "end")
    tfield.insert(tkinter.INSERT, scraper_recipe.title(), scraper_recipe.ingredients(), scraper_recipe.description(
    ), scraper_recipe.yields(), scraper_recipe.instructions_list(), scraper_recipe.ingredients(), scraper_recipe.nutrients())


tkinter.Label(gui, text='Enter Website',
              font='Arial 20 bold').pack(pady=10)

tkinter.Entry(gui, textvariable=url,
              width=24, font='Arial 20 bold').pack()

tkinter.Button(gui, command=scraper, text="Get Recipe", font="Arial 20 bold",
               bg='red', fg='black', activebackground="red", padx=5, pady=5).pack(pady=20)

tkinter.Label(gui, text="Recipe Info:",
              font='arial 15 bold').pack(pady=10)


tfield = tkinter.Text(gui, width=58, height=10)
tfield.pack()
# -------------------------------------closed in mainloop to run
gui.mainloop()
