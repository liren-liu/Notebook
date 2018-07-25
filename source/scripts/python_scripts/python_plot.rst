Plot plain figures
==============

Usage:  python plot.py [filename] column_x column_y1 [column_y2 ...]

plot.py for plot data and save fig
----------------------------------
::

    #lipai@mail.ustc.edu.cn
    import sys
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import numpy as np
    mpl.rcParams['agg.path.chunksize']=10000
    arg_num=len(sys.argv)
    if arg_num==1:
        print("no inputs!!!\n")
        exit()
    filename=sys.argv[1]
    data=np.loadtxt(filename,skiprows=1)
    
    colors=['k','r','g','b','c','m']
    labels=['DFT','NN']
    plt.figure(figsize=(10,4))
    if arg_num==2:
        plt.plot(data[:,0],data[:,1])
    
    elif arg_num>3:
        yn=arg_num-3
        if int(sys.argv[2]) == 0:
    #            x=np.arange(data.shape)
    #        else:
    #            x=np.arange(data.shape[0])
            x=np.arange(list(data.shape)[0])
            for i in range(yn):
                if i==0:
                    alpha=1
                else:
                    alpha=0.7
                if  len(data.shape)==1:
                    plt.plot(x,data[:],color=colors[i],linewidth=2,label=labels[i],alpha=alpha)
                else:
                    plt.plot(x,data[:,int(sys.argv[i+3])-1],color=colors[i],linewidth=2,label=labels[i],alpha=alpha)
        else:
            for i in range(yn):
                plt.plot(data[:,int(sys.argv[2])-1],data[:,int(sys.argv[i+3])-1],color=colors[i],linewidth=2,label=labels[i])
    
    else:
        print("wrong input arguments")
    plt.ylabel('Energy/eV')
    #plt.ylim(0,5)
    #plt.axhline(0)
    plt.legend(loc=0)
    plt.savefig("temp.jpg",dpi=300)
    #plt.savefig("temp.jpg")
    #plt.show()
