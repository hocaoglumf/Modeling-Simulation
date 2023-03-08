import PetriNets.SimNetScenario
import JobShopSim.BouncingBall

ball=JobShopSim.BouncingBall.Ball()
ball.Initialize()
ball.SetName("Top")
ball.SetTransitionDurationCalculation({"t0": -1, "t1": 0.01, "t2":-1, "t3":-1, "t4":0.001, "t5":-1})


pc= PetriNets.PetriCoordinator.PetriCoordinator()
ball.SetChat(True)
pc.Join(ball)
pc.SetExecutionDuration(500)
pc.SetChat(True)
pc.Run()
