import random

list_of_words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(list_of_words)
word2 = word
while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'exit':
        break
    elif choice == 'play':
        print("H A N G M A N\n")
        hint = ('-' * len(word))
        tries = 8
        symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']',
                   ':', '"',
                   "'", ',', '.', '?', '<', '>', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        g_copy = []

        while tries <= 8:
            print('\n')
            print(hint)
            guess = input('Input a letter: ')
            if guess in word2:
                index = word.find(guess)
                if guess in word and guess in word2:
                    hint = list(hint)
                    hint[index] = guess
                    hint = ''.join(hint)
                    word = list(word)
                    word[index] = '-'
                    word = ''.join(word)
                    if hint == word2:
                        print('You survived!')
                        break
                    elif word2.count(guess) >= 2:
                        index = word.find(guess)
                        hint = list(hint)
                        hint[index] = guess
                        hint = ''.join(hint)
                        word = list(word)
                        word[index] = '-'
                        word = ''.join(word)
                    continue
            if 1 < len(guess) > 1:
                print('You should input a single letter')
            elif guess in word2 and guess not in word or guess in g_copy:
                print('You already typed this letter')
            elif guess in symbols:
                print('It is not an ASCII lowercase letter')
            elif guess not in word2:
                print('No such letter in the word')
                tries -= 1
                g_copy.append(guess)
            if tries == 0:
                print('You are hanged!')
                break
