from controversial_filter.filter import ControversialFilter
import random

class ChatBot:
    def __init__(self):
        self.filter = ControversialFilter()
        self.name = "ChatBot"
        self.greetings = "Hello! I'm ChatBot, How can I help you today?"
         
        self.fallback_responses = "Against policies ! Please ask something else."
    
    def get_response(self, user_input):
        # First check if the input is controversial
        if self.filter.is_controversial(user_input):
            return self.handle_controversial_input()
        
        # Otherwise, generate a normal response
        return self.generate_normal_response(user_input)
    
    def handle_controversial_input(self):
        responses = "Controversial content detected! Please ask something else."
        return (responses)
    
    def generate_normal_response(self, user_input):
        # This is a simple response generator - you can replace with a real LLM
        lower_input = user_input.lower()
        
        if any(word in lower_input for word in ['hi', 'hello', 'hey']):
            return random.choice(self.greetings)
        
        elif any(word in lower_input for word in ['bye', 'goodbye']):
            return "Goodbye! Feel free to come back if you have more questions."
        
        else:
            return random.choice(self.fallback_responses)
    
    def start_chat(self):
        print((self.greetings))
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print(f"{self.name}: Goodbye!")
                break
            
            response = self.get_response(user_input)
            print(f"{self.name}: {response}")