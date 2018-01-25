from tkinter import filedialog
from tkinter import *
import shutil
import os
import datetime
import time
import argparse
import ftplib


#######################################################
#Customized version of fileextractor with Tkinter GUI.#
#######################################################
def search_copy_files(source, destination, extension, logger):
	logger.insert(END,"Searcning and copying files from Source: "+source+" to Destination: "+destination)
	logger.see(END)
	if not os.path.exists(destination):
		os.makedirs(destination)
	for root, directories, filenames in os.walk(source):
		for filename in filenames:
			if extension != None:
				if filename.endswith(extension):
					_copy_file(root,filename,destination,logger)
			else:
				_copy_file(root,filename,destination,logger)
	logger.insert(END,"Finisned copying all files. Please check the destination folder:"+destination+"\n")
	logger.see(END)

def _copy_file(root, filename, destination, logger):
	try:
		shutil.copy(os.path.join(root,filename),destination)
	except Exception as e:
		logger.insert(END,e)
		logger.see(END)
		pass
	finally:
		logger.insert(END,"copied "+os.path.join(destination,filename)+"\n")
		logger.see(END)

#############
#Tkinter GUI#
#############
def src_button():
	global src_path
	filename = filedialog.askdirectory()
	src_path.set(filename)
	
def dest_button():
	global dest_path
	filename = filedialog.askdirectory()
	dest_path.set(filename)

def run_button():
	search_copy_files(src_path.get(),dest_path.get(),extension.get(), text)

#main window
root = Tk()
root.title("File Extractor v1.0 | me@kunxia.com")
root.geometry('700x450')
root.resizable(False, False)


#source directory picker
src_path = StringVar()
src_path.set("Please choose the source directory where you want to extract file from")
srcLbl = Label(master=root,textvariable=src_path, anchor='w')
srcLbl.grid(row=0, column=2, columnspan=3, sticky=W)
srcBtn = Button(text="Source Directory", command=src_button)
srcBtn.grid(row=0, column=1)

#destination directory picker
dest_path = StringVar()
dest_path.set("Please specify the output directory where you want to copy files to")
destLbl = Label(master=root,textvariable=dest_path, anchor='w')
destLbl.grid(row=1, column=2, columnspan=5, sticky=W)
destBtn = Button(text="Output Directory", command=dest_button)
destBtn.grid(row=1, column=1)

#file extension input
extension = StringVar()
extLbl = Label(master=root,text="File Extension")
extLbl.grid(row=3, column=1,sticky=W)
extBox = Entry(master=root, textvariable=extension)
extBox.grid(row=3, column=2, sticky=W)

#Run File Extraction
runBtn = Button(text="Extract Files", command=run_button)
runBtn.grid(row=4, column=2, sticky=W)

#Log output
log = StringVar()
text = Text(master=root, wrap=WORD)
text.tag_configure("center", justify='center')
text.grid(row=5,column=2, columnspan=3, sticky=W)
text.insert(END, "File Extrator helps you extract files from the source directory including sub-folders and save them to the output directory.\n")

mainloop()

