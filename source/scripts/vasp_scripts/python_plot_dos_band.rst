plot DOS & Band Structure
===========

This python script plots dos and band using VASP results


画DOS
::

    %matplotlib inline
    from pymatgen.io.vasp import Vasprun
    from pymatgen.electronic_structure.plotter import DosPlotter

    v = Vasprun('Si-dos/vasprun.xml')
    tdos = v.tdos
    plotter = DosPlotter()
    plotter.add_dos("Total DOS", tdos)
    plotter.show(xlim=[-5, 5], ylim=[0, 4])


画pDOS
::

    %matplotlib inline
    from pymatgen.io.vasp import Vasprun
    from pymatgen.electronic_structure.plotter import DosPlotter

    v = Vasprun('Si-dos/vasprun.xml')
    cdos = v.complete_dos
    element_dos = cdos.get_element_dos()
    plotter = DosPlotter()
    plotter.add_dos_dict(element_dos)
    plotter.show(xlim=[-5, 5], ylim=[0, 1])

画band structure
::

    from pymatgen.io.vasp import Vasprun, BSVasprun
    from pymatgen.electronic_structure.plotter import BSPlotter

    v = BSVasprun("Si-band/vasprun.xml")
    bs = v.get_band_structure(kpoints_filename="Si-band/KPOINTS",line_mode=True)
    plt = BSPlotter(bs)
    plt.get_plot(vbm_cbm_marker=True,ylim=(-3,3))
    plt.show()
