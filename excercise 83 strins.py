ls =("""
Chief Keef ain't no hitter, Chief Keef aint this, Chief Keef a fake
Shut the fuck up, y'all don't live with that bababooey
Y'all know that bababooey got caught with a ratchet
Shootin' at the police and shit
bababooey been on probation since fuckin' I don't know when
Motherfucker, stop fuckin' playin' him like that
""")
print(ls)
s = int(input("choose a starting point \n"))
if s < 0:
    s = int(input("choose a starting point \n"))
e = int(input("choose an ending point \n"))
if e < 0:
    e = int(input("choose an ending point \n"))
print(ls[s:e])
