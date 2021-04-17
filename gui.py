import tkinter
from tkinter import *
top = tkinter.Tk()

import pandas as pd
import pickle

pickle_off = open ("final_model.pkl", "rb")
emp = pickle.load(pickle_off)
print(emp)

top.title('DDos Attack Prediction')

def pred():
    datapoint = pd.DataFrame({"src_port": [src_port.get()],
    "dst_port":[dst_port.get()],
    "flow_duration":[flow_d.get()],
    "tot_fwd_pkts":[tfp.get()],"tot_bwd_pkts":[tbp.get()],"totLen_fwd_pkts": [tlfp.get()],"totLen_bwd_pkts":[tlbp.get()],
     "fwd_pkts_per_s": [fps.get()], "bwd_pkts_per_s": [bps.get()]})
    
    print(emp.predict(datapoint)[0])
    return my_string_var.set("It's a DDoS Attack") if emp.predict(datapoint)[0] == 1 else my_string_var.set("Not a DDoS Attack")

mylabel = Label(top, text="Source Port:").grid(row=1, column=0)
src_port = Entry(top,width=50)
src_port.grid(row=1,column=1)
def clicked():
      res = "Welcome to " + txt.get()
      l1.configure(text= res)

mylabel = Label(top, text="Destination Port:").grid(row=1, column=2)
dst_port = Entry(top,width=50)
dst_port.grid(row=1,column=3)
def clicked():
      res = "Welcome to " + txt.get()
      l1.configure(text= res)


mylabel = Label(top, text="Flow Duration:").grid(row=3, column=2)
flow_d = Entry(top,width=50)
flow_d.grid(row=3,column=3)
def clicked():
      res = "Welcome to " + txt.get()
      l1.configure(text= res)

mylabel = Label(top, text="Total Forwarded Packets:").grid(row=4, column=0)
tfp = Entry(top,width=50)
tfp.grid(row=4,column=1)
def clicked():
      res = "Welcome to " + txt.get()
      l1.configure(text= res)

mylabel = Label(top, text="Total Backwarded Packets:").grid(row=4, column=2)
tbp = Entry(top,width=50)
tbp.grid(row=4,column=3)
def clicked():
      res = "Welcome to " + txt.get()
      l1.configure(text= res)

mylabel = Label(top, text="Total Length of Forwarded Packets:").grid(row=5, column=0)
tlfp = Entry(top,width=50)
tlfp.grid(row=5,column=1)
def clicked():
      res = "Welcome to " + txt.get()
      l1.configure(text= res)






mylabel = Label(top, text="Total Length of Backwarded Packets:").grid(row=5, column=2)
tlbp = Entry(top,width=50)
tlbp.grid(row=5,column=3)
def clicked():
      res = "Welcome to " + txt.get()
      l1.configure(text= res)





mylabel = Label(top, text="Forward Packets per sec:").grid(row=6, column=0)
fps = Entry(top,width=50)
fps.grid(row=6,column=1)
def clicked():
      res = "Welcome to " + txt.get()
      l1.configure(text= res)

mylabel = Label(top, text="Backward Packets per sec:").grid(row=6, column=2)
bps = Entry(top,width=50)
bps.grid(row=6,column=3)
def clicked():
      res = "Welcome to " + txt.get()
      l1.configure(text= res)


enter = Button(top, text = "Enter", borderwidth = 1, width=10, height=1, command=pred ).grid(row = 7,column = 2)

my_string_var = StringVar()
my_string_var.set("Your Predicted value will be here!")

my_label = Label(top, textvariable = my_string_var).grid(row=7, column=0)

top.mainloop()