#!/usr/bin/env bash

git_Submission(){
    cd /Users/yangyuexiong/Desktop/HuntingBall
    git add .
    git status
    git commit -m $1
    git push origin master
}

development_config(){
    echo "--------切换【开发】环境config--------"
    sed -i "" 's/# DEBUG = True/DEBUG = True/g' /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i "" 's/DEBUG = False/# DEBUG = False/g' /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i "" 's/# port = 9999/port = 9999/g' /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i "" 's/port = 5000/# port = 5000/g' /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i "" "s/# PASSWORD = '123456'/PASSWORD = '123456'/g" /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i "" "s/PASSWORD = 'okcokc111111'/# PASSWORD = 'okcokc111111'/g" /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i "" "s/# redis_pwd = 123456/redis_pwd = 123456/g" /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i "" "s/redis_pwd = 'okc1111'/# redis_pwd = 'okc1111'/g" /Users/yangyuexiong/Desktop/HuntingBall/config.py
    echo "--------done--------"
}

production_config(){
    echo "--------切换【生产】环境config--------"
    sed -i '' 's/DEBUG = True/# DEBUG = True/g' /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i '' 's/# DEBUG = False/DEBUG = False/g' /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i '' 's/port = 9999/# port = 9999/g' /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i '' 's/# port = 5000/port = 5000/g' /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i '' "s/PASSWORD = '123456'/# PASSWORD = '123456'/g" /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i '' "s/# PASSWORD = 'okcokc111111'/PASSWORD = 'okcokc111111'/g" /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i '' "s/redis_pwd = 123456/# redis_pwd = 123456/g" /Users/yangyuexiong/Desktop/HuntingBall/config.py
    sed -i '' "s/# redis_pwd = 'okc1111'/redis_pwd = 'okc1111'/g" /Users/yangyuexiong/Desktop/HuntingBall/config.py
    echo "--------done--------"
}

production_config
echo "--------提交代码--------"
git_Submission $1
echo "--------done--------"
development_config