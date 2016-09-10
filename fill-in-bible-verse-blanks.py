#creating the 'first level' where the user guesses the correct inputs.
level_1 = 'Romans 8:1 \nThere is therefore now no -- for those who are in -- Jesus, for the law of the -- of life has set you -- in Christ Jesus'

#creating the 'second level' where the user guesses the correct inputs.
level_2 = 'Romans 8:19-20 \nFor I consider that the -- of this present time is not worth -- to the future glory that is to be -- to us. For the -- was subjected to futility, not --, but because of him who suggested it, in --.'

#creating the 'third level' where the user guesses the correct inputs.
level_3 = 'Hebrews 11:1-3 \nNow -- is the assurance of things hoped for, the -- of things not seen. For by it, the people of old received their --. By faith we understand that the -- was created by the Word of God, so that what is seen was not made out of things that are --. By faith -- offered a more acceptable -- to God than Cain, through which he was commended as --.'

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
	print('\nWelcome to the Bible Memory verse game! In this game you will try to fill in the blanks for three different levels (verses).\n')
	print('To quit at any time, press ctrl + C\n')
	while check == False:
		difficulty = input("Please enter your difficulty level from Easy, Medium, or Hard: ")
		if difficulty.lower() != 'easy' and difficulty.lower() != 'medium' and difficulty.lower() != 'hard':
			print('You did not enter an appropriate difficulty.')
			check = False
		else:
			check = True
			if difficulty.lower() == 'easy':
				print('\nYou chose Easy! \n')
				answer_list = level_1_answers
				level_choice = level_1
			elif difficulty.lower() == 'medium':
				print('\nYou chose Medium! \n')
				answer_list = level_2_answers
				level_choice = level_2
			elif difficulty.lower() == 'hard':
				print('\nYou chose Hard! \n')
				answer_list = level_3_answers
				level_choice = level_3
	return difficulty, level_choice, answer_list

def play_level(level_choice, answer_list):
	'''
	use this function once a level is chosen
	this function will print the prompts and check for the correct answers
	'''
	print('Hint: answers ARE case-sensitive! \n')
	length = len(answer_list)
	level_list = level_choice.split('--')
	assert length == len(answer_list)
	#first_phrase = level_list[0]
	#print(first_phrase + '\n')
	sentence_piece = ''
	for i in range(length):
		sentence_piece = sentence_piece + level_list[i]
		check = False
		print(sentence_piece + '_______' + '\n')
		while check == False:
			guess = input("guess: ")
			if guess != answer_list[i]:
				print('\nTry again\n')
			else:
				print('\nGood job!\n')
				sentence_piece = sentence_piece + answer_list[i] 
				check = True


def winning_statement(difficulty, level_choice, answer_list):
	'''
	this function will print the winning statements and the complete string with all blanks filled
	call this once all the blanks have been correctly filled
	'''
	length = len(answer_list)
	level_list = level_choice.split('--')
	complete_sentence = ''
	for i in range(length):
		complete_sentence = complete_sentence + level_list[i] + answer_list[i]
	print('\033[1m' + 'Congratulations! You beat the {0} difficulty! \n'.format(difficulty) + '\033[0m') 
	print('The whole sentence is: \n')
	print('\033[1m' + complete_sentence + '\033[0m' + '\n')


def run_all_functions():
	'''
	this function puts together the three functions needed for a functioning game
	'''
	difficulty, level_choice, answer_list = startup_game()
	play_level(level_choice, answer_list)
	winning_statement(difficulty, level_choice, answer_list)

run_all_functions()
