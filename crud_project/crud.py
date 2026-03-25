import sqlite3

DB_NAME = "database.db"

def connect():
    return sqlite3.connect(DB_NAME)

# CREATE
def add_user(name, age):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
    print("User added successfully!")

# READ
def view_users():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    if users:
        print("\n--- Users List ---")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")
    else:
        print("No users found.")

# UPDATE
def update_user(user_id, name, age):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET name=?, age=? WHERE id=?",
        (name, age, user_id)
    )
    conn.commit()
    conn.close()
    print("User updated successfully!")

# DELETE
def delete_user(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    print("User deleted successfully!")