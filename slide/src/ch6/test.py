import sys,io

out = io.StringIO()
out.write('hello')
s = out.getvalue()
sys.stdout = out
print('ok')
sys.stdout = sys.__stdout__
print(out.getvalue())
