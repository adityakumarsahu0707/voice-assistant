import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import googlesearch
from googlesearch import search
import smtplib
import playsound
from gtts import gTTS
import wolframalpha
from selenium import webdriver
import pyaudio
import urllib3
import random
from time import strftime
from bs4 import BeautifulSoup as soup
import re
import subprocess
from googletrans import Translator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

print("\n \n  \t\t\t\t!!Welcome to Adi's Voice Based Assistant!!\n")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! This smart Assistant is ready to help you.")
    elif hour>=12 and hour<18:
        speak("Good Afternoon! This smart Assistant is ready to help you.")
    else:
        speak("Good Evening! This smart assistant is ready to help you.")

#Global Listener
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 5
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Please wait, Processing...")
        query = r.recognize_google(audio, language='en')
        print(f"\nCommand Recognized: {query}\n")
    except Exception as e:
        # print(e)
        print("\nSay that again please...")
        return "None"
    return query

#AWS Main menu listener
def awscommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening for your Command...")
        #speak("AWS is Listening")
        r.pause_threshold = 5
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Processing your selection...")
        query1 = r.recognize_google(audio, language='en')
        print(f"\nSelected option: {query1}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query1

#EC2 listener
def ec2command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening for your EC2 Command...")
        #speak("AWS is Listening")
        r.pause_threshold = 5
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Processing your command...")
        query1_1 = r.recognize_google(audio, language='en')
        print(f"\nCommand Recieved for EC2: {query1_1}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query1_1



#Key Listener
def keycommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening for your Key Command...")
        #speak("AWS is Listening")
        r.pause_threshold = 5
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Processing your command...")
        query1_2 = r.recognize_google(audio, language='en')
        print(f"\nCommand Recieved for Key : {query1_2}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query1_2



#EBS Listener
def ebscommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening for your EBS Command...")
        #speak("AWS is Listening")
        r.pause_threshold = 5
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Processing your command...")
        query1_3 = r.recognize_google(audio, language='en')
        print(f"\nCommand Recieved for EBS: {query1_3}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query1_3


#EC2 Instance Defination 

def imagef():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nImage")
        audioe1 = r.listen(source)
    try:
        image= r.recognize_google(audioe1, language='en')
        print(f"Command Recognized: {image}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return image

def countf():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nCount : ")
        audioe2 = r.listen(source)
    try:
        count = r.recognize_google(audioe2, language='en')
        print(f"\nCommand Recognized: {count}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return count

def subnetf():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nSubnet : ")
        audioe3 = r.listen(source)
    try:
        subnet = r.recognize_google(audioe3, language='en')
        print(f"Command Recognized: {subnet}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return subnet

def keyf():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nKey Name : ")
        audioe4 = r.listen(source)
    try:
        keyy = r.recognize_google(audioe4, language='en')
        print(f"Command Recognized: {keyy}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return keyy

def tagf():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nName of Instance : ")
        audioe5 = r.listen(source)
    try:
        tag = r.recognize_google(audioe5, language='en')
        print(f"Command Recognized: {tag}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return tag    

def typef():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nType of Instance : ")
        audioe6 = r.listen(source)
    try:
        typee = r.recognize_google(audioe6, language='en')
        print(f"Command Recognized: {typee}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return typee


#EC2 END DEFINATION



if __name__ == "__main__":
    wish()
    print("\n \tTo see what services we provide, SPEAK 'AVAILABLE SERVICES'\n\tTo terminate the program,either Speak 'exit' or 'close' or press 'ctrl + c' \n")
    while True:
        query = takeCommand().lower()
#Wikipedia       
        if ('information' in query) or ('tell me something about' in query) or ('about' in query) or ('wikipedia' in query):
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            translator = Translator()
            result = translator.translate(results, dest='hi')
            pyttsx3.speak("According to Wikipedia, here are some results.")
            print(results)
            rd_ch=input("\n Do you want me to read it out? [y/n]: ")
            if (rd_ch=='y') or (rd_ch=='Y'):
                speak(results)
            elif (rd_ch=='n') or (rd_ch=='N'):
                print("Okay Thanks..")
            else:
                print('invalid Keypress.')
            

#Notepad
        elif 'notepad' in query:
            pyttsx3.speak("Opening Notepad")
            os.system("notepad")
            print(' ')
        
#Chrome
        elif 'chrome' in query:
                pyttsx3.speak("Opening Chrome Browser")
                os.system("chrome")
                print('')
                pause=input("____________________________________________________________________")

#AWS START
        elif ('start aws' in query) or ('use aws' in query) or ('start a w s' in query) or ('web service' in query) or ('web services' in query) or ('Amazon Web Services' in query) or ('aws' in query) or ('a w s' in query) or ('use a w s' in query) or ('aws services' in query) or ('a w s services' in query) or ('e w s services' in query) or ('aw' in query) or ('WS services' in query):
          print("\nConverting command to : start AWS services\n")
          print("\nWelcome to AWS CLI speech services...", end='\n')
          pyttsx3.speak("Welcome to AWS CLI services.")
          print("We provide these services: \n 1) EC2 (Launch stopped instance, Create instance and List all available instances) \n 2) Key(Creating new key pair, deleting existing pair and listing available keys) \n 3) EBS(Creating EBS volume, deleting volume, Attach & detach volume) \n")

          while True:

            query1=awscommand().lower()
    #EC2
            if ('ec2' in query1) or ('easy to' in query1) or ('1' in query1) or ('first' in query1):
                print("You are inside EC2 SERVICE.\nAvailable options:\n\ta) Start/Launch stopped instance\n\tb) Create new instance(default 10Gb storage)\n\tc) List all instances\n\td) Terminate instance") #\n\td) Create new instance(of custom storage)
                speak("Entered into EC2 services")
                while True:
                    query1_1=ec2command().lower()
                    if (('stopped' in query1_1) or ('start' in query1_1)): # and (('instance' in query1_1) or ('instances' in query1_1)):
                        speak("Enter instance id you want to start")
                        ec2id=input("Enter Instance Id : ")
                        os.system(f"aws ec2 start-instances --instance-ids {ec2id}")
                        speak("Instance is starting")
                        pause=input("____________________________________________________________________")

                    elif (('new' in query1_1)  or ('create' in query1_1) or ('launch new instance' in query1_1)): # and (('instance' in query1_1) or ('instances' in query1_1)):
                        #print ("\n\tNote: By default we are creating storage of 10Gb and type of instance as t2.micro for billing purpose.\n")
                        speak("Tell me the following details")
                        while True:
                            imagef()
                            #im=input("Is information Correct? [y/n/enter manually]: ")
                            print("Is information Correct? [y/n/enter manually(em)]: ")
                            im=input()
                            if ('y' in im):
                                image="ami-052c08d70def0ac62"
                                break
                            elif('enter' in im) or ('manually' in im) or ('em' in im):
                                image=input("Enter Key Name : ")
                                break                               
                            else:
                                print("Okay re-enter")
                                continue

                        while True:
                            typef()
                            #ty=input("Is information Correct? [y/n/enter manually]: ")
                            print("Is information Correct? [y/n/enter manually(em)]: ")
                            ty=input()                            
                            if ('y' in ty):
                                typee="t2.micro"
                                break
                            elif('enter' in ty) or ('manually' in ty) or ('em' in ty):
                                typee=input("Enter Key Name : ")
                                break                               
                            else:
                                print("Okay re-enter")
                                continue
                        while True:
                            countf()
                            #cou=input("Is information Correct? [y/n/enter manually]: ")
                            print("Is information Correct? [y/n/enter manually(em)]: ")
                            cou=input()                            
                            if ('y' in cou):
                                count=int("1")
                                break
                            elif('enter' in cou) or ('manually' in cou) or ('em' in cou):
                                count=input("Enter Key Name : ")
                                break                               
                            else:
                                print("Okay re-enter")
                                continue
                        while True:
                            subnetf()
                            #sub=input("Is information Correct? [y/n/enter manually]: ")
                            print("Is information Correct? [y/n/enter manually(em)]: ")
                            sub=input()                            
                            if ('y' in sub):
                                subnet="subnet-878d87ef"
                                break
                            elif('enter' in sub) or ('manually' in sub) or ('em' in sub):
                                subnet=input("Enter Key Name : ")
                                break                               
                            else:
                                print("Okay re-enter")
                                continue
                        while True:
                            tagf()
                            #iname=input("Is information Correct? [y/n/enter manually]: ")
                            print("Is information Correct? [y/n/enter manually(em)]: ")
                            iname=input()                            
                            if ('y' in iname):
                                tag="Test3"
                                break
                            elif('enter' in iname) or ('manually' in iname) or ('em' in iname):
                                tag=input("Enter Key Name : ")
                                break
                            else:
                                print("Okay re-enter")
                                continue
                        while True:
                            keyf()
                            #ky=input("Is information Correct? [y/n/enter manually]: ")
                            print("Is information Correct? [y/n/enter manually(em)]: ")
                            ky=input()                            
                            if ('y' in ky):
                                keyy="hadoopkeyid2"
                                break
                            elif('enter' in ky) or ('manually' in ky) or ('em' in ky):
                                keyy=input("Enter Key Name : ")
                                break
                            else:
                                print("Okay re-enter")
                                continue
                        print("____________________________________________________________________")
                        print(f"Instance is being created with the following information:\nimage: {image} ami-052c08d70def0ac62 \ntypee: {typee} \ncount: {count} \nsubnet: {subnet} ap-south-1a \nname : {tag} \nKey : {keyy} ")#\nsubnet : subnet-878d87ef 
                        print("____________________________________________________________________")
                        speak("Creating Instance")
                        os.system(f"aws ec2 run-instances --image-id {image} --instance-type {typee} --count {count} --subnet-id {subnet} --security-group-ids sg-0c3b45eedda355852 --tag-specifications ResourceType=instance,Tags=[{{Key=Name,Value={tag}}}] --key-name {keyy}") #.format(image,typee,count,subnet,tag,keyy)
                        
                        #os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --count 1 --subnet-id subnet-878d87ef --security-group-ids sg-0c3b45eedda355852 --tag-specifications ResourceType=instance,Tags=[{Key=Name,Value='Test2'}] --key-name hadoopkeyid2")
                        speak("Operation Completed")

                        pause=input("____________________________________________________________________")

                    elif ('show instance' in query1_1) or ('list' in query1_1) or ('view' in query1_1) or ('show' in query1_1) or ('see' in query1_1) or ('describe' in query1_1):
                        speak("Listing available instances")
                        os.system("aws ec2 describe-instances --output table")
                        #skip=input("Press any key to continue.")
                        pause=input("____________________________________________________________________")

                    elif ('stop' in query1_1):
                        speak("Enter instance id you want to stop")
                        ec2id=input("Enter Instance Id : ")
                        speak("Instance is being stopped")
                        os.system(f"aws ec2 stop-instances --instance-ids {ec2id}")
                        pyttsx3.speak("Operation Completed successfully")
                        pause=input("____________________________________________________________________")

                    elif ('terminate' in query1_1):
                        tid=input("Enter Instance Id : ")
                        speak("Terminating the instance")
                        os.system(f"aws ec2 terminate-instances --instance-ids {tid}")
                        pause=input("____________________________________________________________________")

                    elif  ('back to menu' in query1_1) or ('back' in query1_1) or('back aws menu' in query1_1):
                        speak("okay getting back to aws menu")
                        break

                    elif (('exit' in query1_1) or  ('close' in query1_1) or ('shut' in query1_1)) and ('program' in query1_1):
                        speak("Thankyou for using this service")
                        sys.exit("\n\nTHANKYOU, It was amazing to help you out.")

                    else:
                        print("Sorry, Invalid EC2 input.")

    #Key

            elif ('key' in query1) or ('2' in query1) or ('second' in query1) or ('two' in query1):
                print("You are inside KEY SERVICE.\nAvailable options:\n\ta) Create new Key pair\n\tb) Delete available key pair\n\tc) List all keys available\n\n")
                speak("Entered into Key services")
                while True:
                    query1_2=keycommand().lower()
                    if ('Create' in query1_2) or ('new key' in query1_2) or ('create' in query1_2):
                        print("\n")
                        speak("Enter a unique key-name you want to create.")
                        keycreate=input("Enter Unique Keyname: ")
                        pyttsx3.speak("Key Creation is in process..")
                        os.system(f"aws ec2 create-key-pair --key-name {keycreate}")
                        speak("Operation Completed.")
                        pause=input("____________________________________________________________________")

                    elif ('delete key' in query1_2) or ('delete' in query1_2):
                        speak("Enter keyname you want to delete")
                        keydelete=input("Enter key you want to delete: ")
                        pyttsx3.speak("Deleting selected key, that is,  "+ keydelete)
                        os.system(f"aws ec2 delete-key-pair --key-name {keydelete}")
                        speak("Operation Completed")
                        pause=input()

                    elif ('show key' in query1_2) or ('list' in query1_2) or ('show' in query1_2):
                        speak("Listing available Keys")
                        os.system("aws ec2 describe-key-pairs --key-name")
                        pause=input()
                        
                    elif  ('back to menu' in query1_2) or ('back' in query1_2) or('back aws menu' in query1_2):
                        speak("okay getting back to aws menu")
                        break

                    elif (('exit' in query1_2) or  ('close' in query1_2) or ('shut' in query1_2)) and ('program' in query1_2):
                        speak("Thankyou for using this service")
                        sys.exit("\n\nTHANKYOU, It was amazing to help you out.")

                    else:
                        print("Sorry, Invalid KEY input.")

    #EBS

            elif('ebs' in query1) or ('e b s' in  query1) or ('3' in  query1) or ('third' in  query1) or ('three' in query1):
                print("You are inside EBS SERVICE.\nAvailable options:\n\ta)Creating EBS volume\n\tb) Deleting available volume\n\tc)Attach volume to an instance\n\td) Detach volume from instance")
                speak("Entered into EBS services")
                while True:
                    query1_3=ebscommand().lower()
                    if ('create' in query1_3) :
                        print("Creating EBS Volume")
                        pause=input("____________________________________________________________________")
 
                    elif ('back to menu' in query1_3) or ('back' in query1_3) or ('back aws menu' in query1_3):
                        speak("okay getting back to aws menu")
                        break

                    elif (('exit' in query1_3) or  ('close' in query1_3) or ('shut' in query1_3)) and ('program' in query1_3):
                        speak("Thankyou for using this service")
                        sys.exit("\n\nTHANKYOU, It was amazing to help you out.")
                    else:
                        print("Sorry, Invalid EBS input.")

            elif('back to menu' in query1) or ('back' in query1) or ('back aws menu' in query1):
                speak("okay getting back to main menu")
                break

            elif (('exit' in query1) or  ('close' in query1) or ('shut' in query1)) and ('program' in query1):
                speak("Thankyou for using this service")
                sys.exit("\n\nTHANKYOU, It was amazing to help you out.")

            else:
                print("Sorry invalid choice or speech_recognition, please TRY AGAIN!! ")
#awsEnd

#Google Search
        elif('search result' in query) or ('google search' in query) or ('top search' in query):
            query=query.replace('google', "")
            query=query.replace('search', "")
            query=query.replace('for', "")
            query=query.replace('top', "")
            query=query.replace('result', "")
            query=query.replace('results', "")
            query=query.replace('about', "")
            speak("Enter what search result you want to get:")
            query=input("Enter Search query : ")
            speak("Searching and printing top 10 google search result")
            for j in search(query, num=10, stop=10, pause=2):
                print('\t' + j)
            pause=input("____________________________________________________________________")
#Services
        elif ('available' in query) and (('services' in query) or ('service' in query)):
            print("\n \n \t\t I provide the following services:\n\n -Searching from WIKIPEDIA \n -Top 10 Google Search results \n -AWS Services \n -NOTEPAD \n -CHROME \n -Opening Directory from your drive \n\n")
            speak('I provide these services')
            pause=input("____________________________________________________________________")

#clear screen
        elif('clear' in query) or ('clear screen' in query):
            pyttsx3.speak("Wait.. Clearing out screen")
            os.system("cls")
#EXIT
        elif ('exit' in query) or ('close' in query) or ('back' in query) or ('shutdown' in query) or ('shut down' in query):
            speak("Thankyou, for using this service.")
            break
        elif ('doing well' in query) or ('nice job' in query) or ('Thankyou' in query) or ('thankyou' in query) or ('thank you' in query) or ('thanks' in query):
            speak("It was my pleasure helping you out.")

        else:
            print("sorry..command not available..")
