from app import app

from . views import index
from . auth.views import auth

app.register_blueprint(index)
app.register_blueprint(auth)