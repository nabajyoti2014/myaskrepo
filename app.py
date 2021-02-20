from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = ["https://demost009.blob.core.windows.net/images/cat1.png","https://demost009.blob.core.windows.net/images/cat2.png"]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")