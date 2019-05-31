##  Mai Do.PY
## Mai Nhu Do  mdo@temple.edu 

## Survey Game in which you answer 5 questions and we will show you your favorite artist!

import os
os.chdir(r'C:\Python32')

class MyApp():
    def __init__(self, title=None, author="", date="" ):
         
           self.title =   title
           self.author =  author
           self.date = date


App = MyApp ("Simpler version of Akinator game")

print(App.title)
print(App.author)
print(App.date)


f = open('tuf96473Questions.txt', mode = 'r')
questions = f.readlines()
print(questions)

import textwrap

yourName = input("Please enter your name: ")
print("\n")
sample_text = '''    Answer each of the 5 questions below (please be truthful)
and I will score your answer. Select A B or C, with C
being neither or no opinion for multiple choice questions, 

        '''
dedented_text = textwrap.dedent(sample_text).strip()

print (dedented_text) 


n = 0
for row in questions:
   
 if row[:3] =="***" :
   needanswer = True
   while needanswer :
      answer = input("Pick answer: ")
      if answer == "A" or answer =="a":
         n = n+1
         needanswer = False
      
      elif answer == "B" or answer =="b":
         n = n-1
         needanswer = False
      elif answer =="C" or answer == "c" :
         pass
         n = n
         needanswer = False
      else:
         needanswer = True
 else:
     line = row.strip()
     print(line)
if n > 0 :
   print("You like Taylor Swift")
elif n < 0 :
   print("You like Kanye West")
else:
   print("Hmm, a tossup, maybe you like Beyonce")
