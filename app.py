import random
from flask import Flask, render_template
app = Flask(__name__)

app.debug = True;

file = open('studentdata', 'r')
global lines
lines = file.readlines()
file.close()



@app.route("/")
def index():
    numberOfStudents = 3
    students = chooseStudents(numberOfStudents)
    
    name = []
    photo = []
    year = []
    gender = []
    focus = []
    featured = []

    studentIndex = 0
    for student in students:
        student = lines[students[studentIndex]] 
        cols = student.split('\t')

        if (studentIndex == 0):
            featuredName = cols[0]
            featuredPhoto = cols[1]
            featuredYear = cols[2]
            featuredFocus = cols[3]
            featured.append('featured')
        else:
            featured.append('notfeatured')

        name.append(cols[0])
        photo.append(cols[1])
        year.append(cols[2])
        focus.append(cols[3])
        gender.append(cols[4])
        studentIndex += 1

    order = [0, 1, 2]
    random.shuffle(order)

    # for the record, this is a dump way of passing data to the template.. I didn't realize that Flask templates
    # support logic for loops and multiple data structures. this and associated code above should be simplified
    return render_template('index.html', featuredName=featuredName, featuredFocus=featuredFocus, featuredYear=featuredYear, featuredPhoto=featuredPhoto, name1=name[order[0]], photo1=photo[order[0]], year1=year[order[0]], focus1=focus[order[0]], featured1=featured[order[0]], name2=name[order[1]], photo2=photo[order[1]], year2=year[order[1]], focus2=focus[order[1]], featured2=featured[order[1]], name3=name[order[2]], photo3=photo[order[2]], year3=year[order[2]], focus3=focus[order[2]], featured3=featured[order[2]])

def chooseStudents(num=3):
    students = []
    thisgender = random.choice(['M','F'])
    while (len(set(students)) < num):
        randomid = random.randrange(0, len(lines))
        student = lines[randomid] 
        cols = student.split('\t')
        if cols[4].strip() == thisgender and cols[1] != "placeholder.jpg" and randomid not in students:
            students.append(randomid)
    return students

if __name__ == "__main__":
    app.run()