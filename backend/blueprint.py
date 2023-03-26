from flask import Blueprint, jsonify, request, g, send_file, make_response
from .models import People
from .models import User
from .extentions import db
from functools import wraps
from .utils import generate_token, decode_token

bp = Blueprint('bp', __name__)



@bp.route('/')
def index():
    return jsonify("Hello World!\n")


@bp.route('/upload_pic', methods=['POST'])
def upload_pic():
    print(request.files)
    return 'success'


@bp.before_request
def judge_login():
    token = request.headers.get('token')
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
    if res and res.validate_password(pwd):
        token = generate_token(res.id)
        return jsonify({'message': 'success', 'token': token}), 200
    else:
        return jsonify('账号或者密码错误'), 401



@bp.route('/logout')
def logout():
    g.current_user = None
    g.login_message = '未登录'
    print('login out success')
    return jsonify({'message': '登出成功'}), 200


@bp.route('/get_img_list/', methods=['GET'])
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