from bs4 import BeautifulSoup
import requests
from tkinter import *



class MyWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry('300x200')
        self.btn = Button(width=15, height=2, text='Показать курс',font=('Times New Roman', 11), command=self.main)
        self.btn.place(relx=.5, rely=.6, anchor='c')
        self.txt = Entry(width=25)
        self.txt.place(relx=.5, rely=.3, anchor='c')
        self.lbl = Label(root, text='Курс Compound', font=('Times New Roman', 16))
        self.lbl.place(relx=.5, rely=.1, anchor='center')


    def get_html(self, url):
        html_content = requests.get(url).text
        return html_content

    def get_data(self, html):
        soup = BeautifulSoup(html, 'lxml')
        # t = soup.find('div', class_ = "temp fact__temp fact__temp_size_s").find('span', class_ = "temp__value temp__value_with-unit")
        t = soup.find('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"}).find('span')
        return t.text

    def main(self):
        self.txt.delete(0, END)
        url = 'https://coinmarketcap.com/currencies/compound/'
        res = self.get_html(url)
        self.txt.insert(0, self.get_data(res))


if __name__ == '__main__':
    root = Tk()
    win = MyWindow(root)

root.mainloop()
