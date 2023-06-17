import os
import sys
from engine import CompilationEngine
from tokenizer import Tokenizer
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter.filedialog import askdirectory
from tkinter import filedialog


def get_names(path):
    paths = []
    out_names = []
    if os.path.isfile(path):
        paths.append(path)
        path, tmp_name = os.path.split(path)
        name, ext = os.path.splitext(tmp_name)
        out_names.append(os.path.join(path, name + '.vm'))
        if ext != '.jack':
            print("Provided file is not a jack file.")
            sys.exit(1)
       
    elif os.path.isdir(path):
        paths = [x for x in os.listdir(path) 
                 if os.path.splitext(x)[1] == '.jack']
        names = [os.path.splitext(x)[0] for x in paths]
        paths = [os.path.join(path, x) for x in paths]
        out_names = [os.path.join(path, x + '.vm') for x in names]
    else:
        print('{} doesn\'t exist.'.format(path))
        sys.exit(1)
    return paths, out_names


def main():
    global filename
    file_paths, outnames = get_names(filename)

    for pth, out_pth in zip(file_paths, outnames):
        with open(pth, 'r') as f:
            tk = Tokenizer(f.readlines())
        engine = CompilationEngine(tk, out_pth)
        engine.compile_class()
    print("Finished compilation...")

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    main()

def browseDirectory():
    global filename
    file_path=[]
    directory_path = askdirectory()
    if directory_path:
        files = os.listdir(directory_path)
        for file_name in files:
            if file_name.endswith('jack'):
                file_path.append( os.path.join(directory_path, file_name))
        for i in file_path:
            filename=i
            main()


root=Tk()
root.title("Compiler")
root.geometry("500x300")
root.configure(bg="#FFFFFF")
frame1 = Frame(root,background="#FFFFFF",height=40,width=500)
lbl1= Label(frame1, text = "Compiler", font=('Arial',25,'bold'),bg="#FFFFFF",fg='#000FFF')
lbl1.pack()
frame1.place(x=170,y=0)
frame2=Frame(root,background="#FFFFFF",height=200,width=500)
btn1 = Button(frame2,command=browseFiles, text="open File",relief='flat',font=('Ariel',8,'bold'),height=1,bg="#000FFF",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#000FFF")
btn1.place(x=125,y=20)
btn2 = Button(frame2,command=browseDirectory, text="open directory",relief='flat',font=('Ariel',8,'bold'),height=1,bg="#000FFF",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#000FFF")
btn2.place(x=250,y=20)
frame2.place(x=0,y=40)
root.mainloop()

