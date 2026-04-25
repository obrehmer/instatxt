#!/usr/bin/env python3

from openai import OpenAI
import os

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

from openai import OpenAI

client = OpenAI()

models = client.models.list()

for m in models.data:
    print(m.id)
