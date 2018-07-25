# /bin/python

"""
Require fabric module -- use : 'pip install fabric'

"""

import fabric
print dir(fabric)
c = fabric.Connection('stage')
# change to root directory

res = c.run('sudo su -')
print res

