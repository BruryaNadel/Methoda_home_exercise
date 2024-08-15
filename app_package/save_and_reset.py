from .models import db
from .app import app

@app.route('/reset', methods=['POST'])
def reset_configuration():
    db.drop_all()
    db.create_all()
    return '', 204
