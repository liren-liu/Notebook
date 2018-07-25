Extract data from Gaussian output file \*.log to series XSF files
===========

::

      grep "SCF Done" *.log|awk '{print $5}' >energy.dat
      cat *.log |sed -n '/concise/,/Rotational/p'| awk '{if($1 ~ /^[0-9]+$/) print $0;}'  >stru.dat
      natoms=`grep NAtoms *.log |head -1 |awk '{print $2}'`
      split -l $natoms -a 3  -d stru.dat g
      mkdir str
      rm stru.dat
      mv g* energy.dat str
      cd str
      mv g09.pbs ..
      sed -i '$d' energy.dat
      ls g* >files
      a=`tail -1 files`
      rm $a
      a=`tail -2 files|head -1 `
      rm $a
      rm files

      a=1
      for i in g*
      do
            e=`head -n $a energy.dat |tail -1`
            echo "# total energy = $e a.u." >$i.xsf
            echo " " >>$i.xsf
            echo "ATOMS" >>$i.xsf
            sort -nk 2 $i |awk '{if($2=="1") printf("H  %f  %f  %f  0  0  0\n",$4,$5,$6);
            else printf("O  %f  %f  %f  0  0  0\n",$4,$5,$6)} '  >>$i.xsf
            a=$(($a+1))
      done

      cd ..
      mkdir xsf
      mv str/*.xsf xsf

