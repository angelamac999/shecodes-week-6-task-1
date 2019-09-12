# from Section import Section
from Question import Question


class Survey:
    def __init__(self):
        pass


question_prompts = [
'\n Are you studying SheCodes Plus?\n (a) yes\n (b) no\n\n', 
'\n Do you currently work at BHP?\n (a) yes\n (b) no\n\n', 
]

questions = [
    Question(question_prompts[0],' '),
    Question(question_prompts[1],' ')
]

question1_prompts1 = [
'\n Do you prefer Wednesday sessions or Saturdays sessions?\n (a) Wednesday\n (b) Saturday\n (c) I have no preference\n\n',
'\n What days do you attend She Codes Australia (on most weeks)\n (a) Wednesday\n (b) Saturday\n (c) Wednesday and Saturday\n\n',
'\n Do you work full-time at BHP?\n (a) yes\n (b) no I am part-time\n (c) yes I am contractor\n\n',
]

questions1 = [
    Question(question1_prompts1[0],' '),
    Question(question1_prompts1[1],' '),
    Question(question1_prompts1[2],' ')
]

question2_prompts2 = [
'\n Do you feel that you are balancing work and study well?\n (a)yes\n (b) no\n (c) unsure\n\n',
'\n Are you enjoying learning coding?\n (a) yes\n (b) no\n (c) unsure\n\n',
'\n Are you feeling supported by the mentors?\n (a) yes\n (b) no\n (c) unsure\n\n',
'\n Do you feel that you are making progress with your learning goals?\n (a) yes\n (b) no\n (c)unsure \n\n',      
]


questions2 = [
    Question(question2_prompts2[0],' '),
    Question(question2_prompts2[1],' '),
    Question(question2_prompts2[2],' '),
    Question(question2_prompts2[3],' ')
]

def run_survey(questions):
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print('Congratulations for studying coding')

run_survey(questions)

def run_survey1(questions1):
    for question in questions1:
        answer = input(question.prompt)
        if answer == question.answer:
            print('thanks for answering section1')

run_survey1(questions1)

def run_survey2(questions2):
    for question in questions2:
        answer = input(question.prompt)
        if answer == question.answer:
            print('thanks for answering section2')

run_survey2(questions2)