DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # mysqlclient librarly 설치
        'NAME': 'myboard',
        'USER': 'root',
        'PASSWORD': '****',  # mariaDB 설치 시 입력한 root 비밀번호 입력
        'HOST': 'localhost',
        'PORT': ''
    }
}
