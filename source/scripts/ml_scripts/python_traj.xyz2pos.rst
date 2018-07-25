Extract poscar files from traj.xyz   
===========

This python script extract poscar files from traj.xyz   
lattice constants are getton from CuC.xsf file


::

    #lipai@mail.ustc.edu.cn
	import os
	f0=open("CuC.xsf")
	f0.readline()
	f0.readline()
	x=f0.readline()
	y=f0.readline()
	z=f0.readline()
	f0.close()
	num_Cu=72

	f1=open("traj.xyz")
	ordi=1
	while 1:
		a=f1.readline()
		if not a:
			break
		num=int(a.split()[0])
		fileout="POSCAR-"+str(ordi)
		f2=open(fileout,"w")
		f2.write("Cu & C system from GCMC simulation\n")
		f2.write("1.0\n")
		f2.write(x)
		f2.write(y)
		f2.write(z)
		f2.write("Cu    C\n")
		f2.write(str(num_Cu)+"  "+str(num-num_Cu))
		f2.write("\nCart\n")
		ordi+=1

		f1.readline()
		for i in range(0,num):
			a=f1.readline().split()
			f2.write(a[1]+"\t"+a[2]+"\t"+a[3]+"\n")
		
		f2.close()

	f1.close()    
				
	os.system('mkdir poscar')
	os.system('mv POSCAR*  poscar')

