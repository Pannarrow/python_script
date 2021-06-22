#!/bin/bash
JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home
export JAVA_HOME
export PATH=$PATH:$JAVA_HOME/bin

echo "start redis"
redis-server /usr/local/redis-6.0.6/redis.conf


cd /Users/sunline/Documents/shell
pwd
logfile="tomcat-start.log"
if [ ! -f $logfile ]; then
    echo $logfile" is not exist"
    touch $logfile
fi
pwd >> $logfile
echo "=======`date +%Y%m%d%H%M%S` startup tomcat=======" >> $logfile
echo "sunline"|sudo -S /Users/sunline/Documents/onlinePackages/apache-tomcat-8.5.8/bin/shutdown.sh
echo "command shutdown tomcat" >> $logfile
echo "sunline"|sudo -S /Users/sunline/Documents/onlinePackages/apache-tomcat-8.5.8/bin/startup.sh
echo "command startup tomcat" >> $logfile
echo "sunline"|sudo -S shutdown -h -r 19:37
echo "=======command shutdown macmini=======" >> $logfile

echo "=======start dns=======" >> $logfile
echo "======query dns ps======"
dns_ps=`ps -ef|grep dns`

echo "======dns ps :"${dns_ps}"======"
result=$(echo $dns_ps | grep "dnsmasq")
if [[ "$result" != "" ]]
then
    echo "======kill dns pid======"
    id=""
    dns_pid=""
    eval $(echo $dns_ps | awk '{ printf("id=%s;dns_pid=%s",$1,$2)}')
    # echo $dns_pid
    echo "sunline"|sudo -S kill -9 $dns_pid
fi

echo "======start dns======"
echo "sunline"|sudo -S /usr/local/sbin/dnsmasq --conf-file=/usr/local/etc/dnsmasq.conf
