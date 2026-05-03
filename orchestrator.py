import os
from dotenv import load_dotenv
from genai import Client

load_dotenv()

# Setup the new AI Client
client = Client(api_key=os.getenv("GEMINI_API_KEY"))

def create_workflow_plan(user_input):
    prompt = f"""
    You are an AI Workflow Architect. 
    Convert this user request into a structured JSON list of steps.
    Request: "{user_input}"
    
    Each step must have: 'step_number', 'action', and 'tool'.
    Output ONLY the JSON list.
    """
    
    # Using the latest model: gemini-2.0-flash
    response = client.models.generate_content(
        model="gemini-1.5-flash", 
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    user_request = "Watch my GitHub for new stars and send a thank you message on Slack"
    print("Asking Gemini 2.0 to build a plan...")
    try:
        result = create_workflow_plan(user_request)
        print("\nGenerated Workflow:")
        print(result)
    except Exception as e:
        print(f"Error: {e}")