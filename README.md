# Connect@Cal Coding Challenge Spring 2021 Recruitment

**What you need installed first:**
* Python 3 (https://www.python.org/downloads/)
* Virtualenv (https://virtualenv.pypa.io/en/latest/installation.html)
* A Coding Editor (we recommend Visual Studio: https://visualstudio.microsoft.com/)
* Git
* GitHub Account

**Steps for getting set up:**
1) [Fork this repo](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo)

2) Clone your github repo into your working directory:
```
git clone <FORKED GITHUB REPO URL>
```

3) Change directory to cloned repo:
```
cd <CLONED DIRECTORY NAME>
```

4) Create a virtual environment:
```
virtualenv venv
```
OR
```
python3 -m venv venv
```

5) Activate virtual environment:
```
source venv/bin/activate
```

6) 
```
pip3 install -r requirements.txt
```

7)
```
cd imageUploader
```

8)
```
export FLASK_APP=app.py
```

9)
```
flask run
```

9) Navigate to a browser and navigate to http://127.0.0.1:5000/

To deactivate your virtual environment, all you need to do is type 
```
deactivate
```
or CTRL-C. 

**Starting the Challenge:**
1) Look over the source code and familiarize yourself with the general structure
2) Look at the /tasks folder to see a list of markdown files where each markdown file corresponds to a task
3) Start with the first task and finish each following task sequentially
4) The code you need to write for each Task will be clearly denoted by:
```
# BEGIN TASK <TASK NUMBER>
```

# Submission Process
Look at submission.md for more details. 

Submission form: https://forms.gle/Cn53H7geLX2JqT5H9

# Helpful Resources
We don't expect you to know how to do this from the get go. 

Don't know Flask? Their documentation is pretty awesome, so first check that out: https://flask.palletsprojects.com/en/1.1.x/

Here are some free resources that might be helpful throughout this challenge:
- https://www.google.com/
- https://stackoverflow.com/
- https://github.com/
- https://developer.mozilla.org/en-US/
- https://www.w3schools.com/
- https://developers.google.com/web/tools/chrome-devtools

# What we are looking for
If you find yourself spending more than 8 hours on this challenge, just submit what you have via the Google Form. We'll have space for you in the form for you to talk about your problem solving process!

Our goal for this challenge is to understand how you approach challenging problems.

This is only part of the appplication process. We have a holistic process and evaluate candidates based on a number of variables outside of strictly coding aptitude.

You do not need to completely finish this challenge to get an offer. 

Rest assured, we will look at all of your code and comments.

# Have Questions?
Come over to our office hours at:
- Fridays (4 - 6 PM PST): https://berkeley.zoom.us/j/91407780777?pwd=WTk2ZFcxRXNKYXVEQSt3a1pjYldCQT09
