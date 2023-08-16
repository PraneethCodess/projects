#API extracted from NewsAPI.org

import io
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
import webbrowser

class QwikReads :

    def __init__(self):

        # fetch data

        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=482df6fdb673409abc96330dda9dfc74').json() #json url
        
        #print(self.data)                                                        to check if the json is printed

       
       
        # initial GUI loading

        self.load_gui()
        

       
        # load the 1st news item

        self.load_news_item(0)                                      # 0 is the index of the news item

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x550')
        self.root.resizable(0,0)
        self.root.configure(background= 'black')
        self.root.title('QwikReads')

    def clear(self):
        
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):

        # clear screen for the new news item
        self.clear()

        #Image 
        try:
            img_url= self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im= Image.open(io.BytesIO(raw_data)).resize((350,260))
            Photo = ImageTk.PhotoImage(im)

        except:
            img_url= 'https://media.istockphoto.com/id/1392182937/vector/no-image-available-photo-coming-soon.jpg?s=170x170&k=20&c=0Bdi_OrEetPTwy_PoKCuevjjOqs3heMgf3-nus2aqAg='
            raw_data = urlopen(img_url).read()
            im= Image.open(io.BytesIO(raw_data)).resize((350,260))
            Photo = ImageTk.PhotoImage(im)

        label = Label(self.root, image=Photo)
        label.pack()

        heading = Label(self.root, text= self.data['articles'][index]['title'], bg= 'black', fg = 'white', wraplength= 350, justify= 'center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15,'bold'))

        details = Label(self.root, text= self.data['articles'][index]['description'], bg= 'black', fg = 'white', wraplength= 350, justify= 'center')
        details.pack(pady=(2,20))
        details.config(font=('verdana',10,))

        frame = Frame(self.root, bg= 'black')
        frame.pack(expand= True, fill=BOTH)
        if index != 0 :
            prev = Button(frame, text= 'Prev', width= 16, height=3, command = lambda : self.load_news_item(index-1))
            prev.pack(side= LEFT)

        read = Button(frame, text= 'Read More', width= 16, height=3, command= lambda : self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles'])-1 :

            next= Button(frame, text= 'Next', width=16, height=3, command = lambda : self.load_news_item(index+1))
            next.pack(side= LEFT)

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)




start= QwikReads()