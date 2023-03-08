
friend(ayse,ahmet).
likes(ahmet,ayse).
friend(ayca,veli).

happy(X):-friend(X,Y),likes(Y,X). 