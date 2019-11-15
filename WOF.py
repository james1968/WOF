VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'
import random


# Write the WOFPlayer class definition (part A) here

class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)


# Write the WOFHumanPlayer class definition (part B) here

class WOFHumanPlayer(WOFPlayer):

    def getMove(self, category, obscuredPhrase, guessed):
        move = input("Guess  letter, phrase, or type 'exit' or 'pass':")


# Write the WOFComputerPlayer class definition (part C) here

class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        rand_number = random.randint(1, 10)
        if rand_number > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        toBeGuessed = []
        for letter in LETTERS:
            if letter in VOWELS and letter not in guessed:
                if self.prizeMoney > VOWEL_COST:
                    toBeGuessed.append(letter)
            elif letter not in guessed:
                toBeGuessed.append(letter)
        return toBeGuessed

    def getMove(self, category, obscuredPhrase, guessed):
        possLetters = getPossibleLetters(guessed)
        if len(possLetters) < 1:
            return 'pass'
        if smartCoinFlip() == True:
            return SORTED_FREQUENCIES[0]
        else:
            letters = [letter for letter in possLetters]
            rand_letter = random.choice(letters)
            return rand_letter
