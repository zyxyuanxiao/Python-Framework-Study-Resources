#!/bin/bash
#!/usr/tcl/bin/expect

git_p(){
    echo "----------拉取最新代码----------"
    cd /srv/HuntingBall
    git pull origin master
#    echo 'yangyuexiong'
#    echo 'python33'
#    expect "Username for 'https://gitee.com'"
#    send "yangyuexiong\n"
#    expect "Password for 'https://yangyuexiong@gitee.com'"
#    send "python33\n"
#    interact

}

git_p
