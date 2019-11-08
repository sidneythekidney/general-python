import pyperclip

#This program allows you to copy multiple objects.
#First take input from user

text_list = []
i = 1
while True:
    text_data = str(input('Enter text you would like to copy (Hit enter when completely finished): '))
    if text_data == '':
        break
    print('This text is at position ' + str(i) + '. Enter this position when prompted to access the text.\n')

    text_list.append(text_data)
    i += 1

print('\nInformation copied!\n')

while True:
    copy_number = str(input('Enter position of text you wish to copy to clipboard (Enter exit to quit program): '))
    if copy_number == '':
        break
    copy_number = int(copy_number)
    pyperclip.copy(text_list[copy_number - 1])
    print(str(text_list[copy_number - 1]) + ' copied to clipboard.')