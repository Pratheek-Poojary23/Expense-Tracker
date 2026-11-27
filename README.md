
# Expense Tracker

A Python Flask-based web application for tracking daily expenses.

## Features

- Add and manage expenses.
- View expense records.
- Delete expenses.
- Calculate total expenses.
- Stores expense data using SQLite.

## Run using Podman

Pull the container image from GitHub Packages:

```bash
podman pull ghcr.io/pratheek-poojary23/expense-tracker:v1.0.0
```

Run the container:

```bash
podman run -d \
  --name expense-app \
  -p 5000:5000 \
  ghcr.io/pratheek-poojary23/expense-tracker:v1.0.0
```

Open the application:

```text
http://localhost:5000
```


```

## Technology Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Podman
