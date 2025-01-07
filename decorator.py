# تعریف کاربران و رمزهای عبور (شبیه پایگاه داده)
users = {"admin": "1234", "user": "abcd"}

# متغیر برای ذخیره وضعیت ورود کاربر
current_user = None

# دکوریتور برای کنترل دسترسی
def login_required(func):
    def wrapper(*args, **kwargs):
        if current_user is None:
            print("Access denied: You must log in first!")
            return
        return func(*args, **kwargs)
    return wrapper

# تابع ورود کاربر
def login(username, password):
    global current_user
    if username in users and users[username] == password:
        current_user = username
        print(f"Welcome, {username}! You are now logged in.")
    else:
        print("Invalid username or password.")

# تابع خروج کاربر
def logout():
    global current_user
    if current_user:
        print(f"Goodbye, {current_user}. You are now logged out.")
        current_user = None
    else:
        print("No user is currently logged in.")

# صفحه‌ای که نیاز به ورود دارد
@login_required
def dashboard():
    print(f"Welcome to your dashboard, {current_user}!")

# صفحه عمومی (نیاز به ورود ندارد)
def home():
    print("Welcome to the homepage. This page is accessible to everyone.")

# اجرای برنامه
print("=== Start ===")
home()  # صفحه عمومی
dashboard()  # تلاش برای دسترسی بدون ورود

login("admin", "1234")  # ورود با کاربر معتبر
dashboard()  # دسترسی به داشبورد بعد از ورود

logout()  # خروج کاربر
dashboard()  # تلاش برای دسترسی به داشبورد بعد از خروج
