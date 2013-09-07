import random
from flask import Flask, render_template
app = Flask(__name__)

file = open('studentdata', 'r')
lines = file.readlines()
global lines
file.close()

@app.route("/")
def index():
    numberOfStudents = 3
    students = chooseStudents(numberOfStudents)
    
    name = []
    handle = []
    year = []
    focus = []
    featured = []

    studentIndex = 0
    for student in students:
        student = lines[students[studentIndex]] 
        cols = student.split('\t')

        if (studentIndex == 0):
            featuredName = cols[0]
            featuredFocus = cols[4]
            featured.append('featured')
        else:
            featured.append('notfeatured')

        name.append(cols[0])
        handle.append(cols[1])
        year.append(cols[2])
        focus.append(cols[4])
        studentIndex += 1

    order = [0, 1, 2]
    random.shuffle(order)

    # for the record, this is a dump way of passing data to the template.. I didn't realize that Flask templates
    # support logic for loops and multiple data structures. this and associated code above should be simplified
    return render_template('index.html', featuredName=featuredName, featuredFocus=featuredFocus, name1=name[order[0]], handle1=handle[order[0]], year1=year[order[0]], focus1=focus[order[0]], featured1=featured[order[0]], name2=name[order[1]], handle2=handle[order[1]], year2=year[order[1]], focus2=focus[order[1]], featured2=featured[order[1]], name3=name[order[2]], handle3=handle[order[2]], year3=year[order[2]], focus3=focus[order[2]], featured3=featured[order[2]])

def chooseStudents(num=3):
    students = []
    while (len(set(students)) < num):
        randomid = random.randrange(0, len(lines))
        students.append(randomid)
    return students

if __name__ == "__main__":
    app.run()