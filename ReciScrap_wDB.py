#!/usr/bin/env python3
import tkinter
from recipe_scrapers import scrape_me
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="local",
  user="admin",
  password="123password",
  database="AppDB"
)

gui = tkinter.Tk()
gui.geometry("500x700")  # size of the window by default
gui.title("Super Recipe App 900")


def scraper():
    url = url_entry.get()
    scraper_recipe = scrape_me(url)
    tfield.delete("1.0", "end")
    tfield.insert(tkinter.INSERT, scraper_recipe.title() + "\n\n")
    tfield.insert(tkinter.INSERT, "Ingredients:\n" +
                  "\n".join(scraper_recipe.ingredients()) + "\n\n")
    tfield.insert(tkinter.INSERT, "Instructions:\n" +
                  (scraper_recipe.instructions()))

    # Insert recipe data into MySQL database
    mycursor = mydb.cursor()
    sql = "INSERT INTO recipes (title, ingredients, instructions) VALUES (%s, %s, %s)"
    val = (scraper_recipe.title(), "\n".join(scraper_recipe.ingredients()), scraper_recipe.instructions())
    mycursor.execute(sql, val)
    mydb.commit()


url_entry = tkinter.Entry(gui, width=24, font='Arial 20 bold')
url_entry.pack(pady=10)

tkinter.Button(gui, command=scraper, text="Get Recipe", font="Arial 20 bold",
               bg='red', fg='black', activebackground="red", padx=5, pady=5).pack(pady=20)

tkinter.Label(gui, text="Recipe Info:", font='arial 15 bold').pack(pady=10)

tfield = tkinter.Text(gui, width=58, height=20)
tfield.pack()

# -------------------------------------closed in mainloop to run
gui.mainloop()
