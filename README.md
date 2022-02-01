# Solitaire AI


A recursive algorithm that explores every possible move in peg solitaire.


<div align=center>
<img align="center" src="https://github.com/schulze-paul/solitaire-ai/blob/main/IMG_20220201_121047.jpg?raw=true" width = 400>
</div>




## Rules of the Game

The board consists of pegs ● and holes •. The goal of the game is to remove as many pegs as possible. 

```
     ● ● ●   
     ● ● ●  
 ● ● ● ● ● ● ●  
 ● ● ● • ● ● ●  
 ● ● ● ● ● ● ●  
     ● ● ●  
     ● ● ●  
```

A move consists of a peg jumping over an adjacent peg into a hole two positions away. The jumped peg is then removed.

```
     ● ● ●                  ● ● ●                  ● ● ●    
     ● ● ●                  ● ● ●                  ● ● ●    
 ● ● ● ● ● ● ●          ● ● ● ● ● ● ●          ● ● ● ● ● ● ●
 ● ● ● • ● 🔵 ●         ● ● ● 🔵🔴 • ●          ● ● ● 🔵 • • ●
 ● ● ● ● ● ● ●          ● ● ● ● ● ● ●          ● ● ● ● ● ● ●
     ● ● ●                  ● ● ●                  ● ● ●    
     ● ● ●                  ● ● ●                  ● ● ●    
```

The game ends when no more moves are possible.

## Algorithm

The recursive algorithm calculates every possible move for a given board state and then calculates the resulting board state for each move. 

```
1. Compute the possible moves m for a given board state b.  
2. Loop through the possible moves m:  
   a. Compute the resulting board state b.  
   b. Go to 1.
``` 

The resulting data structure is a tree where each node is a board state and each edge ist a possible move.  
This alogorithm explores every possible move and every possible board state of the game.


