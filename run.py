from app import create_app, db

if __name__ == "__main__":
    flask_app = create_app('dev')
    with flask_app.app_context(): # to ensure that the SQLAlchemy binds with my application(there may be multiple apps)
        db.create_all()
    flask_app.run(debug=True)
