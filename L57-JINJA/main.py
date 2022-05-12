from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/590c987581c690e21792"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/posts/<num>')
def blog_post(num):
    blog_url = "https://api.npoint.io/590c987581c690e21792"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("post.html", post=all_posts[int(num)-1])


if __name__ == "__main__":
    app.run(debug=True)
