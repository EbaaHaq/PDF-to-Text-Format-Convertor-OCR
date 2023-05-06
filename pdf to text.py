import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo

import PyPDF2 as PyPDF2

window = tk.Tk()
window.title("PDF to text converter")


def openfile():
    file = askopenfile(filetypes=[('PDF Files', '*.pdf')])
    pdf_file = open(file.name, 'rb')
    read_pdf = PyPDF2.PdfReader(pdf_file)
    page = read_pdf.pages[0]
    page_content = page.extractText()
    with open('content.txt', 'w', encoding='utf-8') as f:
        f.write(page_content)
    for i in range(1, len(read_pdf.pages)):
        page = read_pdf.pages[i]
        page_content = page.extractText()
        with open('content.txt', 'a', encoding='utf-8') as fp:
            fp.write(page_content)
    showinfo("Done", "Successfully Converted")

def ocrfile():
    print("welcome to OCR")
    import pytesseract as tess
    tess.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
    from PIL import Image
    file = askopenfile(filetypes=[('PNG Files', '.png'),('JPG Files', '.jpg'),('JPG Files', '.')])
    img = Image.open(file.name)
    text = tess.image_to_string(img)
    with open("imgtext.txt", "w", encoding='utf-8') as f:
        f.write(text)
    showinfo("Done", "Successfully Converted")



label = tk.Label(window, text="Choose pdf file: ")
label.grid(row=0, column=0, padx=5, pady=5)

button = ttk.Button(window, text="Select", width=30, command=openfile)
button.grid(row=0, column=1, padx=5, pady=5)

label = tk.Label(window, text="Choose image file: ")
label.grid(row=1, column=0, padx=5, pady=5)

button = ttk.Button(window, text="Select", width=30, command=ocrfile)
button.grid(row=1, column=1, padx=5, pady=5)


window.mainloop()