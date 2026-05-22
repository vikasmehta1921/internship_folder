import sqlite3

# Create database and connect
conn = sqlite3.connect("college.db")

# Create cursor object
cur = conn.cursor()

# 1. Create Tables
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS courses(
    cid INTEGER PRIMARY KEY,
    course_name TEXT,
    fees INTEGER
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS teachers(
    tid INTEGER PRIMARY KEY,
    teacher_name TEXT,
    subject TEXT
)
""")

print("Tables created successfully")

# 2. Insert Records
cur.execute("INSERT INTO students VALUES(1,'Vikas','Jaipur')")
cur.execute("INSERT INTO students VALUES(2,'Rahul','Delhi')")
cur.execute("INSERT INTO students VALUES(3,'Aman','Mumbai')")

cur.execute("INSERT INTO courses VALUES(101,'Python',5000)")
cur.execute("INSERT INTO courses VALUES(102,'Java',6000)")

cur.execute("INSERT INTO teachers VALUES(1,'Sharma Sir','Math')")
cur.execute("INSERT INTO teachers VALUES(2,'Verma Sir','Science')")

conn.commit()

print("Records inserted successfully")

# 3. Different Select Operations

print("\nAll Students")
data = cur.execute("SELECT * FROM students")
for row in data:
    print(row)

print("\nStudents from Jaipur")
data = cur.execute("SELECT * FROM students WHERE city='Jaipur'")
for row in data:
    print(row)

print("\nCourse Names Only")
data = cur.execute("SELECT course_name FROM courses")
for row in data:
    print(row)

# 4. Update Data
cur.execute("UPDATE students SET city='Udaipur' WHERE id=1")
conn.commit()

print("\nAfter Update")
data = cur.execute("SELECT * FROM students")
for row in data:
    print(row)

# 5. Delete Data
cur.execute("DELETE FROM students WHERE id=3")
conn.commit()

print("\nAfter Delete")
data = cur.execute("SELECT * FROM students")
for row in data:
    print(row)

# Close connection
conn.close()

print("\nDatabase operations completed successfully")