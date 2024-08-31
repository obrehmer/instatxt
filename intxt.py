#!/usr/bin/env python3

from openai import OpenAI
import os

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))


cam = input("Camera Model (Canon EOS 3000):  ") or "Canon EOS 3000"
obj = input("Objective (28-90 mm Zoom):  ") or "28-90 mm Zoom"
loc = input("Location: ")  
year = input("Year (2024): ") or "2024"
month = input("Month: ") 
add = input("Additions: ") 

ai_system_message = f"Schreibe einen text fuer einen instagramm Post, in englisch, mit 20 Hashtags, einfache Sprache, 2 Saetze, Schreibe aus der Beobachterperspektive neutral und professionell"

ai_user_message = f"Fotografiert mit {cam} mit {obj}, in {loc}, fotografiert im {month} in  {year},  {add} "



completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": ai_system_message},
        {"role": "user", "content": ai_user_message}
    ]
)

answer = (completion.choices[0].message.content)

print(answer)
