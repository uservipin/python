

"""
Note Run "test_case.py"  file and follow On screen instructions
"""


from user import user_class
from user import super_user_class
from quiz import quiz


print(
      "\n"
      "Hello Welcome to EdYoda Test Series\nDetails of test are given as follows \n "
      " Note:\n"
      "  1. This Test is MCQ Based\n"
      "  2. Select answer to proceed for Next Question\n"
      "  3. Every Question have ONE correct answer. \n\n"
      "Kindly Please Follow on screen instructions\n"
      )

# super_user1 = super_user_class('Vipin','kumar.vipin1v00@gmail.com',7500574058)
# super_user1.add_question_to_test()
# super_user1.update_question()
# super_user1.delete_question_paper()


print('Let the system know you are:  \n 1. user\n 2. super_user\n')

key= input("Please Enter \n'SUPER USER KEY': super_user@123  To Authenticate You :\n"
           "If 'USER' , 'KEY' is  user \n")

if key=='super_user@123':
      print(" Welcome You Are Now 'super_user' \n You have Following Features :\n1. Add question with Type and Hardness\n"
            "2. Update question with Type and Hardness \n3. Delete question with Type and Hardness\n4. Set correct answers of MCQ")


      func= int(input('You want to add question \n 1. add  \n 2. update \n 3. delete\n'))

      if func ==1:
            super_user1 = super_user_class('Vipin', 'kumar.******@gmail.com', 7500574058)
            super_user1.add_question_to_test()

      if func ==2:
            super_user1 = super_user_class('Vipin', 'kumar.******@gmail.com', 7500574058)
            super_user1.update_question()

      if func ==3:
            super_user1 = super_user_class('Vipin', 'kumar.******@gmail.com', 7500574058)
            super_user1.delete_question_paper()


if key =='user':
      print("Welcome You Are Now 'user': \nFeatures you can access\n\n"
            
            "1. Take Quiz than system will display result and 'correct answer' with options\n"
            "2. Retake Quiz than system will display result and 'correct answer' with optipns\n"
            "You can select Quiz on the bases of: \n #Type# \n #Hardness# \n To select type and hardness follow on screen instructions\n")

      user1 = user_class('Vipin', 7500574058, 'kumar.vipin1v00@gmail.com')

      # ask user type of test
      question_type = user1.question_type()

      # ask user hardness of quiz
      question_hardness = user1.question_hardness()


      take_retake = user_class.take_quiz_or_retake_quiz(user1, question_type, question_hardness)


else:
      print("Try with Correct Credentials")



