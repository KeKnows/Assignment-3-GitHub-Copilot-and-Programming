
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Demo posts data
posts = [
    {
        'id': 1,
        'image': 'placeholder.jpg',
        'likes': 0,
        'comments': []
    },
    {
        'id': 2,
        'image': 'placeholder.jpg',
        'likes': 0,
        'comments': []
    },
    {
        'id': 3,
        'image': 'placeholder.jpg',
        'likes': 0,
        'comments': []
    }
]

@app.route('/', methods=['GET', 'POST'])
def feed():
    global posts
    if request.method == 'POST':
        post_id = int(request.form.get('post_id'))
        for post in posts:
            if post['id'] == post_id:
                if 'like' in request.form:
                    post['likes'] += 1
                elif 'comment' in request.form:
                    comment = request.form.get('comment_text', '').strip()
                    if comment:
                        post['comments'].append(comment)
        return redirect(url_for('feed'))
    return render_template('post.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
