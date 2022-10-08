import json
from re import sub
from urllib import request, response
import requests
from flask import Flask, render_template

app = Flask(__name__)


def get_api():
    sr = "/wholesomememes"
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests.request("GET",url).text)
    memelarge = response["preview"][-2]
    subreddit = response["subreddit"]
    return memelarge,subreddit


@app.route("/")
def index():
    meme_pic , subreddit = get_api()
    return render_template("meme_index.html",meme_pic = meme_pic, subreddit = subreddit)
    # return render_template("meme_index.html",meme_pic = meme_pic, subreddit = subreddit,get_api = get_api())
    # return "You want to watch a meme?"
@app.route("/forward/", methods=['POST'])
def get_api_2():
    sr = "/wholesomememes"
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests.request("GET",url).text)
    memelarge = response["preview"][-2]
    subreddit = response["subreddit"]
    return render_template("meme_index.html",meme_pic = memelarge, subreddit = subreddit)

app.run(host= '0.0.0.0',port = "8080")