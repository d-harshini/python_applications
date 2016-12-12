from random import choice
import sys

print("WELCOME TO QUIZLET - THE BEST FLASHCARD APPLICATION OUT THERE!")
print("                           - Learn in a jiffy")
print("\n\nWhat do you want to learn today?\n\n")
print("Recommendations:\n")
print("1. Metric system")
print("2. 10 Words for food in French")
print("3. 10 Common phrases in French\n\n")

words1={"peta" : "quadrillion", "tera": " trillion ", "giga": " billion", "mega": "million", "kilo": "thousand", "deca": "ten", "macro": "millionth", "nano": "billionth", "pico": "trillionth ", "femto": "quadrillionth"}
words2={"la confiture": "jam", "la mayonnaise":"mayonnaise", "la croissant":"croissant", "la farine": "flour", "les frites": "french fries","le sucre": "sugar", "le sel": "salt", "le pain": "bread", "le riz": "rice", "le poivre": "pepper"}
words3={"oui": "yes", "merci": "thank you", "non": "no", "bonjour": "hello", "au revoir": "goodbye", "bienvenue": "welcome", "Je m'appelle": "My name is", "Comment vous appelezvous?": "What is your name?", "Excusez-moi":"Excuse me", "Parlez lentement": "Please speak slowly"}   


while True:
      
          n=int(input("Enter the integer corresponding to the topic you would like to quiz yourself on\n"))
          
          print("\n10 Random questions which can be repeated will now be displayed on the console")

          print("\nPlease type 'start' to begin or 'quit' to leave")
          user_answer = raw_input()

          if str(user_answer)=="quit":
                      break
                  
          
          if n==1:
                
                for i in range(10):
                   key1=choice(words1.keys())
                   print("\nType the metric system equivalent of: "+words1[key1])
                   user_guess=raw_input()
                      
                   if str(user_guess)==key1:
                         print("\nCorrect!")
                   
                   else:
                         print("\nOops. The correct answer is:", key1)
                         
                   


          elif n==2:
                
                for i in range(10):
                      
                 key2=choice(words2.keys())      
                 print("\nType the French equivalent of the food item: "+words2[key2])
                 user_guess=raw_input()

                 if str(user_guess)==key2:
                      print("\nCorrect!")
                
                 else:
                      print("\nOops. The correct answer is:", key2)      

                 

          else:     
                for i in range(10):

                      
                 key3=choice(words3.keys())      
                 print("\nType the French equivalent of common phrases: "+words3[key3])
                 user_guess=raw_input()

                 if str(user_guess)==key3:
                      print("\nCorrect!")
                 
                 else:
                      print("\nOops. The correct answer is:", key3)      

                

          print("\nDo you want to play another round?\nType 'yes' if you want to or 'quit' if you want to exit")
          n=raw_input()
          if str(n)=='yes':
                continue
          else:
                break
          
