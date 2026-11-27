
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Expense
from datetime import date
from decimal import Decimal, InvalidOperation

main = Blueprint("main", __name__)


@main.route("/")
def index():
    expenses = Expense.query.order_by(
        Expense.expense_date.desc()
    ).all()

    total = db.session.query(
        db.func.sum(Expense.amount)
    ).scalar() or Decimal("0.00")

    return render_template(
        "index.html",
        expenses=expenses,
        total=total
    )


@main.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        try:
            title = request.form.get("title", "").strip()
            amount = Decimal(request.form.get("amount", ""))
            category = request.form.get("category", "")
            expense_date = date.fromisoformat(
                request.form.get("expense_date", "")
            )
            notes = request.form.get("notes", "").strip()

            if not title or not category or amount <= 0:
                raise ValueError("Enter valid expense details.")

            if len(title) > 100 or len(category) > 50:
                raise ValueError("Title or category is too long.")

            expense = Expense(
                title=title,
                amount=amount,
                category=category,
                expense_date=expense_date,
                notes=notes or None
            )

            db.session.add(expense)
            db.session.commit()

            flash("Expense added successfully!", "success")
            return redirect(url_for("main.index"))

        except (ValueError, InvalidOperation):
            db.session.rollback()
            flash("Invalid expense details. Please try again.", "danger")

    return render_template("add_expense.html")


@main.route("/delete/<int:id>", methods=["POST"])
def delete_expense(id):
    expense = db.session.get(Expense, id)

    if expense:
        db.session.delete(expense)
        db.session.commit()
        flash("Expense deleted successfully!", "success")
    else:
        flash("Expense not found.", "danger")

    return redirect(url_for("main.index"))
