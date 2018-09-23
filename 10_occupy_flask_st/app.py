from flask import Flask, render_template
from random import choice
app=Flask(__name__)
def dictionaryMaker():
    dictionary = {}
    file = open('data/occupations.csv','r')
    straw = file.read()
    lines = straw.split("\n")
    #delete useless lines
    del lines[0]
    del lines[-1]
    del lines[-1]
    for line in lines:
        #sets comma to last comma (only relevant)
        comma=line.rfind(",")
        #before comma = key, after = val
        key =line[:comma]
        val = line[comma+1:]
        dictionary[key] = val
    return dictionary

def randomJob():
    jobs = dictionaryMaker()
    #weightedJobs will store reps of jobs
    weightedJobs = []
    for jobKey in jobs:
        #weight -> freq of each job given by percentage
        weight = float(jobs[jobKey]) * 10
        #adds correct number of reps to list
        weightedJobs += [jobKey,] * int(weight)
    return choice(weightedJobs)

@app.route("/")
def helloWorld():
    return "go to /occupations"

@app.route("/occupations")
def occupations():
    return render_template('template.html',randomJob=randomJob(),jobs=dictionaryMaker())

if (__name__ == "__main__"):
    app.debug = True
    app.run()
