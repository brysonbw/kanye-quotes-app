from tkinter import *
import requests

#Using kanye quotes api
#Function fetches api and fills into >quoteText on the canvas  
def get_quote():
    response = requests.get('https://api.kanye.rest')
    response.raise_for_status()
    data = response.json()
    quote = data['quote'] #Fetches value under key quote
    canvas.itemconfig(quoteText, text=quote)



window = Tk()
window.title('Kanye Says...')
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
backgroundImg = PhotoImage(file='background.png')
canvas.create_image(150, 207, image=backgroundImg)
quoteText = canvas.create_text(150, 207, text='Kanye Quote Goes HERE', width=250, font=('Arial', 10, 'bold'), fill='white')
canvas.grid(row=0, column=0)

kanyeImg = PhotoImage(file='kanye.png')
kanyeButton = Button(image=kanyeImg, highlightthickness=0, command=get_quote)
kanyeButton.grid(row=1, column=0)



window.mainloop()