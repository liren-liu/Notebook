Plot Phasediagram
===========

This python script use ase to plot phasediagram


::

      #lipai@mail.ustc.edu.cn
      from ase.phasediagram import PhaseDiagram
      u=[0.0,-2.92,-3.10,-3.20]

      Li=0
      Br=0.0
      O2=0.0

      Br2O3=-0.209*5

      for u_Li in u: 
            Li2O=-2.071*3-2*u_Li
            Li2O2=-1.65*4-2*u_Li

            LiBr=-1.573*2-u_Li

            #Li3OBr=Li2O+LiBr+0.075*5
            Li32O11Br10=11*Li2O+10*LiBr+0.059*53

            refs = [('Br',Br),
                    ('O2',O2),
                    ('Li',u_Li),
                    ('Br2O3',Br2O3),
                    ('Li2O',Li2O),
                    ('Li2O2',Li2O2),
                    ('LiBr',LiBr),
            #        ('Li3OBr',Li3OBr),
                    ('Li32O11Br10',Li32O11Br10)]

            pd = PhaseDiagram(refs)
            fig=pd.plot(show=False)
            fig.savefig("try"+str(u_Li)+".png")
            #pd.savefig(str(u_Li)+".png")

      import matplotlib.pyplot as plt
      u=[0.0,-2.92,-3.10,-3.20]

      for u_Li in u:
            O2=0.0
            Li2O=(-2.071*3-2*u_Li)/1
            Li2O2=(-1.65*4-2*u_Li)/2

            Br2O3=(-0.209*5)/5

            Br=0.0
            LiBr=(-1.573*2-u_Li)/1
            Li32O11Br10=(11*Li2O+10*LiBr+0.059*53)/21

            x_Br=[1,0,2/5.0,0,0,1,10/21.0]
            y=[Br,O2,Br2O3,Li2O,Li2O2,LiBr,Li32O11Br10]
            name=["Br","O2","Br2O3","Li2O","Li2O2","LiBr","Li32O11Br10"]
            plt.plot(x_Br,y,'sr')
            for i,j,k in zip(x_Br,y,name):
                  #cname=
                  if k=="Li2O" :
                        plt.text(i-0.09,j+0.01,k,color='g')
                  else:
                        plt.text(i+0.02,j+0.01,k,color='r')
            plt.xlim([-0.1,1.1])
            plt.axis("off")            
            plt.savefig(str(u_Li)+".png")
            plt.clf()
            
            print "x_Br     y"
            for i,j in zip(x_Br,y):
                  print i,j

