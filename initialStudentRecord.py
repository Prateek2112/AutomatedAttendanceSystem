import connection


def createInitialRecord():
    sheet = connection.createConnection()
    studentNames = ['Abhishek', 'Aditya', 'Akansha', 'Akashnil', 'Akshay', 'Ameya', 'Anisha', 'Aravind', 'Basu', 'Divyanshu', 'Ganguly',
                    'Ghayathri', 'Hannan', 'Hitesh', 'Jay', 'Jayashree', 'Manral', 'Mayank', 'Mohan', 'Mohit', 'Moumi', 'Moumita',
                    'Prateek', 'Pratik C', 'Praveen', 'Priyanka', 'Rahul', 'Rajarshi', 'Satendra', 'Shikhar', 'Shiladitya', 'Soorma',
                    'Soumya Banerjee', 'Soumya Kartik', 'Souvick', 'Sreetama', 'Vipul', 'Vivek John', 'Vivek Kumar']
    index = 2
    for i in range(len(studentNames)):
        raw_data = [studentNames[i], "0"]
        sheet.insert_row(raw_data, index)
        index += 1
