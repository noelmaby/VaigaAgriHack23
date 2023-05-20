from tkinter import *
import tkinter as tk 
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import requests,json
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
from twilio.rest import Client
from time import strftime
import time


#sent audio
def urgent_audio():
    account_sid = 'AC746f7dcc671a8c470b16ce9c311b1b1a'
    auth_token = '9cbff2a4852c6dea8c19e57ab673411a'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    media_url="https://carmine-alligator-5860.twil.io/assets/Urgent.aac",
    to='whatsapp:+919495072672'
    )

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    media_url="https://carmine-alligator-5860.twil.io/assets/Urgent.aac",
    to='whatsapp:+919188721804'
    )

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    media_url="https://carmine-alligator-5860.twil.io/assets/Urgent.aac",
    to='whatsapp:+917306100596'
    )

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    media_url="https://carmine-alligator-5860.twil.io/assets/Urgent.aac",
    to='whatsapp:+919920527457'
    )

    print(message.sid)



def sadha_audio():
    account_sid = 'AC746f7dcc671a8c470b16ce9c311b1b1a'
    auth_token = '9cbff2a4852c6dea8c19e57ab673411a'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    media_url="https://carmine-alligator-5860.twil.io/assets/Saadha.aac",
    to='whatsapp:+919495072672'
    )

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    media_url="https://carmine-alligator-5860.twil.io/assets/Saadha.aac",
    to='whatsapp:+919188721804'
    )

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    media_url="https://carmine-alligator-5860.twil.io/assets/Saadha.aac",
    to='whatsapp:+917306100596'
    )

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    media_url="https://carmine-alligator-5860.twil.io/assets/Saadha.aac",
    to='whatsapp:+919920527457'
    )

    print(message.sid)




def liveaudio_whatsapp():
    account_sid = 'AC746f7dcc671a8c470b16ce9c311b1b1a'
    auth_token = '9cbff2a4852c6dea8c19e57ab673411a'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    media_url="https://carmine-alligator-5860.twil.io/assets/Message.aac",
    to='whatsapp:+919495072672'
    )

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    media_url="https://carmine-alligator-5860.twil.io/assets/Message.aac",
    to='whatsapp:+919188721804'
    )

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    media_url="https://carmine-alligator-5860.twil.io/assets/Message.aac",
    to='whatsapp:+917306100596'
    )

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    media_url="https://carmine-alligator-5860.twil.io/assets/Message.aac",
    to='whatsapp:+919920527457'
    )

    print(message.sid)


#live detetction
def live():
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_Model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # CAMERA can be 0 or 1 based on default camera of your computer
    camera = cv2.VideoCapture(0)

    c=0

    while True:
        # Grab the webcamera's image.
        ret, image = camera.read()

        # Resize the raw image into (224-height,224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Show the image in a window
        cv2.imshow("Webcam Image", image)

        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predicts the model
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        #counting bph
        if ( str(np.round(confidence_score * 100))[:-2]=="100"):
            c=c+1

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
        print("no of bph detected = ",c)

        


        # q for exit
        if cv2.waitKey(1)==ord('q'):
            break

    
    if c>=100:
        liveaudio_whatsapp()
    camera.release()
    cv2.destroyAllWindows()

apiKey="7a6dac120407a958efed1fec1f82e5c7"

baseurl = "https://api.openweathermap.org/data/2.5/weather?lat="
 
r=requests.get('https://get.geojs.io/')
ip_request=requests.get('https://get.geojs.io/v1/ip.json')
ipAdd=ip_request.json()['ip']
print("ip address =",ipAdd)

url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
geo_request = requests.get(url)
geo_data=geo_request.json()
print("longitude =",geo_data.get('longitude'))
print("latitude = ",geo_data.get('latitude'))

lati=geo_data.get('latitude')

longi=geo_data.get('longitude')

completeurl= baseurl + str(lati) + "&lon="+str(longi)+"&appid="+apiKey

response = requests.get(completeurl) 

data = response.json()
temp=data.get('main').get('temp')
humi=data.get('main').get('humidity')
temp=temp-273.15
print("temperature =",int(temp),"C")
print("humidity =",humi)

#Tkinter window
root=Tk()
root.title("farmer friend")
root.geometry("590x270+300+300")
root.configure(bg="#203243")
root.resizable(False,False)

#area
label0=Label(root,text="LOCATION                             ",font=('Calibri',11),fg="white",bg="#203243")
label0.place(x=50,y=20)

label1=Label(root,text="Longitude   :",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=50,y=40)

label2=Label(root,text="Latitude      :",font=('Helvetica',11),fg="white",bg="#203243")
label2.place(x=50,y=60)

label3=Label(root,text= geo_data.get('longitude')       ,font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=150,y=40)

label4=Label(root,text=geo_data.get('latitude'),font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=150,y=60)

#temp humidity
label05=Label(root,text="WEATHER FORECAST  ",font=('Calibri',11),fg="white",bg="#203243")
label05.place(x=50,y=100)


label5=Label(root,text="Temperature:",font=('Helvetica',11),fg="white",bg="#203243")
label5.place(x=50,y=120)

label6=Label(root,text="Humidity       :",font=('Helvetica',11),fg="white",bg="#203243")
label6.place(x=50,y=140)

label7=Label(root,text= int(temp)       ,font=('Helvetica',11),fg="white",bg="#203243")
label7.place(x=150,y=120)
label07=Label(root,text= "C"       ,font=('Helvetica',11),fg="white",bg="#203243")
label07.place(x=170,y=120)

label8=Label(root,text=humi,font=('Helvetica',11),fg="white",bg="#203243")
label8.place(x=150,y=140)

#time and date
def clock():
    hour=time.strftime("%H")
    minute=time.strftime("%M")
    second=time.strftime("%S")
    day=time.strftime("%A")
    am_pm=time.strftime("%p")


    time_label.config(text=hour+":"+minute+":"+second+" "+am_pm)
    time_label.after(1000,clock)

    time_label1.config(text=day)

def update():
    time_label.config(text="new")


time_label=Label(root,text="",font=("Helvetica",15),fg="white",bg="black")
time_label.place(x=445,y=230)

time_label1=Label(root,text="",font=("Helvetica",14))
time_label1.place(x=90,y=180)
clock()
#time_label.after(5000,update)

if int(temp)>=25 and humi>=60 :
    label9=Label(root,text="High temperature and Humidity detected !! \n Urgent precaution Needed ",font=('Helvetica',11),fg="white",bg="#203243")
    label9.place(x=50,y=180)
    urgent_audio()
elif int(temp)>=25:
    label10=Label(root,text="High temperature detected !! \n precaution Needed ",font=('Helvetica',11),fg="white",bg="#203243")
    label10.place(x=50,y=180)
    sadha_audio()
elif humi>=60:
    label11=Label(root,text="High Humidity detected !! \n precaution Needed ",font=('Helvetica',11),fg="white",bg="#203243")
    label11.place(x=50,y=180)
    sadha_audio()




#window close button
close_button=Button(root, text= "Close", font=("Calibri",14,"bold"), command=root.destroy)
close_button.place(x=500,y=20)


#live detection button    
live_dect=Button(root,text="Live detector",font=("Calibri",14,"bold"),command=live)
live_dect.place(x=300,y=20)

root.mainloop()
