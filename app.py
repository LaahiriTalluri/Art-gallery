from flask import Flask, render_template, request, redirect, session, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "artgallerysecretkey"


# ===============================
# DATABASE CONNECTION
# ===============================
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# ===============================
# HOME PAGE
# ===============================
@app.route('/')
def home():
    conn = get_db_connection()

    products = conn.execute(
        "SELECT * FROM products LIMIT 4"
    ).fetchall()

    conn.close()

    return render_template(
        "home.html",
        products=products
    )


# ===============================
# ALL PRODUCTS PAGE
# ===============================
@app.route('/products')
def products():
    conn = get_db_connection()

    products = conn.execute(
        "SELECT * FROM products"
    ).fetchall()

    conn.close()

    return render_template(
        "products.html",
        products=products
    )


# ===============================
# SINGLE PRODUCT DETAILS
# ===============================
@app.route('/product/<int:id>')
def product_details(id):
    conn = get_db_connection()

    product = conn.execute(
        "SELECT * FROM products WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    return render_template(
        "product_details.html",
        product=product
    )


# ===============================
# REGISTER PAGE
# ===============================
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        conn = get_db_connection()

        conn.execute("""
            INSERT INTO users
            (first_name, last_name, email, phone, password)
            VALUES (?, ?, ?, ?, ?)
        """, (first_name, last_name, email, phone, password))

        conn.commit()
        conn.close()

        flash("Registration Successful! Please Login.")
        return redirect('/login')

    return render_template("register.html")


# ===============================
# LOGIN PAGE
# ===============================
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()

        user = conn.execute("""
            SELECT * FROM users
            WHERE email=? AND password=?
        """, (email, password)).fetchone()

        conn.close()

        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['first_name']

            flash("Login Successful!")
            return redirect('/')

        else:
            flash("Invalid Email or Password")

    return render_template("login.html")


# ===============================
# LOGOUT
# ===============================
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged Out Successfully")
    return redirect('/')


# ===============================
# ADD TO CART
# ===============================
@app.route('/add-to-cart/<int:id>')
def add_to_cart(id):

    if 'cart' not in session:
        session['cart'] = []

    cart = session['cart']
    cart.append(id)

    session['cart'] = cart

    flash("Product Added To Cart")
    return redirect('/cart')


# ===============================
# CART PAGE
# ===============================
@app.route('/cart')
def cart():

    if 'cart' not in session:
        session['cart'] = []

    cart_ids = session['cart']

    items = []
    total = 0

    conn = get_db_connection()

    for pid in cart_ids:

        product = conn.execute(
            "SELECT * FROM products WHERE id=?",
            (pid,)
        ).fetchone()

        if product:
            items.append(product)
            total += product['price']

    conn.close()

    return render_template(
        "cart.html",
        cart_items=items,
        total=total
    )


# ===============================
# REMOVE FROM CART
# ===============================
@app.route('/remove-from-cart/<int:id>')
def remove_from_cart(id):

    if 'cart' in session:

        cart = session['cart']

        if id in cart:
            cart.remove(id)

        session['cart'] = cart

    flash("Item Removed")
    return redirect('/cart')

@app.route('/account')
def account():

    if 'user_id' not in session:
        flash("Please login first")
        return redirect('/login')

    conn = get_db_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE id=?",
        (session['user_id'],)
    ).fetchone()

    conn.close()

    return render_template(
        "account.html",
        user=user
    )
# ===============================
# RUN APP
# ===============================
if __name__ == '__main__':
    app.run(debug=True)