from flask import Flask, render_template
import datetime, requests

app = Flask(__name__)

@app.route('/')
def hello():
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    this_year = date.strftime("%Y")
    return render_template('index.html', year=this_year)


agify_url = "https://api.agify.io"
genderize_url= "https://api.genderize.io"


@app.route('/guess/<namer>')
def guesser(namer):
    params = {'name': namer}
    age_response = requests.get(agify_url, params=params)
    age_data = age_response.json()
    gender_response = requests.get(genderize_url, params=params)
    gender_data = gender_response.json()
    return render_template('guess.html',
                           user=str(namer).capitalize(),
                           gender=gender_data["gender"],
                           age=age_data["age"])


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url="https://api.npoint.io/590c987581c690e21792"
    response = requests.get(blog_url)
    all_posts= response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
