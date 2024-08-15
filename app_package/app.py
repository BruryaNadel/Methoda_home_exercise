

# @app.route('/')
# def index():
#     return render_template('index.html')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://status_user:status_user@localhost/status_manager'

from flask import Flask, render_template
#from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from .api import api
from .models import db
import os

#print("Current Working Directory:", os.getcwd())
#print("Templates Directory Exists:", os.path.exists('templates'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://status_user:status_user@localhost/status_manager'
db = SQLAlchemy(app)
#db.init_app(app)
print(f"Templates Directory Path: {os.path.abspath(app.template_folder)}")

# Register the API Blueprint
app.register_blueprint(api, url_prefix='/api')

# Your models and routes would go here
@app.route('/')
def index():
    template_dir = os.path.abspath(app.template_folder)
    print(f"\n\n--- Templates Directory Path: {template_dir} ---\n", flush=True)
        
    try:
        files_in_template_dir = os.listdir(template_dir)
        print(f"\n\n--- Files in Templates Directory: {files_in_template_dir} ---\n", flush=True)
    except Exception as e:
        print(f"\n\n--- Error listing files: {e} ---\n", flush=True)
        
    print(f"Attempting to render 'index.html'...", flush=True)
    return render_template('index.html')  # Attempt to render the template

if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()  # Create database tables
#     app.run(debug=True)