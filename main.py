
import pyttsx3
import os
import openai


openai.api_key = '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'
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
                                          {"role": "user", "content":"Two lines on India"}])
engine = pyttsx3.init()

engine.say(completion.choices[0].message.content)
engine.runAndWait()

