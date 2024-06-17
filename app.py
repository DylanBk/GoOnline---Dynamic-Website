from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/tutors')
def tutors():
    return render_template('tutors.html')

@app.route('/lessons/<lesson>')
def lessons(lesson):
    lessons = ["Programming Concepts", "Design and Development", "Data Applications", "Frameworks", "Network Infrastructure and Security", "Industry Concepts", "Industry Skills"]
    return render_template('lessons.html', lesson=lesson, lessons=lessons)

if __name__ == "__main__":
    app.run()