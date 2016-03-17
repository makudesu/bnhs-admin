import sqlsoup
db = sqlsoup.SQLSoup("mysql://bnhs:123456@db4free.net/codecalltut")
users = db.tblprereg.all()
print users
