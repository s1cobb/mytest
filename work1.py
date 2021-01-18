import sys
import re

# missing csv module
if re.match('(3.7.5)', sys.version):
    m = re.match('(3.7.5)', sys.version)
    if m:
        print(m.group(1))
elif re.match('(2.7.18)', sys.version):
    m = re.match('(2.7.18)', sys.version)
    if m:
        print(m.group(1))
else:
    print('invalid version...')

print('im good')
print('good good')
print("will it pass lint")
print('first push 1/3')
print('second push 1/3')
print('smith')
print('on nmaster lets work 01/10')
print('')

print('save it')
print('good stuff')
if 'small' == 'small':
    print('im small')
print('ok')

sys.exit(0)
