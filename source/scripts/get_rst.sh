for i in vasp kmc ml  python
do
   cat $i.head >$i.rst
   for j in $i*pts/*
   do
       echo "   $j" >>$i.rst
   done
done
cd ..
make html
