from astroquery.nist import Nist
from astropy import units as u

tbl = Nist.query(1370*u.AA, 1*u.AA, linename="Ni II")
print(tbl)