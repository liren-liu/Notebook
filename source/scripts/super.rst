Scripts for job management system on super-computer
====

PBS system
-------

::

      grep lipai |cut -d . -f 1|xargs qstat -f |egrep "state|DIR"|cut -d K -f 2|cut -d , -f 1|cut -d = -f 2


LSF system
----

::

      echo ================================================================================================
      bjobs
      echo ================================================================================================
      echo 
      echo ================================================================================================
      bjobs -l |egrep -A 1 "CWD"|sed -n 'N;N;s/\n//g'p|awk '{if(NR%2==1) print $0}'|sed 's/ //g'|cut -d , -f 2|cut -d "<" -f 2|cut -d ">" -f 1
      echo ================================================================================================
      echo 
      echo ================================================================================================
      #bjobs -l |egrep -A 1  "CWD"|xargs -l3|cut -d , -f 2|awk '{if($1=="Execution") {print "Run";print ""} else print $0}'\
      #|sed 's/ //g'|cut -d "<" -f 2|cut -d ">" -f 1
      bqueues|grep zyli
      echo ================================================================================================
      bhosts |grep -A 8 node291
      bhosts |grep node300
      echo ================================================================================================
      for i in `seq 291 300`
      do
            lsload |grep node$i
      done
      echo ================================================================================================


YH system
------

::

      yhqueue |grep yang
      yhcontrol show jobs|grep -B 13 "yangjl"|grep Command|cut -d = -f 2
