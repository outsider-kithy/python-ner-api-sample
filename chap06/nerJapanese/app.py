import os
import sys
from flask import Flask

def create_app():
	app = Flask(__name__)

	from company import views as company_views
	app.register_blueprint(company_views.company, url_prefix="/company")

	from name import views as name_views
	app.register_blueprint(name_views.name, url_prefix="/name")

	return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)