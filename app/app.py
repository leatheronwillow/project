from flask import Flask, render_template, session, request, flash, redirect
from flask_session import Session
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, apology

# import relevant modules

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Connect to database
#con = sqlite3.connect("contrast.db", autocommit=False)
#cur = con.cursor()

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def orders():
    """Show current orders"""
    return render_template("orders.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        
        # establish connection with database
        con = sqlite3.connect("contrast.db", autocommit=False)
        cur = con.cursor()

        # Query database for username
        result = cur.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),))
        rows = result.fetchall()
        con.close()

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["people_id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
    
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    
    #establish connection with database
    con = sqlite3.connect("contrast.db", autocommit=False)
    cur = con.cursor()

    # if user registered via POST (i.e. submitted the form)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 400)
        
        # Ensure first name is entered
        elif not request.form.get("first-name"):
            return apology("must provide first name", 400)
        
        # Ensure last name is entered
        elif not request.form.get("last-name"):
            return apology("must provide last name", 400)
        
        # Ensure password confirmation matches password field
        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("Confirmation does not match password", 400)
        
        else:
            result = cur.execute("SELECT username FROM users WHERE username = ?", (request.form.get("username"),))
            if result.fetchone():
                return apology("Username already exists", 400)        

        # generate password hash
        hash = generate_password_hash(request.form.get("password"))

        username = str(request.form.get("username"))
        first_name = str(request.form.get("first-name"))
        last_name = str(request.form.get("last-name"))

        if request.form.get("mobile"):
            mobile = str(request.form.get("mobile"))
        else:
            mobile = "not given"
        
        if request.form.get("email"):
            email = str(request.form.get("email"))
        else:
            email = "not given"
        
        

        # Insert user details into people table
        cur.execute("INSERT INTO people (first_name, last_name, mobile, email) VALUES (?, ?, ?, ?)", (first_name, last_name, mobile, email))

        # Insert values for username and password hash into database
        result = cur.execute("SELECT id FROM people WHERE first_name = ? AND last_name = ?", (first_name, last_name))
        people_id = result.fetchone()[0]

        cur.execute("INSERT INTO users VALUES (?, ?, ?)", (people_id, username, hash))
        con.commit()
        con.close()

        return redirect("/")

    # user reached via GET
    else:
        return render_template("register.html")

