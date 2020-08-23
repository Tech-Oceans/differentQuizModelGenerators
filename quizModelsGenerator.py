# ---------------------- this is random Qaiz generator python code -------------------------#

import os # importing os librery
import random # import random for generating random qaiz questions

# set dictanary variable take questions as it keys and Answer as values called QuestionsList:
QuestionsList = { }

# star while loop to deal with user data inputs
while True:

    # sak user if they want to creat mutiple choic exam generate rendom models
    askUser = input('Do you want to creat new list of questions and answer ? yes or No : ')

    # handle the input using if statments ...
    if askUser == 'yes' or askUser == 'Yes':
        # ask the user to enter the number of quiz qestions
        numberOfQuestions = input('please enter the number of question you would like to include in quiz ? ')

        # use the for loop to let user enter number of questions and Answer
        for number in range(int(numberOfQuestions)):
            # the code will ask you to enter Questions and the answers you would like to incude on quiz
            writeQues = input('please inter question no. %s: ' % (number+1))
            writeAnswer = input('please inter Answer for question no. %s: ' % (number+1))

            # add the questions and the Answers to dictionary
            QuestionsList[writeQues] = writeAnswer

    # if answer no
    elif askUser == 'No' or askUser == 'no':
        print(' bay bay ..........')
        break
    # keep looping (while) no answer
    else:
        print('please enter yes or no')
        continue

    # ask the user to enter the number of different quiz models
    numberOfModel = input('please enter number of quiz models you would like to generate ? : ')
    break

# store the state in to list so i can enter it each one 
randQuestions = list (QuestionsList.keys())


# different qaiz models loop
for diffQaizPapers in range (int(numberOfModel)):
    # use try funcation to run the code and handel any error
    try:
        # open files for each exam model and answer sheet for that model .......
        # file directory should to change to match your file where you want to generate quiz models
        qaizSheet = open ('... specify the directory path where you wanna save the questions models... /QaizSheet%s' %(diffQaizPapers + 1) , 'w')
        answerSheet = open ('... specify the directory path where you wanna save the Answer models .../AnswerSheet%s' %(diffQaizPapers + 1) , 'w')

        # given header for the quiz and answer sheet
        # you can change this section accourding to your need 
        # Start *************************************** 
        qaizSheet.write(('-'*10) + ' ...... here you can write quiz title   model no.%s ........ ' %(diffQaizPapers + 1) + ('-'*10))
        # another enter to be in quiz sheet include student name , date ,and Id number
        qaizSheet.write('\n\n your Name: \n\n\n Date: \n\n\n Id Number: \n\n')
        qaizSheet.write('_'* 80)
        # End *****************************************

        # header for the answer sheet which include the answer of spacific quiz sheet 
        answerSheet.write('---------- this is the Answer Sheet for qaiz No. %s ----------\n' %(diffQaizPapers + 1))
        
        # random up the randQuestions list for each quiz models  .......
        random.shuffle(randQuestions)

        # for loop write the qestions and answer to quiz models 
        for question in range (int (numberOfQuestions)):

            # get the answer from the rendom list for the picked question
            Answer = (QuestionsList[randQuestions[question]])

            # -----  get the wronge answer to be used in multiple choices -----
            wrongeAnswers = list (QuestionsList.values())
            # delete the correct answer from the wrongeAnswers lsit 
            del wrongeAnswers[wrongeAnswers.index(Answer)]
            # collect 3 wronge answer randomly from the wrongeAnswers list
            # if you would like to increase the number of multiple choices you need to change the number of wrongeAnswers
            wrongeAnswers = random.sample(wrongeAnswers, 3)
            # add the wrongeAnswers with correct answer list and max them
            answerOptions = wrongeAnswers + [Answer]
            random.shuffle(answerOptions)

            # write the question to the sheet model
            questions = ('\n Q:'+ str (question+1)) + ' ' + (randQuestions[question]) + ' ?\n'
            qaizSheet.write(questions)

            # loop to add the 4 muliple choice to the question sheet inclue the correct answer 
            for multiple in range (4):

                qaizSheet.write ('%s) %s ' %('ABCD' [multiple], (answerOptions)[multiple]))
                qaizSheet.write('\n')

            # Write the answer key to a file.
            answerSheet.write('%s. %s) %s\n' % (question + 1, 'ABCD'[answerOptions.index(Answer)], Answer))
     

    except FileExistsError:
        print ('file already exsisit.....')
    except FileNotFoundError:
        print ('targeted file can not be founded')
    except NameError:
        print ('it seem you dont want to continue with create the quiz bay bay.... ')
    except ValueError:
        print ('you should have more then 4 question to generate the multiple choices')
        break

    qaizSheet.close()
    answerSheet.close()
