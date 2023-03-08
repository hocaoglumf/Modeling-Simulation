import PetriNets.SimNetScenario
import JobShopSim.Machine
import JobShopSim.Generator
import JobShopSim.Combiner

#scenario1= PetriNets.SimNetScenario.SimNetScenario()


pg=JobShopSim.Generator.Generator()
pg.Initialize()
pg.SetName("Generator-0")
pg.SetTransitionDurationCalculation({"t0":
            "RandomValueCalculation.Exponential(1.3)"})
pg.SetState({"P0": 1, "P1": 0})

pg0=JobShopSim.Generator.Generator()
pg0.Initialize()
pg0.SetName("Generator-1")
pg0.SetTransitionDurationCalculation({"t0":
            "RandomValueCalculation.Exponential(2.3)"})
pg0.SetState({"P0": 1, "P1": 0})


pm0= JobShopSim.Machine.Machine()
pm0.Initialize()
pm0.SetName("Makine-0")
pm0.SetState({"P0": 0, "P1": 1, "P2": 0, "P3": 0})
pm0.SetTransitionDurationCalculation({"t0": -1, "t1": 1})

pm1= JobShopSim.Machine.Machine()
pm1.Initialize()
pm1.SetState({"P0": 0, "P1": 1, "P2": 0, "P3": 0})
pm1.SetTransitionDurationCalculation({"t0": -1, "t1": 1})
pm1.SetName("Makine-1")

pm2= JobShopSim.Machine.Machine()
pm2.Initialize()
pm2.SetState({"P0": 10, "P1": 1, "P2": 0, "P3": 0})
pm2.SetTransitionDurationCalculation({"t0": -1, "t1": 1})
pm2.SetName("Makine-2")


pm3= JobShopSim.Machine.Machine()
pm3.Initialize()
pm3.SetState({"P0": 10, "P1": 1, "P2": 0, "P3": 0})
pm3.SetTransitionDurationCalculation({"t0": -1, "t1":
    "RandomValueCalculation.Exponential(.7)"})
pm3.SetName("Makine-3")

pm4= JobShopSim.Machine.Machine()
pm4.Initialize()
pm4.SetState({"P0": 10, "P1": 1, "P2": 0, "P3": 0})
pm4.SetTransitionDurationCalculation({"t0": -1, "t1":
    "RandomValueCalculation.Uniform(5,1)"})
pm4.SetName("Makine-4")



pm5= JobShopSim.Machine.Machine()
pm5.Initialize()
pm5.SetState({"P0": 10, "P1": 1, "P2": 0, "P3": 0})
pm5.SetTransitionDurationCalculation({"t0": -1, "t1":
    "RandomValueCalculation.Uniform(5,1)"})
pm5.SetName("Makine-5")

pm6= JobShopSim.Machine.Machine()
pm6.Initialize()
pm6.SetState({"P0": 10, "P1": 1, "P2": 0, "P3": 0})
pm6.SetTransitionDurationCalculation({"t0": -1, "t1":
    "RandomValueCalculation.Uniform(5,1)"})
pm6.SetName("Makine-6")

cmbr= JobShopSim.Combiner.Combiner()
cmbr.Initialize()
cmbr.SetState({"P0": 0, "P1": 0, "P2": 1, "P3": 0, "P4":0})
cmbr.SetTransitionDurationCalculation({"t0": -1, "t1":
    "RandomValueCalculation.Uniform(5,1)"})
cmbr.SetName("Birleştirici-0")

pc= PetriNets.PetriCoordinator.PetriCoordinator()
pc.AttachTransition([pg,"P1",1,pm0, "P0", 1])
pc.AttachTransition([pm0,"P3", 10, pm1, "P0",10 ])
pc.AttachTransition([pm1,"P3", 2, pm2, "P0",2 ])
pc.AttachTransition([pm2,"P3", 2, pm3, "P0",2 ])
pc.AttachTransition([pm3,"P3", 2, pm4, "P0",2 ])

pc.AttachTransition([pg0,"P1",1,pm5, "P0", 1])
pc.AttachTransition([pm5,"P3", 2, pm6, "P0",2 ])
pc.AttachTransition([pm6,"P3", 4, cmbr, "P0",4 ])
pc.AttachTransition([pm4,"P3", 1, cmbr, "P1",1 ])

pg.SetChat(True)
pg0.SetChat(True)
pm0.SetChat(True)
pm1.SetChat(True)
pm2.SetChat(True)
pm3.SetChat(True)
pm4.SetChat(True)
pm5.SetChat(True)
pm6.SetChat(True)
cmbr.SetChat(True)

pc.Join(pg)
pc.Join(pg0)
pc.Join(pm0)
pc.Join(pm1)
pc.Join(pm2)
pc.Join(pm3)
pc.Join(pm4)
pc.Join(pm5)
pc.Join(pm6)
pc.Join(cmbr)
pc.SetChat(True)
pc.SetExecutionDuration(5000)

#scenario1.Join(pc)
#scenario1.Run(3)

pc.Run()

