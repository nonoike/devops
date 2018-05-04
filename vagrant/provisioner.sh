#!/bin/sh

#
# init
#
yum -y update
yum -y install wget


#
# install
#

# git
yum install -y git

# java 8
yum install -y java-1.8.0-openjdk
yum install -y java-1.8.0-openjdk-devel

# scala 2.11.8
git clone git://github.com/mazgi/scalaenv.git ~/.scalaenv
echo 'export PATH="${HOME}/.scalaenv/bin:${PATH}"' >> ~/.bash_profile
echo 'eval "$(scalaenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
scalaenv install scala-2.11.8
scalaenv global scala-2.11.8

# mysql 5.6
yum localinstall -y https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
yum repolist enabled | grep "mysql.*-community.*"
yum-config-manager --disable mysql57-community
yum-config-manager --enable mysql56-community
yum repolist enabled | grep mysql
yum install -y mysql-community-server
# mysql_secure_installation  # 手動実行
