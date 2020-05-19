# Virtual Classroom

### kill a running session
run(tested on macOS)
```
ps -ef | grep manage.py | awk '{print $2}'| xargs kill 
```


### create dummy users
1. run django shell. 
```
python manage.py shell
```
2. run 
```
from createuser import createObjects
createObjects()
```