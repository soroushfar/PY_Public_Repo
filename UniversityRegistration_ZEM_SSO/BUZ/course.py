from Data.dbnmagement import *
dbm=dbmange('../Data/myDB.db')
dbm.create()
class course:
    def __init__(self,cid,cname,cunit): #,ctid):
        self.cid=cid
        self.cname=cname
        self.cunit=cunit
        # self.ctid=ctid


    def show(self):
        return (self.cid, self.cname, self.cunit) #, self.ctid)

    def insert(self):
        query='INSERT  INTO COURSES VALUES (?,?,?)' #,?)'
        parameters=self.show()
        return dbm.insert(query,parameters)

    @staticmethod
    def selectcrs():
        query='SELECT * FROM COURSES'
        L=dbm.select(query)
        return L

    def delete(self):
        query = 'DELETE  FROM  COURSES WHERE CRS_ID ='+str(self.cid)
        dbm.delete(query)

    @staticmethod
    def selectCrsById(crs_id):
        query = 'SELECT * FROM COURSES WHERE CRS_ID = ' + str(crs_id)
        L = dbm.select(query)
        # L2 = list(L)
        # print(L)
        # print(L2[0][0])
        # print(L2[0][1])
        # print(L2[0][2])
        return L

    @staticmethod
    def selectTeachersOfCrsById(crs_id):
        query = 'SELECT * FROM TEACHERS T WHERE T.TCH_ID IN ' \
                '(SELECT TCH_ID FROM COURSES_TEACHERS CT ' \
                'WHERE CT.CRS_ID =  ' + str(crs_id) + ' )'
        L = dbm.select(query)
        return L

    @staticmethod
    def set_mark(std_id, crs_id, tch_id, term, mark):
        query = 'INSERT INTO MARKS (MRK_STD_ID, MRK_CRS_ID, MRK_TCH_ID, MRK_SEMESTER, MRK_NO) VALUES (?,?,?,?,?)'
        parameters = (std_id, crs_id, tch_id, term, mark)
        # print(query)
        # print(parameters)
        return dbm.insert(query,parameters)