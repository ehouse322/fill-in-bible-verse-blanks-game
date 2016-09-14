# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

#level_1 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
#adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
#don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
#tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/

#creating the 'first level' where the user guesses the correct inputs.
level_1 = 'There is therefore now no -- for those who are in -- Jesus, for the law of the -- of life has set you -- in Christ Jesus'

#creating the 'second level' where the user guesses the correct inputs.
level_2 = 'For I consider that the 1 of this present time is not worth 2 to the future glory that is to be 3 to us. For the 4 was subjected to futility, not 5, but because of him who suggested it, in 6.'

#creating the 'third level' where the user guesses the correct inputs.
level_3 = 'Now 1 is the assurance of things hoped for, the 2 of things not seen. For by it, the people of old received their 3. By faith we understand that the 5 was created by the Word of God, so that what is seen was not made out of things that are seen. By faith 6 offered a more acceptable 7 to God than Cain, through which he was commended as 8.'

#creating the answers to the first level in a list
level_1_answers = ['condemnation', 'Christ', 'Spirit', 'free']

#creating the answers to the second level in a list
level_2_answers = ['suffering', 'comparing', 'revealed', 'creation', 'willingly', 'hope']

#creating the answers to the third level in a list
level_3_answers = ['faith', 'conviction', 'commendation', 'universe', 'visible', 'Abel', 'sacrifice', 'righteous']

def startup_game():
	'''
	start game and ask user to select difficulty
	'''
	check = False
	print('Welcome to the Bible Memory verse game! In this game you will try to fill in the blanks for three different levels (verses).')
	print('To quit at any time, press ctrl + C')
	while check == False:
		difficulty = input("Please enter your difficulty level from Easy, Medium, or Hard: ")
		if difficulty.lower() != 'easy' and difficulty.lower() != 'medium' and difficulty.lower() != 'hard':
			print('You did not enter an appropriate difficulty.')
			check = False
		else:
			check = True
			if difficulty.lower() == 'easy':
				print('You chose Easy!')
				answer_list = level_1_answers
				level_choice = level_1
			elif difficulty.lower() == 'medium':
				print('You chose Medium!')
				answer_list = level_2_answers
				level_choice = level_2
			elif difficulty.lower() == 'hard':
				print('You chose Hard!')
				answer_list = level_3_answers
				level_choice = level_3
	return difficulty, level_choice, answer_list

startup_game()

def play_level(difficulty, answer_list, level_choice):
	length = len(answer_list)
	print
	#if difficulty

def initialize_level(difficulty):
	pass



