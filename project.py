from flask import Flask, render_template, request
import random
import csv

SHOWS = []
GENRES = []
NAMES = []
with open("tvshows.csv", encoding="utf8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            SHOWS.append({"name": row["title"], "genre": row["genre"], "mood": row["mood"]})

for show in SHOWS:
        if show["genre"] not in GENRES:
                GENRES.append(show["genre"])
for show in SHOWS:
        if show["name"] not in NAMES:
                NAMES.append(show["name"])

app = Flask(__name__)

@app.route("/")
def main():
        return render_template("index.html")


@app.route("/mood", methods=["GET", "POST"])
def mood():
        return render_template("mood.html")
        

@app.route("/genre", methods=["GET", "POST"])
def genre():
        return render_template("genre.html", genres = GENRES)


@app.route("/favorite", methods=["GET", "POST"])
def favorite():
        return render_template("favorite.html")


@app.route("/nostalgic", methods=["GET", "POST"])
def nostalgic():
        nostalgics = []
        for show in SHOWS:
                if show["mood"] == "nostalgic":
                        nostalgics.append(show["name"])
        choice = str(random.choice(nostalgics))
        return render_template("nostalgic.html", choice=choice)


@app.route("/laugh", methods=["GET", "POST"])
def laugh():
        laughing = []
        for show in SHOWS:
                if show["mood"] == "laugh":
                        laughing.append(show["name"])
        choice = str(random.choice(laughing))
        return render_template("laugh.html", choice=choice)


@app.route("/thrilled", methods=["GET", "POST"])
def thrilled():
        thrilling = []
        for show in SHOWS:
                if show["mood"] == "thrilled":
                        thrilling.append(show["name"])
        choice = str(random.choice(thrilling))
        return render_template("thrilled.html", choice=choice)


@app.route("/learn", methods=["GET", "POST"])
def learn():
        learning = []
        for show in SHOWS:
                if show["mood"] == "learn":
                        learning.append(show["name"])
        choice = str(random.choice(learning))
        return render_template("learn.html", choice=choice)

@app.route("/showgenre", methods=["POST"])
def showgenre():
        shows_genre = []
        if request.form.get("genre") not in GENRES:
                return render_template("failure.html", message = "Please select a genre!")
        
        for show in SHOWS:
                if request.form.get("genre") == show["genre"]:
                        shows_genre.append(show["name"])
        
        choice = str(random.choice(shows_genre))
        return render_template("showgenre.html", choice=choice)

@app.route("/similar", methods=["POST"])
def similar():
        similars = []
        favorite = []
        if request.form.get("tvshow") not in NAMES:
                return render_template("failure.html", message = "Sorry, we don't know this show :(")
        for show in SHOWS:
                if request.form.get("tvshow") == show["name"]:
                        favorite.append(show)
        for show in SHOWS:
                if show not in favorite:
                        if show["genre"] == favorite[0]["genre"] or show["mood"] == favorite[0]["mood"]:
                                similars.append(show["name"])
        
        choice = str(random.choice(similars))
        return render_template("similar.html", choice=choice) 
 
        


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)