import random

word_list = ["apple", "banana", "peach", "plum", "pineapple", "fig", "grapes","mango"]
count = 1
right_word = random.choice(word_list)
wordlist = list(right_word)
random.shuffle(wordlist)
shuffled_word = ''.join(wordlist)
print("Guess the Scrambled word, you have 5 guesses, here is the word: ", shuffled_word)
guess = str(input("Your guess: "))
while guess != right_word and count < 5:
    print("Wrong One you have " + str(5 - count) + " attempts")
    count += 1
    guess = str(input("Your new guess: "))
if guess == right_word:
    print("CORRECT!!! Congratulation")
elif count == 5:
    print ("Wrong! Good luck next time, the right word is ", right_word)
print("Thank you for playing!") 
























# while word:
#     position = random.randrange(len(word))
#     scramble += word[position]
#     word = word[:position] + word[(position + 1)]


