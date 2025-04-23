# Instructions

## MCQ Formating:

### Help
```bash
python mcq.py --help
```

### Output
```
usage: mcq.py [-h] [--source_file SOURCE_FILE] [--target_file TARGET_FILE] [--choice_delimiter CHOICE_DELIMITER] [--space_between_questions SPACE_BETWEEN_QUESTIONS] [--do_index_answer]

Process a text file containing multiple-choice questions and answers.

options:
  -h, --help            show this help message and exit
  --source_file SOURCE_FILE
                        Path to the source text file.
  --target_file TARGET_FILE
                        Path to the target text file.
  --choice_delimiter CHOICE_DELIMITER
                        Delimiter for multiple-choice answers. eg: `.` -> A. The answer
  --space_between_questions SPACE_BETWEEN_QUESTIONS
                        Number of blank lines between questions.
  --do_index_answer     Will append index to the answer. eg: 1. A 2. B ...
```

### Example Usage
```bash
python mcq.py --source_file source/wbmcq8.txt --target_file result/wbmcq8.result.txt --space_between_questions 1 --do_index_answer
```

## Short Answer Formating

### Help
```bash
python shorta.py --help
```

### Ouput

```
usage: shorta.py [-h] [--source_file SOURCE_FILE] [--target_file TARGET_FILE] [--answer_starts_with ANSWER_STARTS_WITH]

Process a text file containing multiple-choice questions and answers.

options:
  -h, --help            show this help message and exit
  --source_file SOURCE_FILE
                        Path to the source text file.
  --target_file TARGET_FILE
                        Path to the target text file.
  --answer_starts_with ANSWER_STARTS_WITH
                        Prefix for answer lines.

```

### Example Usage

```bash
python shorta.py --source_file source/wbsa8.txt --target_file result/wbsa8.result.txt --answer_starts_with A:
```