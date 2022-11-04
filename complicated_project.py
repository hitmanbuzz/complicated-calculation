# Open the 'complicated_question.txt' for the question if you want to do this yourself or by your own method/style
# Made by Hitman-2005(Github)
# I made this program just to practice my python skill because right now(at the moment) I am not a good programmer/coder in python
# Feel free to make changes/modified the code

print('\n')
number = int(input('Please pick any number from 1-10: '))

# Mathematical Table:
if number >= 1 and number <= 10:
	r1 = number * 1
	r2 = number * 2
	r3 = number * 3
	r4 = number * 4
	r5 = number * 5
	r6 = number * 6
	r7 = number * 7
	r8 = number * 8
	r9 = number * 9
	r10 = number * 10
	result = r1, r2, r3, r4, r5, r6, r7, r8, r9, r10
	print('\n')
	print('Direct Result for Table',number,'(1-10) is shown below inside the bracket')
	print('\n')
	print('		👇')			
	print('\n')
	print(result)
	print('\n')
elif number > 0 and number < 10:
	print('The number you have ')
else:
	print('Wrong Input/Error Occured!')

first_half = sum(result[0:5])
second_half = sum(result[5:10])

final_result1 = first_half - second_half
final_result2 = second_half - first_half

print('Result as Negative:',final_result1)
print('Reason: Because we are subtracting greater number from smaller number')
print('\n')
print('Result as positive:',final_result2)
print('Reason: Because we are subtracting smaller number from greater number')
