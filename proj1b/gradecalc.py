# Marcy Held
# SI 507, Project 1
# 26 Jan 2017

# Part 1: Create a dictionary of the student and their respective test scores
gradebookFile = open('gradebook.csv', 'r')

studentGrades = {}
linesList = gradebookFile.readlines()
for line in linesList[1:7]:
    lineVals = (line.split(","))
    studentGrades[lineVals[0]] = {}
    studentGrades[lineVals[0]]['Assn 1'] = lineVals[1]
    studentGrades[lineVals[0]]['Assn 2'] = lineVals[2]
    studentGrades[lineVals[0]]['Assn 3'] = lineVals[3]
    studentGrades[lineVals[0]]['Final Exam'] = lineVals[4][:-1]

print ("PART 1")
print (studentGrades)
print ('\n')


gradebookFile2 = open('gradebook.csv', 'r')
#gradebookData = csv.reader(gradebookFile2) # makes reader object
gradesInfo = {}

linecount = 0
linesList = gradebookFile2.readlines()
for line in linesList:
    #print (linecount)
    lineVals = (line.split(","))
    #print (lineVals)
    if linecount == 7:
        gradesInfo['Assn 1'] = {}
        gradesInfo['Assn 1']['weight'] = lineVals[1]

        gradesInfo['Assn 2'] = {}
        gradesInfo['Assn 2']['weight'] = lineVals[2]

        gradesInfo['Assn 3'] = {}
        gradesInfo['Assn 3']['weight'] = lineVals[3]

        gradesInfo['Final Exam'] = {}
        gradesInfo['Final Exam']['weight'] = lineVals[4][:-1]

    if linecount == 8:
        gradesInfo['Assn 1']['max_points'] = lineVals[1]
        gradesInfo['Assn 2']['max_points'] = lineVals[2]
        gradesInfo['Assn 3']['max_points'] = lineVals[3]
        gradesInfo['Final Exam']['max_points'] = lineVals[4]

    linecount += 1
print ('PART 2')
print (gradesInfo)
print ('\n')


def student_average(student_name):

    weightedAvg = 0

    percent1 = (float(studentGrades[student_name]['Assn 1'])/float(gradesInfo['Assn 1']['max_points']))
    avg1 = percent1 * float(gradesInfo['Assn 1']['weight'])

    percent2 = (float(studentGrades[student_name]['Assn 2'])/float(gradesInfo['Assn 2']['max_points']))
    avg2 = percent2 * float(gradesInfo['Assn 2']['weight'])

    percent3 = (float(studentGrades[student_name]['Assn 3'])/float(gradesInfo['Assn 3']['max_points']))
    avg3 = percent3 * float(gradesInfo['Assn 3']['weight'])

    percent4 = (float(studentGrades[student_name]['Final Exam'])/float(gradesInfo['Final Exam']['max_points']))
    avg4 = percent4 * float(gradesInfo['Final Exam']['weight'])

    return (avg1 + avg2 + avg3 + avg4) * 100

print ('PART 3')
print ('Julie : ' + str(student_average('Julie')))
print ('Humphrey : ' + str(student_average('Humphrey')))
print ('James : ' + str(student_average('James')))
print ('Clark : ' + str(student_average('Clark')))
print ('Audrey : ' + str(student_average('Audrey')))
print ('Marilyn : ' + str(student_average('Marilyn')))
print ('\n')

def assn_average(assn_name):
    percent_Julie = (float(studentGrades['Julie'][assn_name])/float(gradesInfo[assn_name]['max_points']))
    percent_Humphrey = (float(studentGrades['Humphrey'][assn_name])/float(gradesInfo[assn_name]['max_points']))
    percent_James = (float(studentGrades['James'][assn_name])/float(gradesInfo[assn_name]['max_points']))
    percent_Clark = (float(studentGrades['Clark'][assn_name])/float(gradesInfo[assn_name]['max_points']))
    percent_Audrey = (float(studentGrades['Audrey'][assn_name])/float(gradesInfo[assn_name]['max_points']))
    percent_Marilyn = (float(studentGrades['Marilyn'][assn_name])/float(gradesInfo[assn_name]['max_points']))

    return ((percent_Julie + percent_Humphrey + percent_James + percent_Clark + percent_Audrey + percent_Marilyn) / 6) * 100

print('PART 4')
print ('Assn 1 : ' + str(assn_average('Assn 1')))
print ('Assn 2 : ' + str(assn_average('Assn 2')))
print ('Assn 3 : ' + str(assn_average('Assn 3')))
print ('Final Exam : ' + str(assn_average('Final Exam')))
