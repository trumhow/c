import os

print(os.path.abspath('.'))
print(os.path.join('/Users/', 'python/'))


from pathlib import Path

p = Path('.')
print(p.resolve())
print(p.is_dir())

q = Path('tmp/a/b/c')
Path.mkdir(q, parents=True)
