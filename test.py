import sys
import platform as pf
sys.path.append('.\\modules')
import module

print(pf.platform())
print(pf.machine())
print(pf.processor())
print(pf.system())
print(pf.version())
print(pf.python_implementation())
for ele in pf.python_version_tuple():
    print(ele)
for i in sys.path:
    print(i)
print(module.welcome('Nishanth'))