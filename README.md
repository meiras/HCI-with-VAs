# HCI-with-VAs (in progress)

__*LS COMMENTS:*__
*I opted to go ahead and get folks comments sooner rather than later on this given the timeline for our final project. If you have any questions or concerns, let me know!*

# Model Proposal for Human Interaction with Virtual Assistants

Meira Chefitz

* Course ID: CMPLXSYS 530,
* Course Title: Computer Modeling of Complex Systems
* Term: Winter, 2018



&nbsp; 

### Goal 
*****
 
The goal of the model is to simulate how people have varying expectations when interacting with conversational agents (machines) and how those expectations may change overtime. This model is an exercise in applying models in human-human interaction to human-computer interaction while accounting for the difference.


&nbsp;  
### Justification
****


This human-computer interaction research problem entails an interplay of multiple components. I am interested in using computational modeling as a means to communicate to others about these interactions. At a minimum, a benefit of a model of human interactions with interfaces is that it may provide me with an opportunity to communicate ideas about human-computer interaction to researchers in multiple disciplines. A visual output could be useful in explaining to designers the potential implications in their designs. Last, the model provides an opportunity explore emergent behaviors in HCI.


&nbsp; 
### Main Micro-level Processes and Macro-level Dynamics of Interest
****

A micro-level process of interest is the one-to-one interaction of a person with a conversational interface given a person's initial expectation of the machine and the machines actual performance. In that relationship, a measure of interest is to what extent expectations were met. In turn, a person may adjust expectations. Macro-level dynamics of interest are in the diversity of expectations across people and the diversity in performance of conversational interfaces meeting those expectations. Additional behaviors of interest are in human-computer interaction when the conversational interface can interact across multiple subject domains, and when people adjust expectations for one interface based on an experience with another interface.

&nbsp; 


## Model Outline
****
&nbsp; 
### 1) Environment
_Description of the environment in your model. Things to specify *if they apply*:_

The current iteration is a bipartite graph. There are boundary conditions because there are defined edges within the network.

NetworkX will be used in Python
https://networkx.github.io/documentation/networkx-1.10/reference/algorithms.bipartite.html

Notes:
* _Boundary conditions (e.g. wrapping, infinite, etc.)_[not necessary]
* _Dimensionality (e.g. 1D, 2D, etc.)_[2D]
* _List of environment-owned variables (e.g. resources, states, roughness)_[location, but only for visualization]
* _List of environment-owned methods/procedures (e.g. resource production, state change, etc.)_none

__*LS COMMENTS:*__
*I'd probably go ahead and file this part of the model under "topology" rather than environment. Good description and conceptualization, however.*


```python
# NetworkX will be used in Python per Sayama's Random Walk on a Network

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import networkx as NX
from networkx.algorithms import bipartite

#Include first pass of the code you are thinking of using to construct your environment
B = nx.Graph()
B.add_nodes_from([1,2,3,4], bipartite=0) # Add the node attribute "bipartite"
B.add_nodes_from(['a','b','c'], bipartite=1)
B.add_edges_from([(1,'a'), (1,'b'), (2,'b'), (2,'c'), (3,'c'), (4,'a')])

# NetworkX creates soemthing like a group for each set

# bool on connection to check
nx.is_connected(B)

#create the two sets so top nodes are 1,2,3,4 and bottom nodes are a,b,c
bottom_nodes, top_nodes = bipartite.sets(B)


# This may be a set of "patches-own" variables and a command in the "setup" procedure, a list, an array, or Class constructor
# Feel free to include any patch methods/procedures you have. Filling in with pseudocode is ok! 
# NOTE: If using Netlogo, remove "python" from the markdown at the top of this section to get a generic code block
```

__*LS COMMENTS:*__
*This is a solid start. Currently, your network is not very big - are you thinking of expanding it later? Also, I'm assuming that the letters represent the computer interfaces. Is that correct?*

&nbsp; 

### 2) Agents
 
 _Description of the "agents" in the system. Things to specify *if they apply*:_

 There are two types of agents. Agents are conversational interfaces and humans. In the first version, humans will only interact with converstional interfaces and vice versa in an undirected network. In this iteration, humans will act as perceivers and conversational interfaces will act as targets.
 Perceivers will own expectation variables. Targets will own performance variables. In the first iteration, these will be dummy factors in the form of an array or single weight. Ideally, these will be set to allow for different expectations by one perceiver based on the target.

 
* _agent-owned variables: type; identification number; number of targets a perceiver is connected to
* _agent-owned methods/procedures: interact with target (perceiver); perform (target); adjust expectation (perceiver) 


```python
# Create agents for people. Number is not important, maybe 10 to allow some variablity
# Create agents for conversational interfaces/virtual assistants. Have a few different types: personal virtual assistant at #home, personal virtual assistant on the go, bank virtual assistant, customer service virtual assistant, therapy virtual #assistant.
# People agents (perceivers) have properties of expectations per virtual assistant (target).
# Edges ties perceivers to targets. In one tick, perceiver will interact with its connections/targets a certain number of times dependings on the frequency set. For example, in one tick,the assisatn may interact with a personal virtual assistant three times and a bank assistant once. There might be a probaility in a tick that it interacts with a customer support assistant.
# Model will also allow for added level of performance variables owned by target agents for each perceiver agent. 
# Expectations may take the form of a set of dummy variables. Performance variables are from the same set of dummy variables.
# For example, if perceiver 1 expects D, E, F from target 1, and target 1 performs D, E, F, then the resultis 100% #expectations met.
# An extra level in the model may be a change in interaction if the weights continue to decrease or maintain 100% for a long enough time. These parameters have not been defined yet. Basically, if the interactions meet a threshold of failure conistently and the expectations do not adequately change to accomodate performance, then the perceiver may interact less with the target.

```

__*LS COMMENTS:*__
*I can see the beginnings of how you might be thinking of implementing this model here, but need a lot more specificity and nitty gritty of how you think the code is going to look at this point. There are a lot of ways to operationalize learning and adaptation, but even beginning with something very simple would be a great place to start from. So for example, thinking through precisely how the agent changes its expectations when the previous interaction result is less than 100% and demonstrating how you will execute that through code is what is needed right here.


&nbsp; 

### 3) Action and Interaction 
 
**_Interaction Topology_**

_Description of the topology of who interacts with whom in the system. Perfectly mixed? Spatial proximity? Along a network? CA neighborhood?_

Each perceiver will interact with one or more targets. The variety in nunmber of targets per perceiver is intentional to allow for variablity in expectation adjustment. Targets may interact with one or more perceivers. 
They will connect along a network. The edges will already formed in setup.

 
**_Action Sequence_**

 
_What does an agent, cell, etc. do on a given turn? Provide a step-by-step description of what happens on a given turn for each part of your model_
0. Each perceiver has a stored expectation.
1. Perceivers will be set to interact with targets (begin tick).
2. The target performs.
3. The perceiver adjusts expectations, storing the new expectation.

__*LS COMMENTS:*__
*See previous comment about needing to translate this into actual steps that are being carried out through lines of code. This is a good start, but at this point you'll be needing to move from your conceptual implementation (what is expressed here) to an actual computational implementation.


&nbsp; 
### 4) Model Parameters and Initialization

_Describe and list any global parameters you will be applying in your model._
Time, Network, Position, Type

_Describe how your model will be initialized_
For each perceiver in network, interact with a target. Go through 1:1 interaction with all targets.  

_Provide a high level, step-by-step description of your schedule during each "tick" of the model_
(Rewrite above)

__*LS COMMENTS:*__
*Not sure I would classify the above as global parameters. A global parameter might instead be something like "learning rate," "failure tolerance," or "number of interfaces interacted with"

*In terms of initialization, I would think about this specifically with regard to the expectation sets agents begin with/
&nbsp; 

### 5) Assessment and Outcome Measures

_What quantitative metrics and/or qualitative features will you use to assess your model outcomes?_
The extent to which expectations have changed and in what directoin or if they remained the same. 

&nbsp; 

### 6) Parameter Sweep

_What parameters are you most interested in sweeping through? What value ranges do you expect to look at for your analysis?_
Expectations and performance

__*LS Comments:*__
*Need more clarification on what you mean here. Do you mean expectation set size? Other things to consider are average network degree and learning rate as well.

Notes: 
1. it would be really cool to do this with edges that reflected the extent to which expectations were met as it can become a factor in predicting future interactions.
2. Expectations are adjusted using interpretations of human learning. I am still working on which model is more appropriate based on the options in I'm Game (Abrahamson, Wilensky, and Levin 2007).

__*LS COMMENTS:*__
*I agree that making the network adaptive in the sense that tie weight adjusts depending on performance would be cool. Hope you are able to get to it!*
