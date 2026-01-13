import requests,sqlite3


url="http://127.0.0.1:5000/books"
response=requests.get(url) #dataa that api sendss back is now in response
books=response.json()
conn=sqlite3.connect("books.db")

cursor = conn.cursor()#contrls sql commands


cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
               id Integer Primary key autoincrement,
               title text,
               author text,
               year text)
""")

for book in books:
    cursor.execute("Insert into books(title,author,year) values (?,?,?)",(book["title"],book["author"],book["year"]))
conn.commit()
cursor.execute("select * from books")
data=cursor.fetchall()
for row in data:
    print(row)

conn.close()    