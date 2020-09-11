import os
import datetime
from playsound import playsound
import time,random,json
from boltiot import Bolt
from win32com.client import Dispatch
import requests
api_key = '1b9bfa86-07f0-4387-91f3-5a65c3547ff7'
device_id  = 'BOLT14917480'
mybolt = Bolt(api_key, device_id)
speak = Dispatch("SAPI.Spvoice")
os. system('clear')
def alarm():
    '''
    this function take input to setup time to wake up
    '''
    alarmH = int(input("What hour do you want the alarm to ring? "))# INPUT HOUR 
    alarmM = int(input("What minute do you want the alarm to ring? "))#INPUT MINUITES
    amPm = str(input("am or pm? "))# INPUT AM OR PM
    os. system('clear')
    print("Waiting for alarm",alarmH,alarmM,amPm)
    if (amPm == "pm"):
        alarmH = alarmH + 12 #FOR 12 HR FORMAT
    while(1==1):
        if(alarmH == datetime.datetime.now().hour and
           alarmM == datetime.datetime.now().minute) :
            print("Time to wake up")
            playsound("c:/Users/Administrator/Desktop/project/beep.mp3")#PLAY ALRAM SOUND 
            break
            
def light_on():
    mybolt.digitalWrite(0, 'HIGH')#TO TURN ON LIGHT 
def room_temp():
    r = mybolt.analogRead('A0') 
    data = json.loads(r)
    a=int(data['value'])/10#CONVERTING VOLTS INTO CELSIUS
    temp='temprature is ',a,'°Celsius'
    speak.Speak(temp)# SPEAKS OUT ROOM TEMPRATURE 

def NewsFromBBC():
        main_url="https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=0eb059f83a044e08b8c23679882e27e6"#API TO FETCH NEWS 
        open_bbc_page = requests.get(main_url).json() 
        article = open_bbc_page["articles"] 
        results = [] 
        for ar in article:
                results.append(ar["title"]) 
        for i in range(len(results)):    
                print(i + 1, results[i])          
        morning ="Today's news are as follow"
        speak.Speak(morning)
        speak.Speak(results)# SPEAKS OUT NEWS                  
 
if __name__ == '__main__': 
# FUNCTION CALLING      
    alarm()
    light_on()
    room_temp()
    NewsFromBBC() 
