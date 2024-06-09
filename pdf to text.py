import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo, showerror

import PyPDF2
import pytesseract as tess
from PIL import Image

window = tk.Tk()
window.title("PDF to text converter")

def openfile():
    file = askopenfile(filetypes=[('PDF Files', '*.pdf')])
    if file:
        try:
            with open(file.name, 'rb') as pdf_file:
                read_pdf = PyPDF2.PdfReader(pdf_file)
                page_content = ""
                for page in read_pdf.pages:
                    try:
                        page_content += page.extract_text() or ""
                    except Exception as e:
                        showerror("Error", f"An error occurred while extracting text from page: {e}")
                        return
                with open('content.txt', 'w', encoding='utf-8') as f:
                    f.write(page_content)
            showinfo("Done", "Successfully Converted")
        except Exception as e:
            showerror("Error", f"An error occurred while reading the PDF file: {e}")
def ocrfile():
    try:
        tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as necessary
    except Exception as e:
        showerror("Error", "Tesseract is not installed or it's not in your PATH. Please install Tesseract OCR.")
        return

    file = askopenfile(filetypes=[('PNG Files', '*.png'), ('JPG Files', '*.jpg')])
    if file:
        try:
            img = Image.open(file.name)
            text = tess.image_to_string(img)
            with open("imgtext.txt", "w", encoding='utf-8') as f:
                f.write(text)
            showinfo("Done", "Successfully Converted")
        except Exception as e:
            showerror("Error", f"An error occurred while performing OCR: {e}")


label = tk.Label(window, text="Choose pdf file: ")
label.grid(row=0, column=0, padx=5, pady=5)

button = ttk.Button(window, text="Select", width=30, command=openfile)
button.grid(row=0, column=1, padx=5, pady=5)

label = tk.Label(window, text="Choose image file: ")
label.grid(row=1, column=0, padx=5, pady=5)

button = ttk.Button(window, text="Select", width=30, command=ocrfile)
button.grid(row=1, column=1, padx=5, pady=5)

window.mainloop()
