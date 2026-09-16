from google import genai
import os
from dotenv import load_dotenv
#from voice import speak

load_dotenv()

gemini_api = os.getenv("GEMINI_API_KEY")




# Initialize the client
client = genai.Client(api_key=gemini_api) 

# Call the API using the fastest current model
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='Write a haiku about writing Python code.'
)

print(response.text)
#speak(response.text)