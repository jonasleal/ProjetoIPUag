from datetime import *
from Entidades.LucroMes import *

data = datetime.now()
lucro = LucroMes(data, 100)
print data.date()
print lucro