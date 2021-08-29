import csv
filepath = "database/"
def get_questions(filename):
    form_questions = dict()
    with open(filepath+filename) as f:
        isQuestion = True
        question = ""
        options = []
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                form_questions[question] = options
                options = []
                isQuestion = True
            elif isQuestion:
                question = line.rstrip()
                isQuestion = False
            else:
                options.append(line.rstrip())
    return form_questions

def get_info_from_csv(filename):
    # create a dictionary
    data = dict()
     
    # Open a csv reader called DictReader
    with open(filepath+filename, encoding='utf-8') as f:
        csvReader = csv.DictReader(f)
        for rows in csvReader:
            key = rows['ID']
            data[key] = rows
    return data

def get_links_from_service(data, serviceType):
    links = list()
    for _, val in data.items():
        if val['Service'].strip() in serviceType or serviceType in val['Service'].strip():
            links.append({'Name': val['Name'], 'Link': val['Link'], 'Image': val['Image']})
    return links