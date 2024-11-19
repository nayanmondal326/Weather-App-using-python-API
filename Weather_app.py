import tkinter
from tkinter import *
from tkinter import ttk
#rom tkinter import photoImage
import requests
def data_get():
    city = city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=610aabd4b54ee202a8e99dc60edfffee").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    #temp_label1.config(text=str(int(data["main"]["temp_min"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])
    hu_label1.config(text=data["main"]["humidity"])
    vi_label1.config(text=data["visibility"]/1000)
    se_label1.config(text=data["main"]["sea_level"])


win =tkinter.Tk()
win.title("weather app")
win.config(bg = "lightgreen")
win.geometry("500x700")
#image_path=photoImage(file=r"C:\Users\nayan\PycharmProjects\weatherforecast\pythonProject2")
#bg_image=tkinter.Label(win,image=image_path)
#bg_image.pack()


name_label = Label(win,text="Weather Forecast app",
                   font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
city_name=StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa",
             "Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka",
             "Kerala","kolkata","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha",
             "Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand"
    ,"West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu",
             "Lakshadweep","National Capital Territory of Delhi","Puducherry"]
###############################
com = ttk.Combobox(win,text="Weather Forecast app",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)

com.place(x=25,y=120,height=50,width=450)


w_label = Label(win,text="Weather Climate",
                   font=("Time New Roman",20))
w_label.place(x=25,y=250,height=30,width=210)
w_label1 = Label(win,text="",
                   font=("Time New Roman",20))
w_label1.place(x=250,y=250,height=30,width=210)



wb_label = Label(win,text="Weather Description",
                   font=("Time New Roman",17))
wb_label.place(x=25,y=300,height=30,width=210)
wb_label = Label(win,text="",
                   font=("Time New Roman",17))
wb_label.place(x=250,y=300,height=30,width=210)



temp_label = Label(win,text="Temperature",
                   font=("Time New Roman",22))
temp_label.place(x=25,y=350,height=30,width=210)
temp_label1 = Label(win,text="",
                   font=("Time New Roman",17))
temp_label1.place(x=250,y=350,height=30,width=210)




hu_label1 = Label(win,text="Humidity",
                   font=("Time New Roman",21))
hu_label1.place(x=25,y=400,height=30,width=210)
hu_label1 = Label(win,text="",
                   font=("Time New Roman",20))
hu_label1.place(x=250,y=400,height=30,width=210)



per_label = Label(win,text="Pressure",
                   font=("Time New Roman",23))
per_label.place(x=25,y=450,height=30,width=210)
per_label1 = Label(win,text="",
                   font=("Time New Roman",17))
per_label1.place(x=250,y=450,height=30,width=210)


vi_label = Label(win,text="Visibility",
                   font=("Time New Roman",21))
vi_label.place(x=25,y=500,height=30,width=210)
vi_label1 = Label(win,text="",
                   font=("Time New Roman",17))
vi_label1.place(x=250,y=500,height=30,width=210)


se_label = Label(win,text="Sea_level",
                   font=("Time New Roman",21))
se_label.place(x=25,y=550,height=30,width=210)
se_label1 = Label(win,text="",
                   font=("Time New Roman",17))
se_label1.place(x=250,y=550,height=30,width=210)


####################

#############
done_button=Button(win,text="Done",
                   font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)
#############

win.mainloop()
