#GAME OF LIFE

import random

#Global Variables

game_status="alive"
dice_no=0
gender=""
name=""
cause_death=""

name_male_list=['Jeffrey', 'Charles', 'Ross', 'Chandler', 'Mike', 'Joey', 'Justin', 'Louis', 'Niall', 'Zayn', 'Bryan', 'Barry', 'Thomas', 'Theo', 'David', 'Matt',  'Matthew', 'Alfredo', 'Dan', 'Connor', 'Harry', 'Giles', 'Austin', 'Stephen', 'Barack', 'Shawn', 'Patrick']
name_female_list=['Cara', 'Danielle', 'Nina', 'Hailey', 'Gigi', 'Alisha', 'Emma', 'Anne', 'Francis', 'Selena', 'Britney', 'Niki', 'Meredith', 'Eva', 'Samantha', 'Nala', 'Kiara', 'Rachel', 'Monica','Phoebe','Georgina','Amy','Janice','Ariel','Tris','Carla','Ashley','Beth']
causes_death_list=['infected mushrooms', 'A lightning went straight for the head', 'Poisoned apple', 'Embarrassment', 'Game over', 'Bad joke', 'Stage diving', 'Club fight with a barbarian', 'Jumped too many holes', 'Followed the rabbit to the wrong hole', 'Forgot to define the type on a Java variable', 'Played Pokemon Go while crossing the road', 'Broke the 8th string on a djent riff', 'Missed an Avicii concert in town', 'Too much sadness at the same time', 'Lost the heart in a gamble', 'Went to the crossroad and signed the wrong contract']


#Variables

sad_message=False
job_message=False
college_message=False
married_message=False
kids_message=False
retire_message=False


#Functions definitions

def it_lives():
      print('Creation of a new life is now in progress. It all starts as a single cell:')
      print('0 ')
      print('00')
      print('0000\n00000000')
      print('.')
      print('.')
      print('.')
      print("A little while later,")

def set_gender():
   gender_dice = random.randint(0,1)
   if gender_dice == 0:
      return "Female"
   elif gender_dice == 1:
      return "Male"


def gender_print():
   print("A coin is flipped and a gender is chosen.\nThe pair of chromosomes responsible for this task now look like this:")
   if gender == "Female":
      print("XX")
     
   else:
      print("XY")
         
   print("\nYour gender is..." + gender + ".")
   print("\nYears later,")
          
def set_name():
   if gender == "Male":
      name_index_male = random.randint(0 , int(len(name_male_list)) -1 )
      return name_male_list[int(name_index_male)]
      
   if gender == "Female":
      name_index_female = int(random.randint(0 , int(len(name_female_list))) -1 )
      return name_female_list[int(name_index_female)]
                        
def name_print():
   print("You tumble across a game\n\n")
   print("WELCOME TO THE GAME OF LIFE")
   print("                         - Noone told you it was going to be this way\n")
   print("The name given to you is \"" + str(name) + "\".\n")
   print("And this is how your life is going to unfold:\n\n")
   print("Various stages:")
   print("1. Middle School")
   print("2. College")
   print("3. Work")
   print("4. Marriage")
   print("5. Kids")
   print("6. Retirement\n")

   print("Let's begin\n")
 
def get_death():
   cause_index = int(random.randint(0, int(len(causes_death_list))) -1 )
   cause_death = str(causes_death_list[int(cause_index)])
   return cause_death

def death():
   print("\n========================= R.I.P================================")
   print("\"" + str(name) + "\"" +" is now a slave to Death. \nReason: " + get_death() + ".")
   if age <=18:
      print("So sad it had to be so soon. No worries though, IT'S JUST A GAME!")
   print("\nOne last wish: Play another round by pressing F5!")
   print("Thank You.")
   
def user_dice():
  n=str(input("Type 'y' to roll the dice and go ahead! \nType ' n' to exit the game: "))
  if n=='y':
    dice_no=random.randint(1, 6)
    print("The number shown on your dice is", dice_no)
    
  else:
    print("Type a valid input") 

#End of function definitions

#Start

it_lives()
gender=set_gender()
gender_print()
name = set_name()
name_print()

#End

low_chance=1
high_chance=75


while game_status == "alive":

  event_chance = random.randint(low_chance, high_chance)
  if event_chance == 66:
        game_status = "dead" 
 
  print("You are now entering the first stage of your life: Middle School\n")
    
#Middle School
  user_dice()
  print("\nFirst day at new school")
  if dice_no==1:
    print("Its not looking good cause you dont have many friends and everyone seems to be giving you the stink eye. But dont worry, its just the beginning")
  elif dice_no==2:
    print("How lucky can you get? Everyone wants to be your friend and sit with you for lunch or play with you. School  sure is looking good!") 
  elif dice_no==3:
    print("You hate school. You hate everything about it. The only thing you look forward to all day is recess. UGH! Life doesnt good at all")
  elif dice_no==4:
    print("You are an all rounder, quite a favorite among the teachers. But beware because all the students are jealous")
  elif dice_no==5:
    print("You are suspended for your bad behaviour.")
  else:
    print("You couldn't attend your exams as you were unwell. get well soon!")
    
  

#Marriage
  print(" \n\nThey say marriage is both a sacred union and a natural institution. Lets see how this works out for you, shall we?\n")
  user_dice()
  if dice_no==1 or dice_no==2:
                print("\nYou got married to your childhood sweetheart you've known since you can remember! Being born in the same hospital on the same day does mean something then.")
                user_dice()
                if dice_no==1 or dice_no==2:
                    print(" \nSorry mate. Looks like this wasnt meant to be but it sure did look up at the time you said 'I Do', didnt it? You guys lasted for hardly a year. Well, thats more than what people get in a lifetime so cheer up!")
                elif dice_no==3 or dice_no==4:
                    print(" \nYour husband/wife now suffers from amnesia after a terrible motorbike accident. Sort of reminds you of 'The Notebook', doesnt it? You hang in there,though")
                else:
                    print(" \nAww. What a lovely couple you two make! A match truly made in heaven. The gods/godesses of marriage truly bestowed their blessing upon you two")      
                    married_message=True
  elif dice_no==3 or dice_no==4:
                print("\nAre the odds ever in your favour! You feel in love and got married to Python! Things are going to be just right")   
                user_dice()
                if dice_no==1 or dice_no==2:
                    print(" \nYou cant get over your love for coding! Python and you spend a lot of time together now. What a happy marriage")
                elif dice_no==3 or dice_no==4:
                    print(" \nBad news! You just discovered Java and C++ and cant choose between the three. They are all equally good and you would love to spend equal time with all of them but please do Remember your vows!")
                else:
                    print(" \nYou met your partner for life through an online coding chatroom and realised you two are just perfect for each other and get married right away. Happy coding you two!")
                    married_message=True 
  else :
                print(" \nOh no! Looks like you have to give your chance to be a married person a miss. You are too into your job and are working hard towards your promotion and you dont want anything getting into the way of you being the next CEO of your company\n")        
                user_dice()
                if dice_no==1 or dice_no==2:
                    print(" \nI guess you have to keep your goals aside for a while cause you think you are falling for your secretary pretty hard. Love doesnt wait for anyone, my friend") 
                elif dice_no==3 or dice_no==4:
                    print(" \nAt this rate, you'll have to get married to your job. This obsession isnt healthy. There are better things to look forward in life! Take a deep breath and review")
                else:
                    print(" \nYou sure know how to balance things just right. You married your boss. Now you can spend your time together always and still work on that promotion")

  print("\n\nBONUS ROUND: You get to roll pick a card for unexpected turn of events!")
  p=str(input("\nEnter 'p' to pick a card and 'c' to continue with the game"))
  if p=='p':
      s=random.randint(1,10)
      if s==2 or s==8:
          print("YOU WON THE LOTTERY. YOU ARE NOW A MILLIONAIRE")
      elif s==1 or s==6:
          print("Oh no! Youve gone bankrupt")
      elif s==5 or s==9:
          game_status=="dead"
          death()
      else:
          print("You are saved. Looks like life has nothing to thow at you in the moment. Lucky Chap!")
          
          
  
#Kids

  print(" \n\nTrue purpose served or not? Lets see\n ")
  user_dice()
  if married_message==True:
                print("\nBlessed with a little boy and girl whom you name Jackson and Jazmyn. They are the most well known kids on the block. The talk of all parents these two! Good Job ")
                user_dice()
                if dice_no==1 or dice_no==2:
                    print("\nJackson is into sports just like you. Football, Baskeball, Cricket, you name it and he's good at it. Jazmyn is more on the artistic side. She wins the google doodle competition every year.  ")
                elif dice_no==3 or dice_no==4:
                    print("\nJackson is such turning into such a  brat. You should definitely do something about it unless you want him to end up being the male Paris Hilton. Jazymn on the other end wins over everyone. Shes has your typical girl next door charm")
                else:
                    print("\nGEEK ALERT! Looks like your passion for coding has passed on to both of your kids. They host kiddie hackathons in school. Genius")      

  elif dice_no==3 or dice_no==4:
                print("\nYou derive satisfaction from helping students online as a tutor for a python course and they all love you. Why wouldnt they, youre such a good teacher after all \n")
                user_dice()
                if dice_no==1 or dice_no==2:
                    print("\nYou discovered the only way  you wanted to be around kids is as their teacher, so you teach part-time over the weekends")
                elif dice_no==3 or dice_no==4:
                    print(" \nOh no. You had to take care of your ailing parents so you had no choice but to stop teaching. How you miss that sigh.")
                else:
                    print(" \nYouve been receving a lot of appreciation from students fo all the hard work you put in for them. They are begging you set up a programming institution. You can only wish you knew how good you were at this")
                    
  else :
                
                print("\nLife is so lonely. You debate whether to get a pet or adopt a child. Lets weigh the odds shall we?\nPets stay loyal to you till your/their death. The same cant be said for children. But you cant pass your pet as your offspring. What do you do?\n ")        
                user_dice()
                if dice_no==1:
                    print("\nTo hell with no kids, its not like everyone who has kids are happy and conent. Pets rock! You visit the local animal shelter and pick the cutest puppy mankind has ever seen. Now thats a friend for life") 
                elif dice_no==2:
                    print("\nIts pains you to see humans suffer the way they are now. You visit the local orphanage and have a chat with kids. Though you dont actually get one, you vow to make timely donations on your birthday. What a great way to spend your special day.")
                else:
                    print("\nMeh! None of this excites you so you still go back to being a lonely potato on your coach and binge watch telly all day long. No better way to make time fly")

                          
  
  print("\n\nBONUS ROUND: You get to roll pick a card for unexpected turn of events!")
  p=str(input("\nEnter 'p' to pick a card and 'c' to continue with the game"))
  if p=='p':
      s=random.randint(1,10)
      if s==1 or s==5:
          print("A Brand New BMW is all yours to ride")
      elif s==2 or s==9:
          print("A tornado washed away your condo in Florida")
      elif s==3 or s==10:
          game_status=="dead"
          death()
      elif s==8:
          print("You get a custom made Lifetime Pass to Disneyland")
      else:
          print("You are saved. Looks like life has nothing to thow at you in the moment. Lucky Chap!")


#      
  if game_status=="dead":
      death()
     
        

