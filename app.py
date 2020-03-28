from flask import Flask, render_template, request
from datetime import datetime
import re
import calendar

from ext_app import app
from exts import db

from models import Room_108, Name_List, Success_Record

date_regex = re.compile(r'^\d{4}-\d{2}-\d{2}$')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        all_rec = Success_Record.query.all()
        right_date_list = []
        date_str = request.form['date'] if 'date' in request.form else None
        course_select = request.form['course'] if 'course' in request.form else None
        week_day_name = None
        #
        if date_str != '' and date_regex.match(date_str):
            print(date_str)
            date = datetime.strptime(date_str, '%Y-%m-%d')
            week_day_name = calendar.day_name[date.weekday()]
            weekday = date.weekday()+1 # 1 = monday ... 7 = sunday

            course_list = Room_108.query.filter_by(Week=weekday).all()
            course_list.sort()
            # for option "other"
            other = Room_108()
            other.id = -1
            other.Class_Name = '其他'
            course_list.append(other)
        print('>> ', course_select, type(course_select))
        if course_select:
            course_select = int(course_select)
            # Search ones that matches date and add them to right_date_list
            if course_select != -1:
                ctime = Room_108.query.get(course_select).get_time(date)
                for i in all_rec:
                    i_dt = i.timest
                    if ctime[0] <= i_dt and i_dt <= ctime[1]:
                        right_date_list.append(i)
                right_date_list.sort()
            # TODO: refactor this shit speed O(n*m)
            else:
                time_pair_list = []
                for c in Room_108.query.all():
                    time_pair_list.append(c.get_time(date))
                for s in Success_Record.query.all():
                    check = 0
                    for start, end in time_pair_list:
                        if end < s.timest or s.timest < start:
                            check += 1
                    if check == len(time_pair_list):
                        right_date_list.append(s)
            
            name_list = Name_List.query.all()
            name_dict = {}
            for n in name_list:
                name_dict[n.uid] = n.namess

        return render_template('index.html',
            stu_list=right_date_list,
            name_dict=name_dict,
            #
            date_str=date_str,
            week_day_name=week_day_name,
            #
            course_list=course_list,
            course_select=course_select)

    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)