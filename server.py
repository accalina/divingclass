from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = "DIVING_APP_SCHOOL"

from blueprints.auth import auth
app.register_blueprint(auth)

from blueprints.user import user
app.register_blueprint(user)

from blueprints.admin import admin
app.register_blueprint(admin)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)
