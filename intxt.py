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

ai_system_message = f"Write a text for an instagram post, in English, with 20 hashtags, simple language, 2 sentences, write from the observer's perspective, neutral and professional. You are a photographer. I need your assistance! Do not use 'my', use 'a' instead."

ai_user_message = f"taken with {cam} with a lens {obj}, in {loc}, in the {month} of  {year},  {add} "



completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": ai_system_message},
        {"role": "user", "content": ai_user_message}
    ]
)

answer = (completion.choices[0].message.content)

print(answer)
