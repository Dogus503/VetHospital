import sqlite3


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect("data_db.sqlite")
        self.cur = self.con.cursor()

    def insert(self, result, name_test):
        self.cur.execute("INSERT INTO results(RESULTS, TEST) VALUES(?, ?);", (result, name_test))
        self.con.commit()

    def delete_all(self):
        self.cur.execute("DELETE FROM results WHERE ID>-1;")
        self.con.commit()

    def select(self, name_test):
        res = self.cur.execute("SELECT MAX(RESULTS) FROM results WHERE TEST='{}';".format(name_test))
        self.con.commit()
        return res.fetchmany()

    def select_all(self, name_test):
        res = self.cur.execute("SElECT RESULTS FROM results WHERE TEST = '{}';".format(name_test))
        self.con.commit()
        return res.fetchall()

    def update(self, id_, results1):
        self.cur.execute("UPDATE results RESULTS = '{}' WHERE ID = '{}'".format(results1, id_))
        self.con.commit()

    def close(self):
        self.con.close()
