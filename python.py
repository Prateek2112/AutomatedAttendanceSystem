import connection
import json, ast
import initialStudentRecord
import faceRecognition

initialStudentRecord.createInitialRecord()
sheet = connection.createConnection()
index = 2
allRecord = sheet.get_all_records()
print('allrecord:', allRecord)
allRecordWithoutUnicode = ast.literal_eval(json.dumps(allRecord))
studentComesIn = faceRecognition.fetchFaces()
for student in allRecordWithoutUnicode:
    if (str(student["name"]) in studentComesIn):
        sheet.update_cell(index, 2, 1)
        index += 1
    else:
        index += 1
index = 0
print(studentComesIn)
