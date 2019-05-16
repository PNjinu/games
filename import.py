import csv

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://rhorbjqbilyivg:d21a06382bbf64da498543deb0692e08cd4f68e6b16843582049fca5e59ac9ce@ec2-23-23-228-132.compute-1.amazonaws.com:5432/db62nln4h7f707")
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