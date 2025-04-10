from pymongo import MongoClient

# اتصال به MongoDB محلی
client = MongoClient("mongodb://localhost:27017/")

# انتخاب دیتابیس و کالکشن
db = client["mydb"]
collection = db["names"]

# --------- CREATE ---------
new_name = {"name": "محمدامین", "gender": "boy"}
collection.insert_one(new_name)
print("✅ داده جدید اضافه شد.")

# --------- READ ---------
print("📥 خواندن همه داده‌ها:")
for doc in collection.find():
    print(doc)

# --------- UPDATE ---------
query = {"name": "محمدامین"}
new_values = {"$set": {"name": "محمد امین (ویرایش‌شده)"}}
collection.update_one(query, new_values)
print("✏️ نام ویرایش شد.")

# --------- DELETE ---------
collection.delete_one({"name": "محمد امین (ویرایش‌شده)"})
print("🗑️ حذف انجام شد.")

# پایان
client.close()
