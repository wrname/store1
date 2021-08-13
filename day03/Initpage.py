class Initpage:

    # 成功用例的数据
    login_success_data = [
        {"username":"WangRui","password":"12341234","expect":"Student Login"},
        {"username": "root", "password": "root", "expect": "student login"}
    ]

    # 失败用例的数据：msg_uname
    login_pwd_error_data = [
        {"username": "不再爱了", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
    ]

    login_longin1_data = [
        {"username": "root", "password": "123456", "expect": "账号密码登录错误，请重新登录"}
    ]

    login_longin2_data = [
        {"username": "A0a汉", "password": "123456", "expect": "账号密码登录错误，请重新登录"}
    ]










