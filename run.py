from sqlalchemy import text

from app import create_app, db

app = create_app()

if __name__ == "__main__":

    try:

        with app.app_context():

            db.session.execute(text("SELECT 1"))

            print("SUCCESS: Database Connected")

            db.create_all()

    except Exception as e:

        print("ERROR: Database Connection Failed")
        print(e)

    app.run(debug=True)