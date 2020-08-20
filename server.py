from flask import Flask, render_template, request, url_for, redirect
from forms import SubmitForm
import os

#app = Flask(__name__) #initialize flask app, shouldnt rly change
app = Flask(__name__,
            static_url_path='',
            static_folder='static')
app.config['SECRET_KEY'] = 'haiii'
uploadFile = 'static/this.mp4'

#@app.route('/') #create route that's a single slash, this is wat u get: http://127.0.0.1:5000/
@app.route('/', methods=['GET', 'POST'])
def home():#function associated with this route? delete everyhting in uploads folder
    if (os.path.exists(uploadFile)): #delete everything in upload(static) folder
        os.remove(uploadFile)
    form = SubmitForm()
    if form.is_submitted():
        fileContent = form.inputFile.data
        fileName = fileContent.filename
        fileContent.save(uploadFile) #delete contents of upload file somehow, prob at beginning of this function
        return redirect(url_for('display'))
    return render_template('home.html', form = form)

@app.route('/display')
def display():
    #f = open(uploadFile)
    #read_data = f.read()
    #return render_template('display.html', fileContent = read_data)
    return render_template('display.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__": #convention to be true
    app.run()
