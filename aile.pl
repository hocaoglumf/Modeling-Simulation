baba(ahmet, veli).
baba(ahmet,ayse).
baba(ahmet, ismet).
baba(riza, ayten).
baba(riza, ayse).
baba(mahmut, ahmet).
baba(mahmut,fadime).
baba(mahmut,fatma).
baba(mahmut, hediye).

anne(ayten, veli).
anne(ayten,ayse).
anne(ayten, ismet).
anne(hatice,ayten).
anne(hatice,ayse).

evli(riza,hatice).
evli(ahmet,ayten).


erkek(ahmet).
erkek(veli).
erkek(riza).
erkek(ismet).
erkek(mahmut).
kiz(ayse).
kiz(ayten).
kiz(fadime).
kiz(hatice).
kiz(fatma).
kiz(hediye).

ogul(X,Y):-baba(Y,X),erkek(X).
kizevlat(X,Y):-baba(Y,X),kiz(X).
kizevlat(X,Y):-anne(Y,X),kiz(X).


kardes(X,Y):-baba(Z,X),baba(Z,Y).
kardes(X,Y):-anne(Z,X),anne(Z,Y).

kizKardes(X,Y):-kardes(X,Y), kiz(X).
erkekKardes(X,Y):-kardes(X,Y),erkek(X).


% X Y'nin görümcesidir.
%gorumce(X,Y):-kiz(X),kiz(Y),evli(Z,Y), erkek(Z), kardes(Z,X). 

gorumce(X,Y):-evli(Z,Y), kizKardes(X,Z).

teyze(X,Y):-kizKardes(X,Z), anne(Z,Y).
hala(X,Y):-kiz(X), baba(Y,Z), kizKardes(X,Z).
