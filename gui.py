import tkinter
from tkinter import *
top = tkinter.Tk()

import pandas as pd
import pickle

pickle_off = open ("final_model.pkl", "rb")
emp = pickle.load(pickle_off)
print(emp)

top.title('DDos Attack Prediction')