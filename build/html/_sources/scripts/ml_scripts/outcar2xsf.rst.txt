Extract data from OUTCAR to series XSF files
===========

::

      #!/bin/sh
      #lipai@mail.ustc.edu.cn
      #creat xsf files using OUTCAR and POSCAR

      if [ $# = 0 ]; then
            out="OUTCAR"
      else
            out=$1
      fi
      echo $out
      rm *.temp

      awk '/POSITION/,/drift/{
       if(NF==6) print $0
      }' $out  > pos.temp
      grep "energy  without " $out |awk '{print $4}' >energy.temp

      #head -5 POSCAR |tail -3 > primvec.temp
      #atom_1=`awk '{if(NR==6) print $1}' POSCAR`
      #atom_2=`awk '{if(NR==6) print $2}' POSCAR`
      #num_1=`awk '{if(NR==7) print $1}' POSCAR`
      #num_2=`awk '{if(NR==7) print $2}' POSCAR`
      grep -A 3 "direct lattice vectors" $out \
      |head -4|tail -3 |awk '{printf("%f    %f    %f\n",$1,$2,$3)}' >primvec.temp
      atom_1=`grep "POTCAR" $out |awk 'NR==1{print $3}'`
      atom_2=`grep "POTCAR" $out |awk 'NR==2{print $3}'`
      num_1=`grep "ions per type" $out |head -1 \
      |awk '{print $5}' `
      num_2=`grep "ions per type" $out |head -1 \
      |awk '{print $6}' `

      num_atom=`echo "$num_1+$num_2" |bc`
      lines=`wc pos.temp|awk '{print $1}'`
      num_str=`echo "$lines/$num_atom" |bc`

      for i in `seq $num_1`
      do
            echo "$atom_1" >> type.temp
      done
      for i in `seq $num_2`
      do
            echo "$atom_2" >> type.temp
      done

      echo $atom_1 $num_1
      echo $atom_2 $num_2
      echo "all $num_atom"
      echo "num of str: $num_str"

      for i in `seq $num_str`
      do
            energy=`head -n $i energy.temp|tail -1`
            echo "# total energy = $energy eV" >> str_$i.xsf
            echo " " >> str_$i.xsf
            echo "CRYSTAL" >> str_$i.xsf
            echo "PRIMVEC" >> str_$i.xsf
            cat primvec.temp >> str_$i.xsf
            echo "PRIMCOORD" >> str_$i.xsf
            echo "$num_atom 1" >> str_$i.xsf
            end=`echo "$i*$num_atom" |bc `
            head -n $end pos.temp|tail -n $num_atom >pos_i.temp
            paste type.temp pos_i.temp >> str_$i.xsf
            mv str_$i.xsf $out-$i.xsf
      done

      rm *.temp
      if [ ! -d "struc" ]; then
            mkdir struc
      fi
      mv *xsf struc

