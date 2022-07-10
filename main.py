from tkinter import filedialog
import zipfile
import tkinter as tk
from tkinter import filedialog
import os

def getDestinationFolder():
  root = tk.Tk()
  root.withdraw()
  selected_folder = filedialog.askdirectory()
  return selected_folder



if __name__ == "__main__":
  dest = getDestinationFolder()
  os.chdir(dest)
  for root, dirs, files in os.walk(".", topdown=False):
    for file in files:
        if not zipfile.is_zipfile(file):
            filename = file.split('.')[0]
            with zipfile.ZipFile(f'{filename}.zip', 'w') as myzip:
                myzip.write(file)
            os.remove(file)