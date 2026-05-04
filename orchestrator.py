import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: No API Key found in .env")
else:
    client = genai.Client(api_key=api_key)

    def create_workflow_plan(user_input):
        # We use 'gemini-1.5-flash' - this is the most common free model
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash", 
                contents=f"Return a JSON list of steps for: {user_input}"
            )
            return response.text
        except Exception as e:
            if "429" in str(e):
                return "QUOTA_ERROR: Waiting for server reset..."
            return f"Error: {e}"

    if __name__ == "__main__":
        print("Connecting to AI...")
        result = create_workflow_plan("Summarize my emails")
        print(result)