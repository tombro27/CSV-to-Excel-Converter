import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300, bg = '#708090', relief = 'raised')
canvas1.pack()

def getCSV():
    global df
    filePath= filedialog.askopenfilename()
    df = pd.read_csv(filePath)
    #df.to_excel('output.xlsx',encoding='utf-8',index=False)

def saveXlsx():
    outFilePath=filedialog.asksaveasfile(filetypes=(("Excel files", "*.xlsx"),("All files", "*.*") ))
    df.to_excel(outFilePath.name + ".xlsx",index=False)

browseButton= tk.Button(text="Open CSV File", command=getCSV, bg='#5F9EA0', fg='white',font=('helvetica', 12, 'bold'))
saveButton= tk.Button(text="Save as", command=saveXlsx, bg='#2E8B57', fg='white',font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 100, window=browseButton)
canvas1.create_window(150, 200, window=saveButton)
root.mainloop()