from flask import Flask, render_template, request
import os
from sentiment_analysis_twitter import SentimentAnalysis
# ----------------------------------------------
#     DECLARATIONS
# ----------------------------------------------
static_folder = 'static'
template_folder = "templates"
app = Flask(__name__,
            static_folder=static_folder,
            template_folder=template_folder)
sa = SentimentAnalysis()

# ----------------------------------------------
#     ROUTINGS
# ----------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/sentiment', methods=["POST"])
def sentiment():
    try:
        searchTerm = str(request.form['term'])
        NoOfTerms = int(request.form['number'])
    except:
        searchTerm = "Harry Potter"
        NoOfTerms = 10
    sa.DownloadData(searchTerm, NoOfTerms)
    return render_template("show.html")
# ----------------------------------------------
#     MAIN FUNTION
# ----------------------------------------------
def main():
    host = "0.0.0.0"
    port = 80
    debug = True
    app.run(host, port, debug)


if __name__ == '__main__':
    main()
