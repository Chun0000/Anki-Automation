import re


def jsonConvertor():
    f = open(
        '/Users/chun/Documents/GitHub/mtexam-data-processing/database/pathology.txt', 'r')
    dict_all_questions = []

    for i in f.readlines():
        template = {'questions': "", "A": "", "B": "",
                    "C": "", "D": "", 'answer': [], 'year': ""}
        L = i.split("\t")
        optionRegex = re.compile(r'\D\.')
        result = re.split(optionRegex, L[0].strip())
        template["questions"] = result[0]
        template["A"] = result[1]
        template["B"] = result[2]
        template["C"] = result[3]
        template["D"] = result[4]
        template["answer"] = L[1].split()
        template['year'] = L[2].strip("\n")
        dict_all_questions.append(template)

    return dict_all_questions
