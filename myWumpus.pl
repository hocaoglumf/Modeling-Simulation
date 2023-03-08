grid(2,1,breeze).
grid(3,2,breeze).
grid(4,1,breeze).
grid(2,3,breeze).
grid(4,3,breeze).
grid(3,4,breeze).


grid(1,2,stench).
grid(1,4,stench).
grid(2,3,stench).

grid(3,1,pit).
grid(3,3,pit).
grid(4,4,pit).

grid(1,3,wumpus).
grid(2,3,gold).

grid(1,1,agent).


ancakveancak(P,Q):-call(P),call(Q).
ancakveancak(P,Q):-not(call(P)),not(call(Q)).




