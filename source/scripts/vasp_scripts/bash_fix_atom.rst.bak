fix_atom.sh
===========

This page contains a bash script to fix atoms in POSCAR.

**usage:**   *fix_atom.sh 0.3*
It fixs atoms with z coordinate lower than 0.3.

::

    #!/bin/sh
    #lipai@mail.ustc.edu.cn
    awk '{
          if ( NR > 9 )
          {
                if ( $3 < 0.04 ) 
                      printf("%10.7f %10.7f %10.7f %s %s %s\n",$1,$2,$3,"F","F","F")
                else 
                      printf("%10.7f %10.7f %10.7f %s %s %s\n",$1,$2,$3,"T","T","T")
          }
          else 
          print $0 
    }' POSCAR > POSCAR-new
