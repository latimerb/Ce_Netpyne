from neuron import h
from math import pi

class RegularSpiking:
  def __init__ (self):
	self.soma = soma = h.Section(name='soma',cell=self)
	
	self.adend = adend = h.Section(name='adend',cell=self)
	self.bdend = bdend = h.Section(name='bdend',cell=self)
	self.adend.connect(self.soma,1,0) #   connect dend(0), soma(1)
	self.bdend.connect(self.soma,0,1)
	
	self.initsoma()
	self.initadend()
	self.initbdend()
	
  def initsoma (self):
	soma = self.soma
	soma.nseg = 1
	soma.diam = 10.0
	soma.L = 15
	soma.Ra = 200
	soma.cm = 0.9
	soma.insert('leak'); soma.glbar_leak = 1.1e-5; soma.el_leak = -99;
	soma.insert('na'); soma.ena = 55; soma.gnabar_na = 0.2
	soma.insert('kdr'); soma.ek = -90; soma.gkdrbar_kdr = 0.04
	soma.insert('hva'); soma.ghvabar_hva= 0.005;
	soma.insert('im'); soma.gmbar_im = 0.0001;
	soma.insert('a'); soma.gabar_a = 5e-5
	soma.insert('capool'); soma.eca = 120; taucac_capool = 1;
	soma.taucas_capool = 1000; soma.cainf_capool = 50e-6;
	caci = soma.cainf_capool; casi = soma.cainf_capool;


  def initadend (self):
	adend = self.adend
	adend.nseg = 1
	adend.diam = 5
	adend.L = 300
	adend.Ra = 150
	adend.cm = 0.9
	adend.insert('leak'); adend.glbar_leak = 1.1e-5; adend.el_leak = -99;
	adend.insert('na'); adend.ena = 55; adend.gnabar_na = 0.2;
	adend.insert('kdr'); adend.ek = -90; adend.gkdrbar_kdr = 0.0085;
	adend.insert('hva'); adend.ghvabar_hva = 0.00115;
	adend.insert('im'); adend.gmbar_im = 0.0001;
	adend.insert('sAHP'); adend.gsAHPbar_sAHP = 3e-6;
	adend.insert('ihyper'); adend.ghbar_ihyper = 2e-5;
	adend.insert('a'); adend.gabar_a = 5e-5;
	adend.insert('capool'); adend.eca = 120; taucac_capool = 1;
	adend.taucas_capool = 1000; adend.cainf_capool = 50e-6;
	caci = adend.cainf_capool; casi = adend.cainf_capool;
	
  def initbdend (self):
	bdend = self.bdend
	bdend.nseg = 1
	bdend.diam = 5
	bdend.L = 300
	bdend.Ra = 150
	bdend.cm = 0.9
	bdend.insert('leak'); bdend.glbar_leak = 1.1e-5; bdend.el_leak = -99;
	bdend.insert('na'); bdend.ena = 55; bdend.gnabar_na = 0.2;
	bdend.insert('kdr'); bdend.ek = -90; bdend.gkdrbar_kdr = 0.0085;
	bdend.insert('hva'); bdend.ghvabar_hva = 0.00115;
	bdend.insert('im'); bdend.gmbar_im = 0.0001;
	bdend.insert('sAHP'); bdend.gsAHPbar_sAHP = 3e-6;
	bdend.insert('ihyper'); bdend.ghbar_ihyper = 2e-5;
	bdend.insert('a'); bdend.gabar_a = 5e-5;
	bdend.insert('capool'); bdend.eca = 120; taucac_capool = 1;
	bdend.taucas_capool = 1000; bdend.cainf_capool = 50e-6;
	caci = bdend.cainf_capool; casi = bdend.cainf_capool;
	



class LowThresholdBursting:
  def __init__ (self):
	self.soma = soma = h.Section(name='soma',cell=self)
	self.adend = adend = h.Section(name='adend',cell=self)
	self.bdend = bdend = h.Section(name='bdend',cell=self)
	self.adend.connect(self.soma,1,0) #   connect dend(0), soma(1)
	self.bdend.connect(self.soma,0,1)
	
	self.initsoma()
	self.initadend()
	self.initbdend()

  def initsoma (self):
	soma = self.soma
	soma.nseg = 1
	soma.diam = 10.0
	soma.L = 15
	soma.Ra = 150
	soma.cm = 0.8
	soma.insert('leak'); soma.glbar_leak = 2.1e-5; soma.el_leak = -80;
	soma.insert('na'); soma.ena = 55; soma.gnabar_na = 0.14#0.2
	soma.insert('kdr'); soma.ek = -90; soma.gkdrbar_kdr = 0.019
	soma.insert('hva'); soma.ghvabar_hva = 0.00020#0.0005
	soma.insert('im'); soma.gmbar_im = 4e-5
	soma.insert('a'); soma.gabar_a = 1e-5
	soma.insert('cat'); soma.gcabar_cat = 0.00035#.0002
	soma.insert('capool'); soma.eca = 120; taucac_capool = 1;
	soma.taucas_capool = 500; soma.cainf_capool = 50e-6;
	caci = soma.cainf_capool; casi = soma.cainf_capool;


  def initadend (self):
	adend = self.adend
	adend.nseg = 1
	adend.diam = 5
	adend.L = 300
	adend.Ra = 150
	adend.cm = 0.75
	adend.insert('leak'); adend.glbar_leak = 2.1e-5; adend.el_leak = -80;
	adend.insert('na'); adend.ena = 55; adend.gnabar_na = 0.14;
	adend.insert('kdr'); adend.ek = -90; adend.gkdrbar_kdr = 0.003;
	adend.insert('hva'); adend.ghvabar_hva = .00020#5e-5;
	adend.insert('im'); adend.gmbar_im = 4e-5;
	adend.insert('sAHP'); adend.gsAHPbar_sAHP = 0.00018;
	adend.insert('ihyper'); adend.ghbar_ihyper = 0;
	adend.insert('a'); adend.gabar_a = 1e-5;
	adend.insert('cat'); gcabar_cat = 0.00035#0.00025;
	adend.insert('capool'); adend.eca = 120; taucac_capool = 1;
	adend.taucas_capool = 500; adend.cainf_capool = 50e-6;
	caci = adend.cainf_capool; casi = adend.cainf_capool;
	
  def initbdend (self):
	bdend = self.bdend
	bdend.nseg = 1
	bdend.diam = 5
	bdend.L = 300
	bdend.Ra = 150
	bdend.cm = 0.75
	bdend.insert('leak'); bdend.glbar_leak = 2.1e-5; bdend.el_leak = -80;
	bdend.insert('na'); bdend.ena = 55; bdend.gnabar_na = 0.14;
	bdend.insert('kdr'); bdend.ek = -90; bdend.gkdrbar_kdr = 0.003;
	bdend.insert('hva'); bdend.ghvabar_hva = .00020#5e-5;
	bdend.insert('im'); bdend.gmbar_im = 4e-5;
	bdend.insert('sAHP'); bdend.gsAHPbar_sAHP = 0.00018;
	bdend.insert('ihyper'); bdend.ghbar_ihyper = 0;
	bdend.insert('a'); bdend.gabar_a = 1e-5;
	bdend.insert('cat'); gcabar_cat = 0.00035#0.0002;
	bdend.insert('capool'); bdend.eca = 120; taucac_capool = 1;
	bdend.taucas_capool = 500; bdend.cainf_capool = 50e-6;
	caci = bdend.cainf_capool; casi = bdend.cainf_capool;

	
class LateFiring:
  def __init__ (self):
	self.soma = soma = h.Section(name='soma',cell=self)
	self.adend = adend = h.Section(name='adend',cell=self)
	self.bdend = bdend = h.Section(name='bdend',cell=self)
	self.adend.connect(self.soma,1,0) #   connect dend(0), soma(1)
	self.bdend.connect(self.soma,0,1)
	
	self.initsoma()
	self.initadend()
	self.initbdend()

  def initsoma (self):
	soma = self.soma
	soma.nseg = 1
	soma.diam = 10.0
	soma.L = 15
	soma.Ra = 150
	soma.cm = 0.7
	soma.insert('leak'); soma.glbar_leak = 2.7e-5; soma.el_leak = -79;
	soma.insert('na'); soma.ena = 55; soma.gnabar_na = 0.12
	soma.insert('kdr'); soma.ek = -90; soma.gkdrbar_kdr = 0.06
	soma.insert('hva'); soma.ghvabar_hva= 0.00001
	soma.insert('im'); soma.gmbar_im = 1e-6
	soma.insert('a'); soma.gabar_a = .001#.0011
	soma.insert('capool'); soma.eca = 120; taucac_capool = 1;
	soma.taucas_capool = 500; soma.cainf_capool = 50e-6;
	caci = soma.cainf_capool; casi = soma.cainf_capool;


  def initadend (self):
	adend = self.adend
	adend.nseg = 1
	adend.diam = 5
	adend.L = 300
	adend.Ra = 150
	adend.cm = 0.7
	adend.insert('leak'); adend.glbar_leak = 2.7e-5; adend.el_leak = -79;
	adend.insert('na'); adend.ena = 55; adend.gnabar_na = 0.12;
	adend.insert('kdr'); adend.ek = -90; adend.gkdrbar_kdr = 0.002;
	adend.insert('hva'); adend.ghvabar_hva = 9.5e-5;
	adend.insert('im'); adend.gmbar_im = 2e-6;
	adend.insert('sAHP'); adend.gsAHPbar_sAHP = 0.00015;
	adend.insert('ihyper'); adend.ghbar_ihyper = 0;
	adend.insert('a'); adend.gabar_a = .00109#.001;
	adend.insert('capool'); adend.eca = 120; taucac_capool = 1;
	adend.taucas_capool = 500; adend.cainf_capool = 50e-6;
	caci = adend.cainf_capool; casi = adend.cainf_capool;
	
  def initbdend (self):
	bdend = self.bdend
	bdend.nseg = 1
	bdend.diam = 5
	bdend.L = 300
	bdend.Ra = 150
	bdend.cm = 0.7
	bdend.insert('leak'); bdend.glbar_leak = 2.7e-5; bdend.el_leak = -79;
	bdend.insert('na'); bdend.ena = 55; bdend.gnabar_na = 0.12;
	bdend.insert('kdr'); bdend.ek = -90; bdend.gkdrbar_kdr = 0.002;
	bdend.insert('hva'); bdend.ghvabar_hva = 9.5e-5;
	bdend.insert('im'); bdend.gmbar_im = 2e-6;
	bdend.insert('sAHP'); bdend.gsAHPbar_sAHP = 0.00015;
	bdend.insert('ihyper'); bdend.ghbar_ihyper = 0;
	bdend.insert('a'); bdend.gabar_a = 0.00109#.001;
	bdend.insert('capool'); bdend.eca = 120; taucac_capool = 1;
	bdend.taucas_capool = 500; bdend.cainf_capool = 50e-6;
	caci = bdend.cainf_capool; casi = bdend.cainf_capool;
