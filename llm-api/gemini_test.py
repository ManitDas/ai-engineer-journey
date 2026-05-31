from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Conversation history — this is what gives the bot memory
conversation_history = [
    {
        "role": "system",
        "content": """You are an expert assistant on ISRO missions and space technology. 
You have deep knowledge of:
- All ISRO satellite missions (Chandrayaan, Mangalyaan, PSLV, GSLV etc.)
- SAC (Space Applications Centre) and its work on remote sensing
- Satellite imaging, SAR data, and earth observation
- Indian space program history and future plans
Answer questions accurately and concisely. If you don't know something, say so."""
    }
]

print("ISRO Mission Assistant 🚀")
print("Ask me anything about ISRO. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break
    
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    # Send full conversation history
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )
    
    # Get assistant response
    assistant_message = response.choices[0].message.content
    
    # Add assistant response to history
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    print(f"\nAssistant: {assistant_message}\n")