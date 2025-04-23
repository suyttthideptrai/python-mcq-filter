import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser(description='Process a text file containing multiple-choice questions and answers.')
    parser.add_argument('--source_file', type=str, help='Path to the source text file.')
    parser.add_argument('--target_file', type=str, help='Path to the target text file.')
    parser.add_argument('--answer_starts_with', type=str, default='A:', help='Prefix for answer lines.')
    return parser.parse_args()

# Test

# source_file = os.path.join(os.path.dirname(__file__), 'source', 'wbmcq7.txt')
# target_file = os.path.join(os.path.dirname(__file__), 'result', 'wbprocess.result.txt')

questions = []
answers = []

QUESTION_STARTS_WITH = r"(?i)question \d+:"


arg = parse_args()
source_file = arg.source_file
target_file = arg.target_file
ANSWER_STARTS_WITH = arg.answer_starts_with

a_len = len(ANSWER_STARTS_WITH.strip())

current_question = 0
with open(source_file, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        if re.match(QUESTION_STARTS_WITH, line):
            current_question += 1
            question = re.sub(QUESTION_STARTS_WITH, '', line, count=1)
            questions.append(question.strip())
            
        if line[:a_len] == ANSWER_STARTS_WITH:
            
            answer = line.replace(line[:a_len], '', 1)
            answer = answer.strip()
            answers.append(answer)

formated_questions = ''
for i, question in enumerate(questions):
    formated_questions += f'Question {i + 1}: {question}\n\n'

formated_answers = ''
for i, answer in enumerate(answers):
    formated_answers += f'Question {i + 1}: {answer}\n\n'


with open(target_file, 'w', encoding='utf-8') as outfile:
    outfile.write('### Questions ###\n\n')
    outfile.writelines(formated_questions)
    outfile.write('\n\n\n### Answers ###\n\n')
    outfile.writelines(formated_answers)


print('done')