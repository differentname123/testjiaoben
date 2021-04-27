#!/bin/bash
d=`date "+%Y%m%d%H"`
echo $d
step=1  #间隔的秒数，不能大于60
for ((i=0;i<600;i=(i+step)));do
    l=`tail -n1 /a8root/work/log/fps.abtest.base/access-$d.log`
    python compare.py "$l"
    sleep $step
done
exit 0