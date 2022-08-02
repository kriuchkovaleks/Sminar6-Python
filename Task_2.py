
from math import pi

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

find_orbit_saquare = [(round(pi, 2)*(orbits[i])[0]*(orbits[i])[1]) for i in range(len(orbits)) if (orbits[i])[0] != (orbits[i])[1] ]


find_farthest_orbit = [orbits[i] for i in range(len(find_orbit_saquare)) if find_orbit_saquare[i] == max(find_orbit_saquare)]

print(*find_farthest_orbit)
