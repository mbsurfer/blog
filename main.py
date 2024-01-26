from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

# load all blog posts when the server starts
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
posts = [Post(post_id=data['id'], title=data['title'], subtitle=data['subtitle'], body=data['body']) for data in response.json()]


@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=posts)


@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    # find the post that matches the blog_id passed in from the url
    blog_post = [blog_post for blog_post in posts if blog_post.id == blog_id][0]
    return render_template("post.html", post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
