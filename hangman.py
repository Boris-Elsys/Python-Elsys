import random
 
word_list = ['board', 'keyboard', 'cloud', 
         'snake', 'globe', 'code', 'biology', 
         'baloon', 'water', 'game', 'elephant'] 

word = random.choice(word_list)
 
print("Guess the word")

tries = 8
corr_guess = ''

while tries > 0:

    print(word[0], word[len(word) - 1])
    guess = input("guess a letter: ")
    
    if guess not in word:
        tries -= 1
        print("wrong")
        print(tries)
    
        if tries == 0:
            print("loss")
                
    else:
        print(guess)
        corr_guess +=guess
        
    if corr_guess == word:
        print("win")
        break
