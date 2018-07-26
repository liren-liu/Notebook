fix_atoms
=========
::

   #!/usr/bin/python
   #The script is written by liren,Email: llr@mail.ustc.edu.cn
   import sys
   
   aname=sys.argv[1]
   bname=sys.argv[2]
   c=float(sys.argv[3])
   a=open(aname)
   b=open(bname,'w')
   
   #line=a.readlines()
   title=a.readline()
   whatever=a.readline()
   latt1=a.readline()
   latt2=a.readline()
   latt3=a.readline()
   atom=a.readline()
   natom=a.readline()
   direct=a.readline()
   b.write('%s\n'%title.strip())
   b.write('%s\n'%whatever.strip())
   b.write('%s\n'%latt1.strip())
   b.write('%s\n'%latt2.strip())
   b.write('%s\n'%latt3.strip())
   b.write('%s\n'%atom.strip())
   b.write('%s\n'%natom.strip())
   b.write('%s\n'%'Selective dynamics')
   b.write('%s\n'%direct.strip())
   for line in a.readlines():
            num=line.split()
            if float(num[2])<=c:
                b.write('%-16s%-16s%-16s%3s%3s%3s\n'%(num[0],num[1],num[2],'F','F','F'))
            else:
                b.write('%-16s%-16s%-16s%3s%3s%3s\n'%(num[0],num[1],num[2],'T','T','T'))
   b.close()

