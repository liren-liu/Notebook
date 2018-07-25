
Convert POSCAR to XSF files
===========

::

      #lipai@mail.ustc.edu.cn
      filename=$1
      pos2xyz.pl $filename
      echo "CRYSTAL" >> $filename.xsf
      echo "PRIMVEC" >> $filename.xsf
      head -5 $filename|tail -3 >> $filename.xsf
      echo "PRIMCOORD" >> $filename.xsf
      num=`head -1 $filename.xyz`
      echo $num 1 >> $filename.xsf
      awk '{if(NR>2) print $0}' $filename.xyz >> $filename.xsf
      rm $filename.xyz
