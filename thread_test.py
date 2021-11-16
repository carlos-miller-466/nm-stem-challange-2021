from turtle import *
from random import randint
import numpy as np
import itertools
import pickle
import threading
import time

start = time.perf_counter()
mode("logo")
tracer(None,32)

class FermentationModel:
    def __init__(self):
        
        # Carbon Dioxide
        CO2 = Turtle()
        CO2.ht()
        CO2.shape("circle")
        CO2.color("grey")
        CO2.resizemode("user")    
        CO2.shapesize(0.3, 0.3)
        self.CO2 = [CO2]

        # Ethanol
        Et = Turtle()
        Et.ht()
        Et.shape("circle")
        Et.color("cyan")
        Et.resizemode("user")
        Et.shapesize(0.5,0.5)
    
    def collision_detection(self, tolerance, precision):
        positions = []
        dry_runs = 0
        with open('COLLISION_DET.log', 'wb') as f_obj:
            pickle.dump('THIS IS A PICKLE OF DATA', f_obj)
        while True:
            # Get X and Y positions
            x_positions = [atom.xcor() for atom in self.CO2]
            y_positions = [atom.ycor() for atom in self.CO2]
            
            # Compare all X positions with a defined tolerance
            for a, b in itertools.combinations(x_positions, 2):
                if a in np.arange(
                    round((b - tolerance),precision),
                    round((b + tolerance),precision),
                    int('1'+'0'*precision)): 
                        print("Collision!")
            
            # Compare all Y positions with a defined tolerance
            for a, b in itertools.combinations(y_positions, 2):
                if a in np.arange(
                    round((b - tolerance),8),
                    round((b + tolerance),8),
                    int('1'+'0'*precision)): 
                        print("Collision!")

            # Log positions
            positions.append((x_positions, y_positions))
            try:
                if positions[-1] != positions[-2]:
                    dry_runs = 0
                    with open('COLLISION_DET.log', 'ab') as f_obj:
                        pickle.dump((x_positions, y_positions), f_obj)
                else:
                    dry_runs += 1
                if dry_runs > 1000:
                    break
            except IndexError:
                continue

    def carbon_dioxide(self, amount):

        self.CO2[0].speed(6)
        self.CO2[0].st()
        for _ in range(amount):
            self.CO2.append(self.CO2[0].clone())
        self.CO2[0].ht()
        self.CO2[0].setpos(1000,1000)

        t1 = threading.Thread(target=self.collision_detection,
                args=(2, 3))

        for x in range(25):
            for c in self.CO2:
                c.seth(randint(0,360))
                mvm = randint(-50,50)
                if mvm == 0:
                    c.fd(1)
                else:
                    c.fd(mvm)
            if x == 1:
                t1.start()

Model = FermentationModel()
Model.carbon_dioxide(10)
done()

finish = time.perf_counter()

print("Executed in", str(round((finish-start),2)), "(s)")

"""
(1) C6H1206 -> 2 Et + 2 CO2, with 2 CO2 making up 25% of atoms "lost" during
fermentation. But, most yeasts can only survive in less than 18% alcohol
before dying to toxicity. Therefore, 100ml of glucose/sucrose could take up
to 10 runs to fully process if the slurry is distilled @ 10% alcohol.

Bypassing true volume and settling for theoretical atomic volume (if all
atoms are equally sized in space at all pressures and temperatures) then
the end result of the Fermentation Model is 75% of the starting volume in
ethanol, and 25% in carbon dioxide.

Inconsistencies in food waste introduce complexities to the simulation. Our
model will either take an average sugar content of multiple biofuel batches
or generalize it as done with simulated volume.

Distillation will be presented with the same simplicity as volume and 
sugar content. The process will be simulated as such:
    Near poisoned yeast strained from biomass-ethanol mixture >>
    heat the mixture towards the boiling point of ethanol >>
    ethanol evaporates and condenses into near pure ethanol >>
    remaining biomass is cooled and the fermentation process begins again.
    
"""










#class Display:
#    def __init__(self):
#        pass
#    def execute(self):
#        shape('circle')
#        color('red', 'yellow')
#        forward(200)
#        left(170)
#        done()
