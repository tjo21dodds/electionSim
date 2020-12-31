# Election Sim
A engine for simulating and comparing voting systems. 
## Core Design
### Architecture
* Each voter has a set number of views (-1.0 to 1.0)
* Voters are members of a constituency.
  * Constituencies have bias that is added to voters own views.
  * "conFactor" effects how great this bias is (0.0 to 1.0)
* Each party has the same number of views (-1.0 to 1.0)
  * Voter's views of each party is calculated using euclidean distance.
  
### Performance
By using numpy matrices we have been able to see high performance.
* Simulations of 50,000,000 voters can be run easily in background.
  * Time : ~30mins
  * RAM : ~1.2Gb
  * CPU : 10% [Ryzen 5 2600x (4GHz)]
## Contributions
Please do contribute, if you want. You can easily add your own voting system and test it out. I would love to hear what you do with it.
## Goals
### Target
  * Votings Systems
    * Single Transferable Vote
    * Additional Member System
    * Alternative Vote
    * AV+
  * Ranking Systems
    * Measure Voter distain for winner
  * Core
    * Support for Constituency Merging (STV with 3 seat per constituency)
    * Better parallelization
### Issues
  * Does not account for two party system shift.
  * Party votes distribution unrealistic. 
  * Constituency constant size.
