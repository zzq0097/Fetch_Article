from flask import Flask


def register_blueprints(app):
    from app.api.crawl import crawl
    app.register_blueprint(crawl)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    register_blueprints(app)
    return app
