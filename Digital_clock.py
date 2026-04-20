from tkinter import *
import datetime
def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")



    Lab_hr.config(text = hr)
    Lab_min.config(text = min)
    Lab_sec.config(text = sec)
    Lab_am.config(text=am)
    Lab_date.config(text = date)
    Lab_month.config(text = month)
    Lab_year.config(text = year)
    Lab_day.config(text = day)
    
    Lab_hr.after(200,date_time)

clock = Tk()
clock.title(' ** Digital clock ** ')
clock.geometry('1000x600')
clock.config(bg = 'light green')

###** Clock **

Lab_hr = Label( clock,text ="00",font = ('Time New Roman', 60 ,"bold" ),  bg ='black',fg = "white" )
Lab_hr.place(x =120,y = 50,height=110,width=100)
Lab_hr_txt = Label( clock, text = "Hour", font = ('Time New Roman', 20 ,"bold" ),  bg ='black',fg = "white" )
Lab_hr_txt.place(x =120,y = 190,height=40,width=100)

Lab_min = Label( clock,text ="00",font = ('Time New Roman', 60 ,"bold" ),  bg ='black',fg = "white" )
Lab_min.place(x =340,y = 50,height=100,width=100)
Lab_min_txt = Label( clock, text = "Min.", font = ('Time New Roman', 20 ,"bold" ),  bg ='black',fg = "white" )
Lab_min_txt.place(x =340,y = 190,height=40,width=100)

Lab_sec = Label( clock,text ="00",font = ('Time New Roman', 60 ,"bold" ),  bg ='black',fg = "white" )
Lab_sec.place(x =560,y = 50,height=100,width=100)
Lab_sec_txt = Label( clock, text = "Sec.", font = ('Time New Roman', 20 ,"bold" ),  bg ='black',fg = "white" )
Lab_sec_txt.place(x =560,y = 190,height=40,width=100)

Lab_am = Label( clock,text ="00",font = ('Time New Roman', 45 ,"bold" ),  bg ='black',fg = "white" )
Lab_am.place(x =780,y = 50,height=100,width=100)
Lab_am_txt = Label( clock, text = "AM/PM", font = ('Time New Roman', 20 ,"bold" ),  bg ='black',fg = "white" )
Lab_am_txt.place(x =780,y = 190,height=40,width=100)

#########Date

Lab_date = Label( clock,text ="00",font = ('Time New Roman', 60 ,"bold" ),  bg ='black',fg = "white" )
Lab_date.place(x =120,y = 270,height=110,width=100)
Lab_date_txt = Label( clock, text = "Date", font = ('Time New Roman', 20 ,"bold" ),  bg ='black',fg = "white" )
Lab_date_txt.place(x =120,y = 410,height=40,width=100)

Lab_month = Label( clock,text ="00",font = ('Time New Roman', 60 ,"bold" ),  bg ='black',fg = "white" )
Lab_month.place(x =340,y = 270,height=100,width=100)
Lab_month_txt = Label( clock, text = "Month.", font = ('Time New Roman', 20 ,"bold" ),  bg ='black',fg = "white" )
Lab_month_txt.place(x =340,y = 410,height=40,width=100)

Lab_year = Label( clock,text ="00",font = ('Time New Roman', 60 ,"bold" ),  bg ='black',fg = "white" )
Lab_year.place(x =560,y = 270,height=100,width=100)
Lab_year_txt = Label( clock, text = "Year.", font = ('Time New Roman', 20 ,"bold" ),  bg ='black',fg = "white" )
Lab_year_txt.place(x =560,y = 410,height=40,width=100)

Lab_day = Label( clock,text ="00",font = ('Time New Roman', 30 ,"bold" ),  bg ='black',fg = "white" )
Lab_day.place(x =780,y = 270,height=100,width=100)
Lab_day_txt = Label( clock, text = "DAY", font = ('Time New Roman', 20 ,"bold" ),  bg ='black',fg = "white" )
Lab_day_txt.place(x =780,y = 410,height=40,width=100)

date_time()

clock.mainloop()
