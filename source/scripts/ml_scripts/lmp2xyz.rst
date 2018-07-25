Convert lammps structure to XYZ file
===========

::

      #!/bin/sh
      #lipai@mail.ustc.edu.cn
      if [ -d "xyz" ] ; then rm -rf xyz; fi
      if [ -f "movie.xyz" ]; then rm movie.xyz;fi
      for i in `seq 0 4000`
      do
            if [ -f "POSCAR-$i" ];then
                  pos2xyz.pl POSCAR-$i
                  cat POSCAR-$i.xyz >>movie.xyz
            else
                  break
            fi
      done
      mkdir xyz
      mv *.xyz xyz

