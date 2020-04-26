from BUZ.student import *
from tkinter import *
from BUZ.course import *
from BUZ.teacher import *
from tkinter.ttk import Combobox

# Menu Panel
masterPanel = Tk()
masterPanel.title('University panel:')
masterPanel.resizable(height=False, width=False)
w = 160  # width for the Tk root
h = 240  # height for the Tk root
# get screen width and height
ws = masterPanel.winfo_screenwidth()  # width of the screen
hs = masterPanel.winfo_screenheight()  # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
# set the dimensions of the screen
# and where it is placed
masterPanel.geometry('%dx%d+%d+%d' % (w, h, x, y))
menuFrame = Frame(masterPanel, bd=5, bg='Red')
menuFrame.grid(row=0, column=0)

def show_std_pnl():
    def saveStudent():
        p = student(int(Se1.get()), Se2.get(), Se3.get())
        result = p.insert()
        if result == 'True':
            messagebox.showinfo('Alert', 'ثبت اطلاعات دانشجو با موفقیت انجام شد.')
            Se1.delete(0, END)
            Se2.delete(0, END)
            Se3.delete(0, END)
            loadStudent()
        else:
            messagebox.showinfo('Alert', 'در ثبت اطلاعات دانشجو خطایی رخ داده است. (' + result + ')')

    def loadStudent():
        mySlist.delete(0, 'end')
        L = student.selectstudent()
        L2 = []
        for i in L:
            sid = int(i[0])
            sfname = i[1]
            slname = i[2]
            s = student(sid, sfname, slname)
            L2.append(s)

        scrollbarS.pack(side=RIGHT, fill=Y)
        for i in L2:
            mySlist.insert(END, i.show())
        mySlist.pack(side=LEFT, fill=BOTH)
        scrollbarS.config(command=mySlist.yview)

    def deleteStudent():
        x = mySlist.get(ANCHOR)
        s = student(x[0], x[1], x[2])
        s.delete()
        loadStudent()

    # Student Panel
    StudentPanel = Tk()
    StudentPanel.title('Students panel:')
    StudentPanel.resizable(height=False, width=False)
    StudentPanel.geometry('260x340')
    stdFrameU = Frame(StudentPanel, bd=5, bg="#E8E8E8")
    stdFrameU.pack(side=TOP)
    stdFrameD = Frame(StudentPanel, bd=5, bg='Blue')
    stdFrameD.pack(side=BOTTOM)
    w = 260  # width for the Tk root
    h = 340  # height for the Tk root
    # get screen width and height
    ws = StudentPanel.winfo_screenwidth()  # width of the screen
    hs = StudentPanel.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = ((ws / 2) - (w / 2)) - 211
    y = ((hs / 2) - (h / 2)) + 50
    # set the dimensions of the screen
    # and where it is placed
    StudentPanel.geometry('%dx%d+%d+%d' % (w, h, x, y))
    ############################
    Label(stdFrameU, text=':شناسه دانشجو').grid(row=0, column=1)
    Label(stdFrameU, text=':نام دانشجو').grid(row=1, column=1)
    Label(stdFrameU, text=':نام خانوادگی دانشجو').grid(row=2, column=1)
    Se1 = Entry(stdFrameU)
    Se1.grid(row=0, column=0)
    Se2 = Entry(stdFrameU)
    Se2.grid(row=1, column=0)
    Se3 = Entry(stdFrameU)
    Se3.grid(row=2, column=0)
    Bs = Button(stdFrameU, text='ذخیره', width=15, command=saveStudent).grid(row=4, column=1)
    Bl = Button(stdFrameU, text='بازیابی اطلاعات', width=15, command=loadStudent).grid(row=5, column=1)
    # BC = Button(stdFrameU, text='انصراف', width=15, command=close_current_window).grid(row=6, column=1)
    Bs2 = Button(stdFrameU, text='حذف دانشجو', width=15, command=deleteStudent)
    Bs2.grid(row=4, column=0)
    frame3 = Frame(stdFrameD)
    frame3.grid(row=5, column=1)
    scrollbarS = Scrollbar(frame3)#(frame1)
    mySlist = Listbox(frame3, yscrollcommand=scrollbarS.set)
    L = []

    loadStudent()

def show_tch_pnl():

    def saveTeacher():
        c = teacher(int(Te1.get()), Te2.get(), Te3.get())
        result = c.insert()
        if result == 'True':
            messagebox.showinfo('Alert', 'ثبت اطلاعات استاد با موفقیت انجام شد.')
            Te1.delete(0, END)
            Te2.delete(0, END)
            Te3.delete(0, END)
            loadTeacher()
        else:
            messagebox.showinfo('Alert', 'در ثبت اطلاعات استاد خطایی رخ داده است. (' + result + ')')

    def loadTeacher():
        myTlist.delete(0, 'end')
        L = teacher.selectteacher()
        L2 = []
        for i in L:
            tid = int(i[0])
            tfname = i[1]
            tlname = i[2]
            s = teacher(tid, tfname, tlname)
            L2.append(s)

        scrollbarT.pack(side=RIGHT, fill=Y)
        for i in L2:
            myTlist.insert(END, i.show())
        myTlist.pack(side=LEFT, fill=BOTH)
        scrollbarT.config(command=myTlist.yview)

    def deleteTeacher():
        x = myTlist.get(ANCHOR)
        t = teacher(x[0], x[1], x[2])
        t.delete()
        loadTeacher()

    # Teachers Panel
    TeacherPanel = Tk()
    TeacherPanel.title('Teachers panel:')
    TeacherPanel.resizable(height=False, width=False)
    TeacherPanel.geometry('260x240')
    tchFrameU = Frame(TeacherPanel, bd=5, bg="#E8E8E8")
    tchFrameU.pack(side=TOP)
    tchFrameD = Frame(TeacherPanel, bd=5, bg='Blue')
    tchFrameD.pack(side=BOTTOM)
    w = 260  # width for the Tk root
    h = 340  # height for the Tk root
    # get screen width and height
    ws = TeacherPanel.winfo_screenwidth()  # width of the screen
    hs = TeacherPanel.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = ((ws / 2) - (w / 2)) - 211
    y = ((hs / 2) - (h / 2)) + 50
    # set the dimensions of the screen
    # and where it is placed
    TeacherPanel.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # Label(panelFrame, text='-------ثبت اطلاعات اساتید-------').grid(row=0, column=1)
    Label(tchFrameU, text='شناسه استاد:').grid(row=1, column=1)
    Te1 = Entry(tchFrameU)
    Te1.grid(row=1, column=0)
    Label(tchFrameU, text='نام استاد:').grid(row=2, column=1)
    Te2 = Entry(tchFrameU)
    Te2.grid(row=2, column=0)
    Label(tchFrameU, text='نام خانوادگی استاد:').grid(row=3, column=1)
    Te3 = Entry(tchFrameU)
    Te3.grid(row=3, column=0)
    Bs2 = Button(tchFrameU, text='ذخیره', width=15, command=saveTeacher).grid(row=4, column=1)
    Bl2 = Button(tchFrameU, text='بازیابی اطلاعات', width=15, command=loadTeacher).grid(row=4, column=0)
    Bs2 = Button(tchFrameU, text='حذف', width=15, command=deleteTeacher).grid(row=5, column=1)

    frame3 = Frame(tchFrameD)
    frame3.grid(row=6, column=1)
    scrollbarT = Scrollbar(frame3)
    myTlist = Listbox(frame3, yscrollcommand=scrollbarT.set)
    L = []

    loadTeacher()

def show_crs_pnl():

    def saveCourse():
        p = course(int(Ce1.get()), Ce2.get(), int(Ce3.get()))
        result = p.insert()
        if result == 'True':
            messagebox.showinfo('Alert', 'ثبت اطلاعات درس با موفقیت انجام شد.')
            Ce1.delete(0, END)
            Ce2.delete(0, END)
            Ce3.delete(0, END)
            loadCourse()
        else:
            messagebox.showinfo('Alert', 'در ثبت اطلاعات درس خطایی رخ داده است. (' + result + ')')

    def loadCourse():
        myClist.delete(0, 'end')
        L = course.selectcrs()
        L2 = []
        for i in L:
            cid = int(i[0])
            cname = i[1]
            cunit = i[2]
            s = course(cid, cname, cunit)
            L2.append(s)

        scrollbarC.pack(side=RIGHT, fill=Y)
        for i in L2:
            myClist.insert(END, i.show())
        myClist.pack(side=LEFT, fill=BOTH)
        scrollbarC.config(command=myClist.yview)

    def deleteCourse():
        x = myClist.get(ANCHOR)
        c = course(x[0], x[1], x[2])
        c.delete()
        loadCourse()

    # Courses Panel
    CoursePanel = Tk()
    CoursePanel.title('Courses panel:')
    CoursePanel.resizable(height=False, width=False)
    CoursePanel.geometry('260x240')
    crsFrameU = Frame(CoursePanel, bd=5, bg="#E8E8E8")
    crsFrameU.pack(side=TOP)
    crsFrameD = Frame(CoursePanel, bd=5, bg='Blue')
    crsFrameD.pack(side=BOTTOM)
    w = 260  # width for the Tk root
    h = 340  # height for the Tk root
    # get screen width and height
    ws = CoursePanel.winfo_screenwidth()  # width of the screen
    hs = CoursePanel.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = ((ws / 2) - (w / 2)) - 211
    y = ((hs / 2) - (h / 2)) + 50
    # set the dimensions of the screen
    # and where it is placed
    CoursePanel.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # Label(panelFrame, text='-------ثبت اطلاعات دروس-------').grid(row=0, column=1)
    Label(crsFrameU, text='شناسه درس:').grid(row=1, column=1)
    Ce1 = Entry(crsFrameU)
    Ce1.grid(row=1, column=0)
    Label(crsFrameU, text='عنوان درس:').grid(row=2, column=1)
    Ce2 = Entry(crsFrameU)
    Ce2.grid(row=2, column=0)
    Label(crsFrameU, text='تعداد واحد:').grid(row=3, column=1)
    Ce3 = Entry(crsFrameU)
    Ce3.grid(row=3, column=0)
    BC = Button(crsFrameU, text='ذخیره', width=15, command=saveCourse).grid(row=5, column=1)
    # CPB_cancel = Button(crsFrameU, text='انصراف', width=15, command=close_current_window).grid(row=4, column=0)
    Bcl = Button(crsFrameU, text='بازیابی اطلاعات', width=15, command=loadCourse).grid(row=5, column=0)
    Bc2 = Button(crsFrameU, text='حذف', width=15, command=deleteCourse).grid(row=6, column=0)
    ########################
    frame3 = Frame(crsFrameD)
    frame3.grid(row=5, column=1)
    scrollbarC = Scrollbar(frame3)
    myClist = Listbox(frame3, yscrollcommand=scrollbarC.set)
    L = []
    loadCourse()

def show_crs_tch_pnl():

    ComboCrsVals = []
    ComboTchVals = []

    def get_crs_vals():
        L = course.selectcrs()
        LC = []
        for i in L:
            cid = int(i[0])
            cname = i[1]
            cunit = i[2]
            s = course(cid, cname, cunit)
            LC.append(cname)
            ComboCrsVals.append([cid,cname, cunit])
        return LC

    def get_tch_vals():
        L = teacher.selectteacher()
        LT = []
        for i in L:
            tid = int(i[0])
            tfname = i[1]
            tlname = i[2]
            t = teacher(tid, tfname, tlname)
            LT.append(tfname + ' ' + tlname)
            ComboTchVals.append([tid, tfname, tlname])
        return LT

    def loadAssignments():
        myTCTlist.delete(0, 'end')
        L = teacher.loadTchCrs()
        L2 = []
        for i in L:
            cname = i[0]
            sep_char = i[1]
            tfnam = i[2]
            tlnam = i[3]
            L2.append(i)
        # print(L2)
        scrollbarTCT.pack(side=RIGHT, fill=Y)
        for i in L2:
            myTCTlist.insert(END, str(i))
        myTCTlist.pack(side=LEFT, fill=BOTH)
        scrollbarTCT.config(command=myTCTlist.yview)

    def assignCrsToTch():
        c = course(ComboCrsVals[int(ccb.current())][0],ComboCrsVals[int(ccb.current())][1],ComboCrsVals[int(ccb.current())][2])
        t = teacher(ComboTchVals[int(tcb.current())][0],ComboTchVals[int(tcb.current())][1],ComboTchVals[int(tcb.current())][2])
        t.take_crs(c)
        loadAssignments()

    def unassignCrsToTch():
        c = course(ComboCrsVals[int(ccb.current())][0], ComboCrsVals[int(ccb.current())][1],
                   ComboCrsVals[int(ccb.current())][2])
        t = teacher(ComboTchVals[int(tcb.current())][0], ComboTchVals[int(tcb.current())][1],
                    ComboTchVals[int(tcb.current())][2])
        t.take_back_crs(c)
        loadAssignments()

    # Courses_Teachers Panel
    CourseTeacherPanel = Tk()
    CourseTeacherPanel.title('Courses Teacher panel:')
    CourseTeacherPanel.resizable(height=False, width=False)
    CourseTeacherPanel.geometry('460x440')
    # crsFrame = Frame(CourseTeacherPanel, bd=5, bg='Red').grid(row=0, column=0)

    crstchFrameB = Frame(CourseTeacherPanel, bd=5, bg='Red')
    crstchFrameB.pack(side=BOTTOM)
    crstchFrameT = Frame(CourseTeacherPanel, bd=5, bg="#a85f50")
    crstchFrameT.pack(side=TOP)
    crstchFrameR = Frame(crstchFrameT, bd=5, bg="#eab3a7")
    crstchFrameR.pack(side=RIGHT)
    crstchFrameL = Frame(crstchFrameT, bd=5, bg="#ae877f")
    crstchFrameL.pack(side=LEFT)
    w = 360  # width for the Tk root
    h = 340  # height for the Tk root
    # get screen width and height
    ws = CourseTeacherPanel.winfo_screenwidth()  # width of the screen
    hs = CourseTeacherPanel.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = ((ws / 2) - (w / 2)) - 262
    y = ((hs / 2) - (h / 2)) + 50
    # set the dimensions of the screen
    # and where it is placed
    CourseTeacherPanel.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Assign Course To Teacher-------------------
    Label(crstchFrameR, text='انتخاب درس مورد نظر').grid(row=0, column=0)

    crs_var = StringVar()
    crs_var.set("")
    cdata = get_crs_vals()
    ccb = Combobox(crstchFrameR, values=cdata)
    ccb.grid(row=1, column=0)

    Label(crstchFrameL, text='انتخاب استاد مورد نظر').grid(row=0, column=1)

    tch_var = StringVar()
    tch_var.set("")
    tdata = get_tch_vals()
    tcb = Combobox(crstchFrameL, values=tdata)
    tcb.grid(row=1, column=1)
    BCT1 = Button(crstchFrameR, text='تخصیص درس به استاد',width=20, command=assignCrsToTch).grid(row=2, column=0)
    BCT2 = Button(crstchFrameL, text='حذف تخصیص درس به استاد',width=20, command=unassignCrsToTch).grid(row=2, column=1)

    frame32 = Frame(crstchFrameB)
    frame32.grid(row=3, column=1)
    scrollbarTCT = Scrollbar(frame32)
    myTCTlist = Listbox(frame32, yscrollcommand=scrollbarTCT.set)

    loadAssignments()

def show_std_crs_tch_pnl():
    ComboCrVals = []
    ComboTchVals = []
    ComboStdVals = []
    selected_crs_id = 0
    selected_crs_name = ''
    selected_std_id = 0
    selected_std_fnam = ''
    selected_std_lnam = ''
    selected_tch_id = 0
    selected_tch_fnam = ''
    selected_tch_lnam = ''
    tcb = Combobox()
    scb = Combobox()
    ccb = Combobox()

    def get_crs_vals():
        L = course.selectcrs()
        LC = []
        for i in L:
            cid = int(i[0])
            cname = i[1]
            cunit = i[2]
            c = course(cid, cname, cunit)
            LC.append(cname)
            ComboCrVals.append([cid, cname, cunit])
        return LC

    def get_tch_vals():
        global selected_crs_id
        # print('selected_crs_id::::',selected_crs_id,ComboCrVals[int(ccb.current())][0])
        L = teacher.loadTchCrsId(selected_crs_id) #ComboCrsVals[int(ccb.current())][0]) #selectteacher()
        LT = []
        for i in L:
            tid = int(i[0])
            tfname = i[1]
            tlname = i[2]
            t = teacher(tid, tfname, tlname)
            LT.append(tfname + ' ' + tlname)
            ComboTchVals.append([tid, tfname, tlname])
        return LT

    def get_std_vals():
        L = student.selectstudent()
        LS = []
        for i in L:
            sid = int(i[0])
            sfname = i[1]
            slname = i[2]
            s = student(sid, sfname, slname)
            LS.append(sfname + ' ' + slname)
            ComboStdVals.append([sid, sfname, slname])
        return LS

    def loadAssignments():
        mySTClist.delete(0, 'end')
        L = student.loadStdTchCrs()
        L2 = []
        for i in L:
            sfname = i[0]
            slname = i[1]
            cname = i[2]
            sep_char = i[3]
            tfnam = i[4]
            tlnam = i[5]
            L2.append(i)

        # print(L2)
        scrollbarSTC.pack(side=RIGHT, fill=Y)
        for i in L2:
            mySTClist.insert(END, str(i))
        mySTClist.pack(side=LEFT, fill=BOTH)
        scrollbarSTC.config(command=mySTClist.yview)

    def assignCrsTchToStd():
        c = course(ComboCrVals[int(ccb.current())][0], ComboCrVals[int(ccb.current())][1],
                   ComboCrVals[int(ccb.current())][2])
        t = teacher(ComboTchVals[int(tcb.current())][0], ComboTchVals[int(tcb.current())][1],
                    ComboTchVals[int(tcb.current())][2])
        s = student(ComboStdVals[int(scb.current())][0], ComboStdVals[int(scb.current())][1],
                   ComboStdVals[int(scb.current())][2])
        s.take_crs_tch(c,t)
        loadAssignments()

    def unassignCrsTchToStd():
        c = course(ComboCrVals[int(ccb.current())][0], ComboCrVals[int(ccb.current())][1],
                   ComboCrVals[int(ccb.current())][2])
        t = teacher(ComboTchVals[int(tcb.current())][0], ComboTchVals[int(tcb.current())][1],
                    ComboTchVals[int(tcb.current())][2])
        s = student(ComboStdVals[int(scb.current())][0], ComboStdVals[int(scb.current())][1],
                    ComboStdVals[int(scb.current())][2])
        s.remove_crs_tch(c,t)
        loadAssignments()


    def show_tch_cnt():
        global selected_tch_id
        global selected_tch_fnam
        global selected_tch_lnam

        selected_tch_id = ComboTchVals[int(tcb.current())][0]
        selected_tch_fnam = ComboTchVals[int(tcb.current())][1]
        selected_tch_lnam = ComboTchVals[int(tcb.current())][2]

        # print('1::::::::', selected_tch_id, selected_tch_fnam, selected_tch_lnam)
        # print('tcb.get===> ', tcb.get())
        Button(stdcrstchFrameB, text='اضافه', command=assignCrsTchToStd).grid(row=0, column=0)
        Button(stdcrstchFrameB, text='حذف', command=unassignCrsTchToStd).grid(row=2, column=0)

    def show_crs_cnt_items():
        global selected_crs_id
        global selected_crs_name
        # global selected_tch_id
        # global selected_tch_fnam
        # global selected_tch_lnam
        selected_crs_id = ComboCrVals[int(ccb.current())][0]
        selected_crs_name = ComboCrVals[ccb.current()][1]
        # print('2::::::::', selected_crs_id, selected_crs_name,ComboCrVals[int(ccb.current())][0], ComboCrVals[ccb.current()][1])
        # print('ccb.get===> ', ccb.get())
        # print('************',ccb.current())
        Label(stdcrstchFrameL, text='انتخاب استاد مورد نظر').grid(row=0, column=0)

        tch_var = StringVar()
        tch_var.set("")
        tdata = get_tch_vals()
        tcb = Combobox(stdcrstchFrameL, values=tdata)
        tcb.grid(row=1, column=0)
        Button(stdcrstchFrameL, text='ادامه', command=show_tch_cnt).grid(row=2, column=0)

    def show_std_cnt_items():
        global selected_std_id
        global selected_std_fnam
        global selected_std_lnam

        Label(stdcrstchFrameM, text='انتخاب درس مورد نظر').grid(row=0, column=0)

        # crs_var = StringVar()
        # crs_var.set("")
        # cdata = get_crs_vals()
        ccb = Combobox(stdcrstchFrameM, values=cdata)
        ccb.grid(row=1, column=0)
        Button(stdcrstchFrameM, text='ادامه', command=show_crs_cnt_items).grid(row=2, column=0)
        selected_std_id = ComboStdVals[int(scb.current())][0]
        selected_std_fnam = ComboStdVals[int(scb.current())][1]
        selected_std_lnam = ComboStdVals[int(scb.current())][2]

        # print('1::::::::', selected_std_id, selected_std_fnam, selected_std_lnam)
        selected_crs_id = ComboCrVals[int(ccb.current())][0]
        selected_crs_name = ComboCrVals[ccb.current()][1]

        # print('3::::::::', selected_crs_id, selected_crs_name)

    # Courses_Teachers Panel
    StdCourseTeacherPanel = Tk()
    StdCourseTeacherPanel.title('Student  Courses Teacher panel:')
    StdCourseTeacherPanel.resizable(height=False, width=False)
    StdCourseTeacherPanel.geometry('460x440')

    stdcrstchFrameB = Frame(StdCourseTeacherPanel, bd=5, bg='Blue')
    stdcrstchFrameB.pack(side=BOTTOM)
    stdcrstchFrameT = Frame(StdCourseTeacherPanel, bd=5, bg='Blue')
    stdcrstchFrameT.pack(side=TOP)
    stdcrstchFrameR = Frame(stdcrstchFrameT, bd=5, bg="#e8e8e8")
    stdcrstchFrameR.pack(side=RIGHT)
    stdcrstchFrameL = Frame(stdcrstchFrameT, bd=5, bg="#e8e8e8")
    stdcrstchFrameL.pack(side=LEFT)
    stdcrstchFrameM = Frame(stdcrstchFrameT, bd=5, bg='Blue')
    stdcrstchFrameM.pack(side=LEFT)
    w =480  # width for the Tk root
    h = 360  # height for the Tk root
    # get screen width and height
    ws = StdCourseTeacherPanel.winfo_screenwidth()  # width of the screen
    hs = StdCourseTeacherPanel.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = ((ws / 2) - (w / 2)) - 321
    y = ((hs / 2) - (h / 2)) + 60
    # set the dimensions of the screen
    # and where it is placed
    StdCourseTeacherPanel.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Label(stdcrstchFrameR, text='انتخاب دانشجوی مورد نظر').grid(row=0, column=2)

    std_var = StringVar()
    std_var.set("")
    sdata = get_std_vals()
    scb = Combobox(stdcrstchFrameR, values=sdata)
    scb.grid(row=1, column=2)

    crs_var = StringVar()
    crs_var.set("")
    cdata = get_crs_vals()
    # ccb = Combobox(stdcrstchFrameM, values=cdata)
    # ccb.grid(row=1, column=0)

    Button(stdcrstchFrameR, text='ادامه', command=show_std_cnt_items).grid(row=2, column=2)

    frame32 = Frame(stdcrstchFrameB)
    frame32.grid(row=1, column=0)
    scrollbarSTC = Scrollbar(frame32)
    mySTClist = Listbox(frame32, yscrollcommand=scrollbarSTC.set)

    loadAssignments()

def show_mrk_pnl():
    ComboTchVals = []
    ComboStdVals = []
    selected_crs_id = 0
    selected_crs_name = ''
    selected_std_id = 0
    selected_std_fnam = ''
    selected_std_lnam = ''
    selected_tch_id = 0
    selected_tch_fnam = ''
    selected_tch_lnam = ''
    tcb = Combobox()
    scb = Combobox()

    def save_std_mrk():
        global selected_crs_id
        global selected_tch_id
        global selected_std_id

        # print(selected_crs_id,selected_tch_id ,selected_std_id)
        course.set_mark(selected_std_id,selected_crs_id,selected_tch_id ,entr_mrktrm.get() ,float(entr_mrkno.get()))

    def get_tch_vals():
        L = teacher.loadTchCrsId(entr_crsid.get())
        LT = []
        for i in L:
            tid = int(i[0])
            tfname = i[1]
            tlname = i[2]
            t = teacher(tid, tfname, tlname)
            LT.append(tfname + ' ' + tlname)
            ComboTchVals.append([tid, tfname, tlname])
        return LT

    def set_std_mrk():
        global selected_crs_id
        global selected_crs_name
        global selected_std_id
        global selected_std_fnam
        global selected_std_lnam
        global selected_tch_id
        global selected_tch_fnam
        global selected_tch_lnam

        Label(mrkFrameM, text='---ثبت نمرات دانشجویان--').grid(row=5)
        Label(mrkFrameM, text=':نام درس').grid(row=6, column=0)
        Label(mrkFrameM, text=selected_crs_name).grid(row=6, column=1)
        Label(mrkFrameM, text='استاد درس:').grid(row=7, column=0)
        Label(mrkFrameM, text=selected_tch_fnam + ' ' + selected_tch_lnam).grid(row=7, column=1)
        Label(mrkFrameM, text='نام و نام خانوادگی دانشجوی انتخاب شده:').grid(row=8, column=0)
        Label(mrkFrameM, text=selected_std_fnam + ' ' + selected_std_lnam).grid(row=8, column=1)
        Label(mrkFrameM, text='نیمسال تحصیلی').grid(row=9, column=0)
        entr_mrktrm.grid(row=9, column=1)
        Label(mrkFrameM, text='نمره').grid(row=10, column=0)
        entr_mrkno.grid(row=10, column=1)

        btn = Button(mrkFrameM, text='ذخیره', width=15, command=save_std_mrk)
        btn.grid(row=11, column=1)

    def find_crs_info():
        global selected_crs_id
        global selected_crs_name
        global selected_tch_id
        global selected_tch_fnam
        global selected_tch_lnam
        c = course.selectCrsById(int(entr_crsid.get()))
        LC = list(c)
        selected_crs_id = entr_crsid.get()
        selected_crs_name = LC[0][1]
        Label(mrkFrameM, text=':نام درس').grid(row=0, column=1)
        Label(mrkFrameM, text=LC[0][1]).grid(row=0, column=0)

        Label(mrkFrameM, text='اساتید درس:').grid(row=2, column=1)
        tch_var = StringVar()
        tch_var.set("")
        tdata = get_tch_vals()
        tcb = Combobox(mrkFrameM, values=tdata)
        tcb.grid(row=2, column=0)

        selected_tch_id = ComboTchVals[int(tcb.current())][0]
        selected_tch_fnam = ComboTchVals[int(tcb.current())][1]
        selected_tch_lnam = ComboTchVals[int(tcb.current())][2]

        Button(mrkFrameM, text='نمایش دانشجویان', width=15, command=find_std_info).grid(row=2, column=2)

    def find_std_info():
        global selected_std_id
        global selected_std_fnam
        global selected_std_lnam
        L = student.loadStdOfCrsTch_ByCidTid(entr_crsid.get(), ComboTchVals[int(tcb.current())][0])
        LS = []
        for i in L:
            sid = int(i[0])
            sfname = i[1]
            slname = i[2]
            s = student(sid, sfname, slname)
            LS.append(sfname + ' ' + slname)
            ComboStdVals.append([sid, sfname, slname])
        # return LS

        Label(mrkFrameM, text='دانشجویان درس:').grid(row=3, column=1)
        std_var = StringVar()
        std_var.set("")
        sdata = LS #get_std_vals()
        scb = Combobox(mrkFrameM, values=sdata)
        scb.grid(row=3, column=0)

        selected_std_id = ComboStdVals[int(scb.current())][0]
        selected_std_fnam = ComboStdVals[scb.current()][1]
        selected_std_lnam = ComboStdVals[scb.current()][2]

        Button(mrkFrameM, text='ثبت نمره', width=15, command=set_std_mrk).grid(row=4, column=2)


    # Marks Panel
    MarkPanel = Tk()
    MarkPanel.title('Marks panel:')
    MarkPanel.resizable(height=False, width=False)
    MarkPanel.geometry('260x240')
    # mrkFrame = Frame(MarkPanel, bd=5, bg='Red').grid(row=0, column=0)
    w = 460  # width for the Tk root
    h = 440  # height for the Tk root
    # get screen width and height
    ws = MarkPanel.winfo_screenwidth()  # width of the screen
    hs = MarkPanel.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = ((ws / 2) - (w / 2)) - 311
    y = ((hs / 2) - (h / 2)) + 100
    # set the dimensions of the screen
    # and where it is placed
    MarkPanel.geometry('%dx%d+%d+%d' % (w, h, x, y))

    mrkFrameT = Frame(MarkPanel, bd=5, bg="blue")
    mrkFrameT.pack(side=TOP)
    mrkFrameM = Frame(MarkPanel, bd=5, bg="#e8e8e8")
    mrkFrameM.pack(side=TOP)
    stdFrameB = Frame(MarkPanel, bd=5, bg='Green')
    stdFrameB.pack(side=TOP)

    Label(mrkFrameT, text=':شناسه درس').grid(row=0, column=1)
    entr_crsid = Entry(mrkFrameT)
    entr_crsid.grid(row=0, column=0)
    Button(mrkFrameT, text='جستجو', width=20, command=find_crs_info).grid(row=1, column=0)

    frame3 = Frame(mrkFrameM)
    frame3.grid(row=3, column=2)
    scrollbarct = Scrollbar(frame3)
    myctlist = Listbox(frame3, yscrollcommand=scrollbarct.set)
    entr_mrktrm = Entry(mrkFrameM)
    entr_mrkno = Entry(mrkFrameM)

def show_rep_pnl():
    def gen_tch_rep():
        L = teacher.selectteacher()
        Tfile = open('..\Reports\ListOfTeachers.txt', 'w', encoding='utf-8')
        Tfile.write('---------فهرست اساتید دانشگاه---------\n')
        Tfile.write('شناسه' + "\t\t" + 'نام' + "\t\t" + 'نام خانوادگی' + "\t\t"  + "\n")
        for i in L:
            Tfile.write(str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\t" + "\n")
        Tfile.close()
        messagebox.showinfo('Alert','گزارش در مسیر پروژه در دایرکتوری Reports با نام ListOfTeachers ذخیره شد.')

    def gen_std_rep():
        L = student.selectstudent()
        Tfile = open('..\Reports\ListOfStudents.txt', 'w', encoding='utf-8')
        Tfile.write('---------فهرست دانشجویان---------\n')
        Tfile.write('شناسه' + "\t\t" + 'نام' + "\t\t" + 'نام خانوادگی' + "\t\t" + "\n")
        for i in L:
            Tfile.write(str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\t" + "\n")
        Tfile.close()
        messagebox.showinfo('Alert', 'گزارش در مسیر پروژه در دایرکتوری Reports با نام ListOfStudents ذخیره شد.')

    def gen_crs_rep():
        L = course.selectcrs()
        Tfile = open('..\Reports\ListOfCourses.txt', 'w', encoding='utf-8')
        Tfile.write('---------فهرست دروس تعریف شده---------\n')
        Tfile.write('شناسه' + "\t\t" + 'نام درس' + "\t\t" + 'تعداد واحد' + "\t\t" + "\n")
        for i in L:
            Tfile.write(str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\t" + "\n")
        Tfile.close()
        messagebox.showinfo('Alert', 'گزارش در مسیر پروژه در دایرکتوری Reports با نام ListOfCourses ذخیره شد.')

    def gen_crs_std_rep():
        L = student.loadStdTchCrs_rep()
        Tfile = open('..\Reports\CoursesOfStudents.txt', 'w', encoding='utf-8')
        Tfile.write('--------- فهرست دروس اخذ شده توسط هر دانشجو ---------\n')
        Tfile.write('شماره دانشجویی' + "\t\t" + 'نام و نام خانوادگی دانشجو' + "\t\t" + 'شناسه درس' + "\t\t"
                    + 'نام درس'+ "\t\t" + 'شناسه استاد درس' + "\t\t" + 'نام و نام خانوادگی استاد' + "\n")
        for i in L:
            Tfile.write(str(i[0]) + "\t\t" + str(i[1])+" "+str(i[2]) + "\t\t" + str(i[3])+ "\t\t" + str(i[4]) + "\t\t"+ str(i[5]) + "\t\t"+ str(i[6]) + " " + str(i[7])+ "\n")
        Tfile.close()
        messagebox.showinfo('Alert', 'گزارش در مسیر پروژه در دایرکتوری Reports با نام CoursesOfStudents ذخیره شد.')

    def gen_std_avg_rep():
        L = student.loadStdAvg()
        Tfile = open('..\Reports\AvgOfStudents.txt', 'w', encoding='utf-8')
        Tfile.write('--------- معدل دانشجویان ---------\n')
        Tfile.write('شماره دانشجویی' + "\t\t" + 'نام و نام خانوادگی دانشجو' + "\t\t" + 'معدل' + "\n")
        for i in L:
            Tfile.write(str(i[0]) + "\t\t" + str(i[1]) + " " + str(i[2]) + "\t\t" + str(round(i[3],2)) + "\n")
        Tfile.close()
        messagebox.showinfo('Alert', 'گزارش در مسیر پروژه در دایرکتوری Reports با نام AvgOfStudents ذخیره شد.')

    def gen_tch_crs_rep():
        L = teacher.loadTchCrs_rep()
        Tfile = open('..\Reports\CoursesOfTeachers.txt', 'w', encoding='utf-8')
        Tfile.write('--------- فهرست دروس اخذ شده توسط اساتید ---------\n')
        Tfile.write('شناسه درس' + "\t\t" + 'نام درس' + "\t\t" + 'شناسه استاد درس' + "\t\t" + 'نام و نام خانوادگی استاد' + "\n")
        for i in L:
            Tfile.write(str(i[0]) + "\t\t" + str(i[1]) + "\t\t" + str(i[2]) + "\t\t" + str(i[3]) + " " + str(i[4]) + "\n")
        Tfile.close()
        messagebox.showinfo('Alert', 'گزارش در مسیر پروژه در دایرکتوری Reports با نام CoursesOfTeachers ذخیره شد.')

    # Reports Panel
    ReportPanel = Tk()
    ReportPanel.title('Reports panel:')
    ReportPanel.resizable(height=False, width=False)
    ReportPanel.geometry('260x240')
    # repFrame = Frame(ReportPanel, bd=5, bg='Red').grid(row=0, column=0)
    w = 300  # width for the Tk root
    h = 200  # height for the Tk root
    # get screen width and height
    ws = ReportPanel.winfo_screenwidth()  # width of the screen
    hs = ReportPanel.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = ((ws / 2) - (w / 2)) - 232
    y = ((hs / 2) - (h / 2)) - 20
    # set the dimensions of the screen
    # and where it is placed
    ReportPanel.geometry('%dx%d+%d+%d' % (w, h, x, y))

    repFrameT = Frame(ReportPanel, bd=5, bg='Yellow')
    repFrameT.pack(side=TOP)
    repFrameM = Frame(ReportPanel, bd=5, bg='Green')
    repFrameM.pack(side=TOP)
    repFrameB = Frame(ReportPanel, bd=5, bg='Blue')
    repFrameB.pack(side=TOP)

    Button(repFrameM, text='فهرست اساتید', width=30, command=gen_tch_rep).grid(row=0, column=0)
    Button(repFrameM, text='فهرست دانشجویان', width=30, command=gen_std_rep).grid(row=1, column=0)
    Button(repFrameM, text='فهرست دروس', width=30, command=gen_crs_rep).grid(row=2, column=0)
    Button(repFrameM, text='فهرست دروس انتخابی دانشجویان', width=30, command=gen_crs_std_rep).grid(row=3, column=0)
    Button(repFrameM, text='فهرست معدل دانشجویان', width=30, command=gen_std_avg_rep).grid(row=4, column=0)
    Button(repFrameM, text='فهرست دروس هر استاد', width=30, command=gen_tch_crs_rep).grid(row=5, column=0)


# menu frame
Label(menuFrame, text='-------انتخاب عملیات-------').grid(row=0,column=0)
MB_STD = Button(menuFrame, text='ثبت دانشجو', width=20, command=show_std_pnl).grid(row=0,column=0)
MB_TCH = Button(menuFrame, text='ثبت اساتید', width=20, command=show_tch_pnl).grid(row=1,column=0)
MB_CRS = Button(menuFrame, text='ثبت دروس', width=20, command=show_crs_pnl).grid(row=2,column=0)
MB_CRS_TCH = Button(menuFrame, text='ثبت اساتید دروس', width=20, command=show_crs_tch_pnl).grid(row=3,column=0)
MB_STD_CRS_TCH = Button(menuFrame, text='حذف و اضافه', width=20, command=show_std_crs_tch_pnl).grid(row=4,column=0)
MB_MRK = Button(menuFrame, text='ثبت نمرات', width=20, command=show_mrk_pnl).grid(row=5,column=0)
MB_REP = Button(menuFrame, text='گزارش گیری', width=20, command=show_rep_pnl).grid(row=6,column=0)


mainloop()
