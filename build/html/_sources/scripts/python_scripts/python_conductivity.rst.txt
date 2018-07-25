Calculate ionic conductivity in solid 
===========

This script calculate diffusivity and conductivity from vasprun.xml file

::

      import matplotlib.pyplot as plt
      #import json
      import collections
      from pymatgen import Structure
      from pymatgen.analysis.diffusion_analyzer import DiffusionAnalyzer, \
          get_arrhenius_plot, get_extrapolated_conductivity
      from pymatgen_diffusion.aimd.pathway import ProbabilityDensityAnalysis
      from pymatgen_diffusion.aimd.van_hove import VanHoveAnalysis

      temperatures = [500, 1000, 1500]
      #analyzers = collections.OrderedDict()
      #for temp in temperatures:
      #    with open("%d.json" % temp) as f:
      #        d = json.load(f)
      #        analyzers[temp] = DiffusionAnalyzer.from_dict(d)
      #
      #plt = analyzers[1000].get_msd_plot()
      #title = plt.title("1000K", fontsize=24)
      #
      #diffusivities = [d.diffusivity for d in analyzers.values()]
      #plt = get_arrhenius_plot(temperatures, diffusivities)
      #
      #rts = get_extrapolated_conductivity(temperatures, diffusivities, 
      #                                    new_temp=300, structure=analyzers[800].structure, 
      #                                    species="Li")
      #print("The Li ionic conductivity for Li6PS5Cl at 300 K is %.4f mS/cm" % rts)

      a = ["500/vasprun.xml"]
      b = ["1000/vasprun.xml"]
      c = ["1500/vasprun.xml"]

      analyzer_500 = DiffusionAnalyzer.from_files(a, specie="Li", smoothed=False)
      analyzer_1000 = DiffusionAnalyzer.from_files(b, specie="Li", smoothed=False)
      analyzer_1500 = DiffusionAnalyzer.from_files(c, specie="Li", smoothed=False)

      diffusivities=[analyzer_500.diffusivity,analyzer_1000.diffusivity,analyzer_1500.diffusivity]

      plt = get_arrhenius_plot(temperatures, diffusivities)
      plt.savefig("Li_Arrhenius_Plot.png")
      rts = get_extrapolated_conductivity(temperatures, diffusivities, 
                                          new_temp=300, structure=analyzer_500.structure, 
                                          species="Li")
      print("The Li ionic conductivity for anti-spinel Li3OBr at 300 K is %.4f mS/cm" % rts)
