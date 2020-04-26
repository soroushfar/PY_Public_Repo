from Data.dbnmagement import *
dbm=dbmange('../Data/myDB.db')
dbm.create()
class student:
    def __init__(self,sid,sfname,slname):
        self.sid=sid
        self.sfname=sfname
        self.slname=slname

    def show(self):
        return (self.sid,self.sfname,self.slname)

    def insert(self):
        query='INSERT  INTO STUDENTS VALUES (?,?,?)'
        parameters=self.show()
        return dbm.insert(query,parameters)

    @staticmethod
    def selectstudent():
        query='SELECT * FROM STUDENTS'
        L=dbm.select(query)
        return L

    def delete(self):
        query = 'DELETE  FROM  STUDENTS WHERE STD_ID ='+str(self.sid)
        # print('========================')
        # print(query)
        dbm.delete(query)

    def take_crs_tch(self, c,t):
        query = 'INSERT  INTO STUDENT_COURSES_TEACHERS VALUES (?,?,?)'
        parameters = (self.sid, c.cid, t.tid)
        dbm.insert(query, parameters)
        # print(query + str(self.sid)  + str(c.cid)+ str(t.tid))

    def remove_crs_tch(self, c,t):
        # query = 'DELETE FROM COURSES_TEACHERS WHERE CRS_ID = ' + str(c.cid) + ' AND TCH_ID = ' + str(self.tid)
        query = 'DELETE FROM STUDENT_COURSES_TEACHERS WHERE STD_ID = ' + str(self.sid) + ' AND  CRS_ID = ' + str(c.cid) + ' AND TCH_ID = ' + str(t.tid)
        dbm.delete(query)
        # print(query + str(self.sid) + str(c.cid) + str(t.tid))

    @staticmethod
    def loadStdTchCrs():
        query = 'SELECT STD_FNAME,STD_LNAME' + ',":"' + ',CRS_NAME,' + '":"' + ',TCH_FNAME,TCH_LNAME FROM TEACHERS T,COURSES C,STUDENTS S ' \
                                                                              'WHERE S.STD_ID||C.CRS_ID||T.TCH_ID IN ' \
                                             '(SELECT STD_ID||CRS_ID||TCH_ID FROM STUDENT_COURSES_TEACHERS)'
        # print(query)
        L = dbm.select(query)
        return L

    @staticmethod
    def loadStdOfCrsTch_ByCidTid(crs_id,tch_id):
        query = 'SELECT STD_ID,STD_FNAME,STD_LNAME FROM STUDENTS S WHERE S.STD_ID IN ' \
                '(SELECT STD_ID FROM STUDENT_COURSES_TEACHERS CT ' \
                'WHERE CT.CRS_ID =  ' + str(crs_id) + ' AND CT.TCH_ID =  ' + str(tch_id) + ' ) '
        L = dbm.select(query)
        return L

    @staticmethod
    def loadStdTchCrs_rep():
        query = 'SELECT STD_ID,STD_FNAME,STD_LNAME,CRS_ID,CRS_NAME,TCH_ID,TCH_FNAME,TCH_LNAME FROM TEACHERS T,COURSES C,STUDENTS S ' \
                                                                               'WHERE S.STD_ID||C.CRS_ID||T.TCH_ID IN ' \
                                                                               '(SELECT STD_ID||CRS_ID||TCH_ID FROM STUDENT_COURSES_TEACHERS)'
        # print(query)
        L = dbm.select(query)
        return L

    @staticmethod
    def loadStdAvg():
        query = 'select STD_ID, STD_FNAME, STD_LNAME, avg(MRK_NO) from MARKS, STUDENTS where MRK_STD_ID = STD_ID group by MRK_STD_ID'
        # print(query)
        L = dbm.select(query)
        return L
