import csv

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("GAMESDB_URL"))
db = scoped_session(sessionmaker(bind=engine))


questions = db.execute("SELECT * FROM questions;").fetchall()
if questions:
    for question in questions:
        print(question)
    print("Questions are already imported")
else:
    q = open("ques.csv")
    reader = csv.reader(q)
    for question in reader:
        db.execute("INSERT INTO questions (question) VALUES (:question)", {"question": question})
        print(f"The question: '{question}' has been added.")
    db.commit()
    print("All questions have successfully been added.")