from os import strerror

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self, line, message):
        self.message = message
        self.line = line
        
class FileEmpty(StudentsDataException):
    def __init__(self, message):
        self.message = message

filename = input("Enter source file name: ")
try:
    source = open(filename, 'rt')
except Exception as e:
    print("Cannot open source file:", strerror(e.errno))
    exit(e.errno)
    
students = {}
line_no = 0

try:
    for line in source:
        line_no += 1
        line = line.split()
        if len(line) == 3:    
            student = line[0] + " " + line[1]
            point = float(line[2])
            if student in students:
                students[student] += point
            else:
                students[student] = point
        elif len(line) == 0:
            continue
        else:
            raise BadLine(line_no, "Bad line detected at line:")

    if len(students) == 0:
        raise FileEmpty("File is empty.")

    sorted_names = sorted(students)
    for name in sorted_names:
        print(name, "\t", students[name])
except BadLine as b:
    print(b.message, b.line)
except FileEmpty as f:
    print(f.message)

