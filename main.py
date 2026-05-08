import anthropic
from dotenv import load_dotenv
from history_chat import history_chat
load_dotenv()

client = anthropic.Anthropic()

class AI_bot:
    def __init__ (self, personality = None):
        if personality is None: 
          personality = "You are just Claude"
        self.history= []
        self.personality = personality
    def chat(self, mess):
        with client.messages.stream(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=mess,
            system= self.personality,
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
            return stream.get_final_message().content[0].text

Fus = AI_bot(f"You are a caveman, you act like conscious competence and everything you said is right. Keep it simple")
Fus.history.append({"role":"assistant", "content":history_chat})
while True:
    user_input= input("\nYou: ")
    if user_input:
      if user_input == "exit":
          break
      else:
          print("Fus: ",end="")
          Fus.history.append({"role":"user", "content":user_input})
          su_dung = Fus.chat(Fus.history)
          Fus.history.append({"role":"assistant", "content":su_dung}) 
    else:
      break
        