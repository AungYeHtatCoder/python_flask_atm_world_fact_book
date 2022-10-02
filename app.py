import imp
from flask import Flask, render_template, request, redirect, url_for, flash
import json

w= json.load(open("world.json"))
page_size = 10
page_number=0
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', w = w[0:page_size],page_size=page_size,page_number=page_number)

@app.route('/begin/<b>')


def beginpage(b):
    bn = int(b)
    return render_template('index.html',
                           w = w[bn:bn+page_size],
                           page_number = bn,
                           page_size = page_size
                           )


@app.route('/continent/<a>')
def continentpage(a):
    cl = [c for c in w if c['continent']==a]
    return render_template('continent.html', length_of_cl = len(cl), cl = cl,
                           a = a) 
@app.route('/countryByName/<i>')
def countryByNamepage(i):
    c = None
    for x in w:
        if x['name']== i:
            c = x
    return render_template('country.html', c = c)

@app.route('/country/<i>')
def countrypage(i):
    return render_template('country.html', c = w[int(i)])


@app.route('/delete/<n>')
def deleteCountry(n):
    i = 0
    for c in w:
        if c['name'] == n:
            break
        i = i+1
    del w[i]
    return render_template('index.html',
                           page_number = 0,
                           page_size = page_size,
                           w = w[0:page_size])


if __name__ == '__main__':
    app.run(debug=True)