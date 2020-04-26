from Data.dbnmagement import *
dbm=dbmange('../Data/myDB.db')
dbm.create()
class teacher:
    def __init__(self,tid,tfname,tlname):
        self.tid=tid
        self.tfname=tfname
        self.tlname=tlname

    def show(self):
        return (self.tid,self.tfname,self.tlname)

    def insert(self):
        query='INSERT  INTO TEACHERS VALUES (?,?,?)'
        parameters=self.show()
        return dbm.insert(query,parameters)

    @staticmethod
    def selectteacher():
        query='SELECT * FROM TEACHERS'
        L=dbm.select(query)
        return L

    def delete(self):
        query = 'DELETE  FROM  TEACHERS WHERE TCH_ID =' + str(self.tid)
        dbm.delete(query)

    def take_crs(self, c):
        query = 'INSERT  INTO COURSES_TEACHERS VALUES (?,?)'
        parameters = (c.cid, self.tid)
        dbm.insert(query, parameters)
        # print(query + str(self.tid) + str(c.cid))

    def take_back_crs(self, c):
        # query = 'DELETE FROM COURSES_TEACHERS WHERE CRS_ID = ' + str(c.cid) + ' AND TCH_ID = ' + str(self.tid)
        query = 'DELETE FROM COURSES_TEACHERS WHERE CRS_ID = ' + str(c.cid) + ' AND TCH_ID = ' + str(self.tid)
        dbm.delete(query)
        # print(query + str(self.tid) + str(c.cid))

    @staticmethod
    def loadTchCrs():
        query='SELECT CRS_NAME,'+'":"'+',TCH_FNAME,TCH_LNAME FROM TEACHERS T,COURSES C WHERE C.CRS_ID||T.TCH_ID IN (SELECT CRS_ID||TCH_ID FROM COURSES_TEACHERS)'
        # print(query)
        L=dbm.select(query)
        return L

    @staticmethod
    def loadTchCrsId(crs_id):
        query = 'SELECT TCH_ID, TCH_FNAME , TCH_LNAME FROM TEACHERS T WHERE T.TCH_ID IN (SELECT TCH_ID FROM COURSES_TEACHERS WHERE CRS_ID = ' + str(crs_id) + ')'
        # print('*************')
        # print(query)
        # print('*************')
        L = dbm.select(query)
        return L

    @staticmethod
    def loadTchCrs_rep():
        query = 'SELECT CRS_ID,CRS_NAME,TCH_ID,TCH_FNAME,TCH_LNAME FROM TEACHERS T,COURSES C WHERE C.CRS_ID||T.TCH_ID IN (SELECT CRS_ID||TCH_ID FROM COURSES_TEACHERS)'
        # print(query)
        L = dbm.select(query)
        return L