import tkinter
from tkinter import font
from PIL import Image, ImageTk
import sqlite3
import pandas as pd
import mplfinance as mpf

from 繪製股價走勢圖.走勢圖 import save_candle_chart

def draw_chart():
    pass

def exit_form():
    root.destroy()
    root.quit()

if __name__ == '__main__':
    # save_candle_chart('2330', 20, False, mydpi=100, mav=(3, 6))
    root = tkinter.Tk()
    root.geometry("800x600")
    root.title("股價走勢圖")

    myfont = font.Font(family='Arial', size=15, weight='bold')
    myfont2 = font.Font(family='Arial', size=15)

    symbol = tkinter.StringVar()
    amount = tkinter.IntVar()

    # view 元件
    symbolLabel = tkinter.Label(root, text='股票代號', font=myfont)
    symbolEntry = tkinter.Entry(root, textvariable=symbol, font=myfont2)
    amountLabel = tkinter.Label(root, text='交易天數', font=myfont)
    amountEntry = tkinter.Entry(root, textvariable=symbol, font=myfont2)
    drawButton = tkinter.Button(root, text='繪圖', command=lambda: draw_chart(), font=myfont)
    exitButton = tkinter.Button(root, text='離開',command=lambda: exit_form(), font=myfont)
    chartLabel = tkinter.Label(root, font=myfont)

    root.rowconfigure(1, weight=1)
    root.columnconfigure((4, 5), weight=1)

    # view 元件布局
    symbolLabel.grid(row=0, column=0, sticky='EWNS')
    symbolEntry.grid(row=0, column=1, sticky='EWNS')
    amountLabel.grid(row=0, column=2, sticky='EWNS')
    amountEntry.grid(row=0, column=3, sticky='EWNS')
    drawButton.grid(row=0, column=4, sticky='EWNS')
    exitButton.grid(row=0, column=5, sticky='EWNS')
    chartLabel.grid(row=1, column=0, columnspan=6, sticky='EWNS')

    root.mainloop()




