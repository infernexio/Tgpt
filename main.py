import dotenv
import openai
import os
import sys

dotenv.load_dotenv()

prompt = sys.argv[1]
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = response.choices[0].text
if (message == ""):
    message = "I'm sorry, I don't understand."
print(message)