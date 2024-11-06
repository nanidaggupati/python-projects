import random
word_list=['uday','ramesh','suresh']

choosen_word=random.choice(word_list)
print(f'psst the choosen word {choosen_word}')


display=[]
word_length=len(choosen_word)
for _ in range(word_length):
   display +="_"

end_of_game=False 

while not end_of_game:
 guess=input("guess a letter:").lower()
 
 #check the guess letter
 for postion in range(word_length):
     letter=choosen_word[postion]
     if letter==guess:
        display[postion]=letter
       
 print(display)

 if "_" not in display:
    end_of_game=True
    print("you win")