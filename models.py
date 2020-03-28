from exts import db

class Room_108(db.Model):
    __tablename__ = '108_room'

    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True)
    Class_Name = db.Column(db.String(14), unique=False, nullable=True)
    Classroom = db.Column(db.String(3), unique=False, nullable=True)
    Week = db.Column(db.String(1), unique=False, nullable=True)
    Hour = db.Column(db.String(1), unique=False, nullable=True)
    Start = db.Column(db.String(5), unique=False, nullable=True)
    End = db.Column(db.String(5), unique=False, nullable=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __lt__(self, other):
        return self.Start < other.Start

    def __repr__(self):
        info = f'<Room_108 id={self.id}\n  Class_Name="{self.Class_Name}" Classroom={self.Classroom}\n'
        info += f'  Week={self.Week} Hour={self.Hour}\n'
        info += f'  Start={self.Start} End={self.End}\n>'
        return info

    def get_time(self, date):
        start_date = date
        end_date = date
        sp = self.Start.split(':')
        # print(sp)
        start_date = start_date.replace(hour=int(sp[0]), minute=int(sp[1]), second=0)
        sp = self.End.split(':')
        # print(sp)
        end_date = end_date.replace(hour=int(sp[0]), minute=int(sp[1]), second=0)
        return start_date, end_date

class Name_List(db.Model):
    __tablename__ = 'namest'

    uid = db.Column(db.String(15), unique=True, nullable=False, primary_key=True)
    namess = db.Column(db.String(30), unique=False, nullable=True)

    def __repr__(self):
        info = f'<Name_List uid={self.uid} names={self.namess}>'
        return info

class Success_Record(db.Model):
    __tablename__ = 'succ_records'

    no2 = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True)

    std_no = db.Column(db.String(9), unique=False, nullable=True)
    room = db.Column(db.String(5), unique=False, nullable=True)
    seat = db.Column(db.String(5), unique=False, nullable=True)
    time = db.Column(db.String(20), unique=False, nullable=True)
    timest = db.Column(db.DateTime(), unique=False, nullable=True)

    def __lt__(self, other):
        return self.std_no < other.std_no
    def __gt__(self, other):
        return self.std_no > other.std_no

    def __repr__(self):
        info = f'<Success_Record no2={self.no2}\n'
        info += f'  std_no={self.std_no} room={self.room}\n'
        info += f'  time={self.time} timest={self.timest}'
        info += '>\n'
        return info
