# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 上午10:25
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_models.py
# @Software: PyCharm


from extend_libs.exts import Base, db
from app import create_app
from app.cms.admin.models import CMSUser


class User(Base):
    id = db.Column(db.Integer, primary_key=True)
    okc = db.Column(db.String(128), default='okc')


if __name__ == '__main__':

    def c_u():
        with db.auto_commit():
            u = User()
            db.session.add(u)


    def s_u():
        for i in range(1, 2):
            u = User.query.filter_by(id=i).first()
            print(u.to_dict())


    app = create_app()
    with app.app_context():
        # db.create_all()
        # c_u()
        # s_u()
        u = CMSUser.query.filter_by(username='yyx').first()
        print(u)
        print(type(u))
        print(u.roles)
        print(u.check_permissions)

        pass

    a = 0b11111111
    print(a)
    b = 0b00100000
    print(b)
    print(a | b)
