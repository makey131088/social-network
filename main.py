from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey123"
USERS = {
    "admin": 'admin123',
    "user": 'pass456'
}


@app.route("/")
def main_page():
    login = session.get('username')
    if login is None:
        login = "Гость"
    return render_template('index.html', username=login)


@app.get("/login")
def login_page():
    if session.get('username') is not None:
        return redirect(url_for('main_page'))
    return render_template('login.html')


@app.post("/login")
def auth_user():
    username = request.form.get('login')
    password = request.form.get('password')
    if username in USERS and USERS[username] == password:
        session['username'] = username
    return redirect(url_for('main_page'))


@app.get("/registration")
def registration_pass ():
    if session.get('username') is not None:
        return redirect(url_for('main_page'))
    return render_template("registration.html")

@app.post("/registration")
def reg_user():
    email = request.form.get("email")
    login = request.form.get("login")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    if login in USERS:
        return {"status": "error", "message": "User already exists"}
    if password != confirm_password:
        return {"status": "error", "message": "Passwords don't match"}
    # TODO: complete validation logic

    USERS[login] = password
    session["session_data"] = login
    return {
        "status": "succes",
        "message": "User sucsessfully created",
        "location": url_for("main_page")
    }

NEWS = [
    {
        "id": 1,
        "title": "Запуск новой миссии на Марс",
        "content": "NASA объявила о запуске новой исследовательской миссии к Марсу, запланированной на 2025 год.",
        "author": "Иван Петров",
        "date": "2024-01-15"
    },
    {
        "id": 2,
        "title": "Прорыв в области квантовых компьютеров",
        "content": "Ученые из Китая создали квантовый компьютер, способный решать задачи в 100 раз быстрее существующих аналогов.",
        "author": "Елена Смирнова",
        "date": "2024-01-14"
    },
    {
        "id": 3,
        "title": "Открытие нового вида динозавров",
        "content": "Палеонтологи обнаружили в Аргентине останки ранее неизвестного вида травоядных динозавров.",
        "author": "Алексей Козлов",
        "date": "2024-01-13"
    },
    {
        "id": 4,
        "title": "Новый рекорд скорости интернета",
        "content": "Японские инженеры достигли скорости передачи данных 319 терабит в секунду.",
        "author": "Мария Иванова",
        "date": "2024-01-12"
    },
    {
        "id": 5,
        "title": "Искусственный интеллект научился предсказывать землетрясения",
        "content": "Нейросеть с точностью 85% предсказывает землетрясения за 7 дней до их наступления.",
        "author": "Дмитрий Сидоров",
        "date": "2024-01-11"
    }
];


@app.get("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('main_page'))


@app.route("/forgot")
def  forgot_pass():
    return render_template("forgot.html")


@app.post("/api/v1/handler")
def form_handler():
    return "OK"