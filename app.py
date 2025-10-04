import requests
import json

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"  #Ollama and LLM model is downloaded locally
    data = {
        "model": "gemma:2b",     # You can change this to gemma:7b if downloaded
        "prompt": prompt
    }
    
    
    
    #Check - List of ollama Installed

    # Send prompt to Ollama and stream response
    response = requests.post(url, json=data, stream=True)

    print("Answer : ")

    for line in response.iter_lines():
        if line:
            # Decode and parse JSON safely
            msg = json.loads(line.decode('utf-8'))
            # Only print the actual model response text
            if "response" in msg:
                print(msg["response"], end="", flush=True)

    print("\n")  # New line after full response

if __name__ == "__main__":
    print("Ask Me Anything  : ")
    while True:
        user_input = input("\nYour Question: ")
        if user_input.lower() in ["exit", "quit","q"]:
            print("Thank You for Using Ollama ChatBot. Goodbye! ")
            break
        ask_ollama(user_input)

