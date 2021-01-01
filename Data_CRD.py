import crd as create
import time
create.create('Alex',85,10,1)
create.create('Jonas',7)
create.create('Smith',10)
create.read('Jonas')
create.destroy('Smith')
time.sleep(10)
create.read('Alex')