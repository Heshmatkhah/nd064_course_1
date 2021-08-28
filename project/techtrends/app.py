from flask import Flask, json, render_template, request, url_for, redirect, flash

from .databse import get_db_connection, get_post, get_post_count, get_connection_count

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


# Health check endpoint
@app.route('/healthz')
def healthcheck():
	response = app.response_class(
		response=json.dumps({"result": "OK - healthy"}),
		status=200,
		mimetype='application/json'
	)
	return response


# Metrics endpoint
@app.route('/metrics')
def metrics():
	# as we use 2 different connections for gathering the information,
	# each time we call `/metrics`, db_connection_count increases by 2
	data = {
		"db_connection_count": get_connection_count(),
		"post_count": get_post_count(),
	}
	response = app.response_class(
		response=json.dumps(data),
		status=200,
		mimetype='application/json'
	)
	return response


# Define the main route of the web application
@app.route('/')
def index():
	connection = get_db_connection()
	posts = connection.execute('SELECT * FROM posts').fetchall()
	connection.close()
	return render_template('index.html', posts=posts)


# Define how each individual article is rendered
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
	post = get_post(post_id)
	if post is None:
		app.logger.debug(f"Article with id {post_id} not found!")
		return render_template('404.html'), 404
	else:
		app.logger.debug(f"Existing article is retrieved: {post['title']}")
		return render_template('post.html', post=post)


# Define the About Us page
@app.route('/about')
def about():
	app.logger.debug(f"The `About Us` page is retrieved")
	return render_template('about.html')


# Define the post creation functionality
@app.route('/create', methods=('GET', 'POST'))
def create():
	if request.method == 'POST':
		title = request.form['title']
		content = request.form['content']

		if not title:
			flash('Title is required!')
		else:
			connection = get_db_connection()
			connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
			                   (title, content))
			connection.commit()
			connection.close()

			app.logger.debug(f"New article is created: {title}")

			return redirect(url_for('index'))

	return render_template('create.html')


# start the application on port 3111
if __name__ == "__main__":
	app.run(host='0.0.0.0', port='3111')
