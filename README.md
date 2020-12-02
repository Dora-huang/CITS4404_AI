# CITS4404_AI
All content in the repository is for the unit of 4404 Artifical Intelligent and Adaptive System. 

**HuangX_L1.ipynb** is the first assignment that uses genetic algorithms imitating darwinian natural selection to achieve the fixed sentence "To be, or not to be, that is the question." <br>
The process of genetic algorithm:
1) initialization - create first population including defination of size, contained entities and fitness parameters etc.
2) fitness calculation - for each agent, it needs to be computed a fitness score that represents hwo close the current agent is to required final result.
3) selection - select agents from the population who are fit enough to reproduce
4) crossover - parents' DNA is recombined to create child's DNA during production 

**HuangX_L2_v2.ipynb** is the second assignment using particle systems to implement the fireword. In fact, there are two types of particle systems. 
1) The first one is to optimaize the problem such as ant colony optimization. Many ants explore the different path to get the food and mark their path. After ten of thousand of experiment, the ants would figure out the optimal path from A to B. 
2) The second type is modelling natural systems. Using particle systems can imitate the flow of water or fireworks. Hence, in this assignment, I will use particle sytems to imtate the fireworks with using pygame package in python. The file called **fireworks.py** is the python code without using jupyter notebook. <br>

The folder called **GenerateHouseNumber** contains all stuff of using GAN to generate the housenumber. **raw_imgs2** is the original pictures from the internet fed into the GAN model. **HuangX_L3.ipynb** illustrates how to build the GAN model with pytorch. Besides, I explored the performance of the learning rate and activation function in GAN.

**Fastai.ipynb** is the first attempt to build NLP model that is used to distinguish the real or not for disaster tweets. The main method I used is fastai, one kind of transfer learning. There are two models I built.
1) The first one is the language model that is used to analyze the meaning of sentence.
2) The second one is the classifier, according to the understanding of the previous model. This model determines the disaster tweets is real or not. 

