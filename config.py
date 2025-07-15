#Configure Database Connection 
class Config:
    def __init__(self):
        self.DEBUG = True
        self.SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:rith23112004@localhost:3306/moviemanagementdb'
