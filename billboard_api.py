import billboard
from flask import Flask

app = Flask(__name__)
#myapi

#myapizaid

@app.route('/')
def get_top100():
    chart = billboard.ChartData('hot-100')
    mydict={}
    for i in range(0,10):
        mydict[i] = str(chart[i])
    return str(mydict)

@app.route('/artist10')
def get_topArtist():
    chart = billboard.ChartData('artist-100')
    mydict={}
    for i in range(0,10):
        mydict[i] = str(chart[i])
    return str(mydict)

@app.route('/ondemand')
def get_ondemand():
    chart = billboard.ChartData('on-demand-songs')
    mydict={}
    for i in range(0,10):
        mydict[i] = str(chart[i])
    return str(mydict)


if __name__ == '__main__':
    app.run()
