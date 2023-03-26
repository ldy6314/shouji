from flask import Blueprint, jsonify, request, g, send_file
from .models import People
from .models import User
from .extentions import db
from functools import wraps
from .utils import generate_token, decode_token
import os

bp = Blueprint('bp', __name__)


@bp.before_app_first_request
def first_request():
    db.drop_all()
    db.create_all()
    try:
        os.mkdir(bp.root_path+"/data")
    except Exception as e:
        print(e)
    try:
        user1 = User(
                    role = 1,
                    subject_name = "趣味编程",
                    teacher_name = "老鲁",
                    teacher_info = "我是一个又有趣的教师",
                    subject_info = "我是一个又有趣的社团" ,
                    username = "ldy6314",
                    pwd="ldy7842431"
        )
        user2 =  User(
                    role = 0,
                    subject_name = "管理员",
                    teacher_name = "老鲁",
                    teacher_info = "我是一个管理员",
                    subject_info = "管理工作好好玩" ,
                    username = "admin",
                    pwd="ldy7842431")
        os.mkdir(bp.root_path + '/data/'+user1.subject_name)
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
    except Exception as e:
        print(e)
    print(bp.root_path +'/data')

@bp.route('/')
def index():
    return jsonify("Hello World!111111111111\n")


@bp.route('/upload_pic', methods=['POST'])
def upload_pic():
    print(request.files)
    return 'success'


@bp.before_request
def judge_login():
    for key in request.headers:
        print(key)
    token = request.headers.get('token')
    print("the token=", token)
    if not token:
        g.current_user = None
        g.login_message = '尚未登录'
    else:
        res = decode_token(token)
        if not res[0]:
            g.current_user = None
            g.login_message = res[1]
        else:
            g.current_user = res[1]['userid']
            g.login_message = '已登录'
    print('login_message:', g.login_message, 'current_usr=', g.current_user)


def login_required(func):
    @wraps(func)
    # 获取令牌
    def decorated(*args, **kwargs):
        if g.current_user:
            return func(*args, **kwargs)
        else:
            return jsonify({'message': g.login_message}), 401
    return decorated


@bp.route('/login', methods=['POST'])
def login():
    print('token=', request.headers.get('token'))
    data = request.get_json()
    username = data['account']
    pwd = data['password']
    res = User.query.filter_by(username=username).first()
    subject_name = res.subject_name
    if res and res.validate_password(pwd):
        token = generate_token(res.id)
        print("token=",token)
        return jsonify({'message': 'success', 'token': token, 'subject_name':subject_name}), 200
    else:
        return jsonify('账号或者密码错误'), 401


@bp.route('/get_all')
@login_required
def get_all():
    res = People.query.all()
    print(res)
    res = list(map(lambda x: {'id': x.id, 'name': x.name, 'age': x.age}, res))
    print(res)
    return jsonify(
        res
    )


@bp.route('/logout')
def logout():
    g.current_user = None
    g.login_message = '未登录'
    print('login out success')
    return jsonify({'message': '登出成功'}), 200


@bp.route('/clear_all')
def clear_all():
    persons = People.query.all()
    for person in persons:
        db.session.delete(person)
    db.session.commit()
    return 'clear'


@bp.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    name, age = data['name'], data['age']
    response = dict()
    res = People.query.filter(People.name == name).first()
    if not res:
        person = People(name=name, age=age)
        db.session.add(person)
        db.session.commit()
    response['result'] = 'fail' if res else 'success'

    return jsonify(response)


@bp.route('/delete/<int:person_id>', methods=['GET'])
def delete_person(person_id):
    res = People.query.filter_by(id=person_id).first()
    db.session.delete(res)
    db.session.commit()
    return jsonify(res.name)


@bp.route('/updateInfo/<int:person_id>', methods=['POST'])
def update_info(person_id):
    data = request.get_json()
    _, age = data['name'], data['age']
    response = dict()
    res = People.query.filter(People.id == person_id).first()
    response['result'] = 'success' if res else 'fail'
    res.age = age
    db.session.commit()
    return jsonify(response)

@bp.route('/get_img_list', methods=['GET'])
@login_required
def get_img_list():
    import os
    path = bp.root_path
    return jsonify(os.listdir(path+'/img'))


@bp.route('/get_img/<img_name>', methods=['GET'])
def get_img(img_name):
    path = bp.root_path + '/img/'
    return send_file(path+img_name)


@bp.route('/get_touxiang/<img_name>', methods=['GET'])
def get_touxiang(img_name):
    path = bp.root_path + '/img/'
    return send_file(path+img_name)