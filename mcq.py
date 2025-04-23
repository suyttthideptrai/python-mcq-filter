import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Process a text file containing multiple-choice questions and answers.')
    parser.add_argument('--source_file', type=str, help='Path to the source text file.')
    parser.add_argument('--target_file', type=str, help='Path to the target text file.')
    parser.add_argument('--choice_delimiter', type=str, default='.', help='Delimiter for multiple-choice answers. eg: `.` -> A. The answer')
    parser.add_argument('--space_between_questions', type=int, default=1, help='Number of blank lines between questions.')
    parser.add_argument('--do_index_answer', action='store_true', help='Will append index to the answer. eg: 1. A  2. B ...')
    return parser.parse_args()

# Test

# source_file = os.path.join(os.path.dirname(__file__), 'source', 'wbmcq7.txt')
# target_file = os.path.join(os.path.dirname(__file__), 'result', 'wbprocess.result.txt')

filtered_questions = []
answers = []

ALLOWED_CHOICE_DELIMITERS = [
    '.',
    ')',
    ',',
]
CORRECT_ENDS_WITH = '*'
ANSWER_STARTS_WITH = [
    'A.',
    'B.',
    'C.',
    'D.',
    'E.',
    'F.',
    
    'A)',
    'B)',
    'C)',
    'D)',
    'E)',
    'F)',
    
    'A,',
    'B,',
    'C,',
    'D,',
    'E,',
    'F,',
]

arg = parse_args()
source_file = arg.source_file
target_file = arg.target_file
delimiter = arg.choice_delimiter
space = arg.space_between_questions

if len(delimiter) != 1:
    print(f"Invalid choice delimiter: {delimiter}. It should be a single character.")
    exit(1)


if delimiter not in ALLOWED_CHOICE_DELIMITERS:
    print(f"Invalid choice delimiter: {delimiter}. Allowed delimiters are: {ALLOWED_CHOICE_DELIMITERS}")
    exit(1)

current_question = 0
current_question_answers = []
with open(source_file, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()
    
    # Remove empty lines
    tmp_lines = []
    for line in lines:
        l = line.strip()
        if l != '':
            tmp_lines.append(l)
    lines = tmp_lines
    
    # Main process
    for i, line in enumerate(lines):
        first_two_chars = line[:2]
        if first_two_chars in ANSWER_STARTS_WITH:
            
            answer_character = first_two_chars[:1]
            
            replaced_answer = f"{answer_character}{delimiter}"
            line = line.replace(line[:2], replaced_answer, 1)
            
            if line.endswith(CORRECT_ENDS_WITH):


                current_question_answers.append(answer_character)
                line = line[:-1]
                
            if i + 1 == len(lines):
                answers.append(current_question_answers)

        else:
            if (current_question > 0):
                answers.append(current_question_answers)
                filtered_questions.append('\n' * space)
            current_question = current_question + 1
            current_question_answers = []
        filtered_questions.append(line + '\n')

formated_answer_text = ''
if arg.do_index_answer:
    for i, answer_character in enumerate(answers):
        formated_answer_text += f"{i + 1}. {','.join(answer_character)}\n"
else:
    for i, answer_character in enumerate(answers):
        formated_answer_text += f"{','.join(answer_character)}\n"

with open(target_file, 'w', encoding='utf-8') as outfile:
    outfile.write('### Questions without asterisks ###\n\n')
    outfile.writelines(filtered_questions)
    outfile.write('\n\n\n### Filtered Answers ###\n\n')
    outfile.writelines(formated_answer_text)


print('done')