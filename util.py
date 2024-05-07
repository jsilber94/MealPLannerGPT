import csv

def read_csv(prompts_name):
    data = ""
    with open(prompts_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            data += ", ".join(row)

    return data
