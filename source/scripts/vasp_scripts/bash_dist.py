bash_dist.sh
===========

This bash script calculate Cx species num 

.. include warning_gnuplot.rst

::

import numpy as np


class atom():
      """
      Class for representing an atom

      Parameters:

      index: index of this atom
      pos: position of this atom
      sp_index: index of its species

      atomnum: number of carbon atoms in its species
      atoms_list: index of all species

      if index!=sp_index, the info of atomnum and atoms_list is useless

      Method:
      join(index_j):   add j atom into this species

      """

      def __init__(self,index,pos):
            self.index=index
            self.pos=pos
            self.sp_index=index
            self.atomnum=1
            self.atoms_list=[]
            self.atoms_list.append(index)

      def extend_sp(self,index_j):
            global atoms
            if self.index != self.sp_index:
                  print("error")
                  raise RunError
            at=atoms[index_j]
            self.atomnum=self.atomnum+at.atomnum
            self.atoms_list.extend(at.atoms_list)
            at.update(self.sp_index)

      def update(self,index_j):
            global atoms
            for i in self.atoms_list:
                  atoms[i].sp_index=index_j;

def dist(i,j):
      return np.linalg.norm(i.pos-j.pos)

def sp_join(i,j):
      global atoms
      if i.sp_index==j.sp_index:
            return
      if i.sp_index < j.sp_index:
            atoms[i.sp_index].extend_sp(j.sp_index)
      else:
            atoms[j.sp_index].extend_sp(i.sp_index)

def calculate(pos):
      global atoms
      atoms=[]
      for i in range(0,pos.shape[0]):
            atoms.append(atom(i,pos[i]))

      for i in range(0,len(atoms)):
            for j in range(i,len(atoms)):
                  if dist(atoms[i],atoms[j])<1.7: 
                        sp_join(atoms[i],atoms[j])

      num=[0,0,0,0,0]
      for i in atoms:
            if i.index==i.sp_index:
                  if i.atomnum<5:
                        num[i.atomnum-1]+=1
      return num
                        
def skip(traj):
      if len(traj.readline())==0:
            return 0
      for i in range(8):
            traj.readline()
      return 1

def get_atom_num(traj):
      for i in range(3):
            traj.readline()
      num_atom=int(traj.readline().rstrip('\n'))
      
      return num_atom

def write_info(sp):
      for filename in filenames:
            if len(filename)>0:
                  sp.write(str(num[0])+'\t'+str(num[1])+'\t'+str(num[2])+'\t'+str(num[3])+'\t'+str(num[4])+'\n')

atoms=[]

fin=open('dump.lammpstrj','r')
fout=open('species','w')
atom_num=get_atom_num(fin)
fin.seek(0)
while skip(fin):
      pos=[]
      for i in range(atom_num):
            cont=fin.readline().rstrip('\n').split()
            if len(cont) !=8:
                  print("len(cout): "+str(len(cont)))
                  print("cout.{}".format(cont))
                  print(str(len(pos)))
                  exit()
            else:
                  if cont[1]=="2":
                        pos.append(cont)
      pos=np.array(pos)
      pos=pos[:,2:5]
      pos=pos.astype(np.float64)
      num=calculate(pos)
      fout.write(str(num[0])+'\t'+str(num[1])+'\t'+str(num[2])+'\t'+str(num[3])+'\t'+str(num[4])+'\n')
fin.close()
fout.close()
