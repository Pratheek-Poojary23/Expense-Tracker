
from datetime import date
from app import db


class Expense(db.Model):
    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(
        db.String(100),
        nullable=False
    )

    amount = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=False
    )

    expense_date = db.Column(
        db.Date,
        nullable=False,
        default=date.today
    )

    notes = db.Column(
        db.Text,
        nullable=True
    )

    def __repr__(self):
        return f"<Expense {self.title}: {self.amount}>"


"""
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    amount NUMERIC(10,2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    expense_date DATE NOT NULL,
    notes TEXT
);
"""
