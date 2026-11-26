import sqlite3 as sql


def listExtension():
    con = sql.connect(".database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension").fetchall()
    con.close()
    return data


def insertContact(email, name):
    con = sql.connect(".database/data_source.db")
    cur = con.cursor()
    cur.execute("INSERT INTO contact_list (email,name) VALUES (?,?)", (email, name))
    con.commit()
    con.close()


def listSSA():
    con = sql.connect(".database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension WHERE language = 'SSA'").fetchall()
    con.close()
    return data


def listSG():
    con = sql.connect(".database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension WHERE language = 'SG'").fetchall()
    con.close()
    return data


def listSF():
    con = sql.connect(".database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension WHERE language = 'SF'").fetchall()
    con.close()
    return data


def listSTT():
    con = sql.connect(".database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension WHERE language = 'STT'").fetchall()
    con.close()
    return data


def listSS():
    con = sql.connect(".database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension WHERE language = 'SS'").fetchall()
    con.close()
    return data


def listSI():
    con = sql.connect(".database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension WHERE language = 'SI'").fetchall()
    con.close()
    return data
