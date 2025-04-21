import requests
import redis
import json

# اتصال به Redis (پیش‌فرض: localhost، پورت 6379)
r = redis.Redis(host='localhost', port=6379, db=0)

# دریافت داده از یک API عمومی
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

if response.status_code == 200:
    users = response.json()

    for user in users:
        user_id = user['id']
        # ذخیره‌ی اطلاعات هر کاربر به صورت hash در Redis
        r.hset(f"user:{user_id}", mapping={
            "name": user["name"],
            "username": user["username"],
            "email": user["email"]
        })

        # print(f"✅ کاربر {user['name']} ذخیره شد.")

else:
    print("❌ دریافت اطلاعات از API با خطا مواجه شد.")

# بازیابی و نمایش اطلاعات کاربران ذخیره‌شده
print("\n📦 بازیابی اطلاعات از Redis:\n")

for user_id in range(1, 11):
    key = f"user:{user_id}"
    if r.exists(key):
        user_data = r.hgetall(key)
        print(f"👤 کاربر {user_id}:")
        for field, value in user_data.items():
            print(f"   {field.decode('utf-8')}: {value.decode('utf-8')}")
        print()
