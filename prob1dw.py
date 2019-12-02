import pandas as pd

A = {'Student' : ['Ice Bear', 'Panda', 'Grizzly'],'Math' : [80, 95, 79]}

B = {'Student' : ['Ice Bear', 'Panda', 'Grizzly'],'Electronics' : [85, 81, 83]}

C = {'Student' : ['Ice Bear', 'Panda', 'Grizzly'],'GEAS' : [90, 79, 93]}

D = {'Student' : ['Ice Bear', 'Panda', 'Grizzly'],'ESAT' : [93, 89, 88]}

a = pd.DataFrame(A, columns = ['Student', 'Math'])
b = pd.DataFrame(B, columns = ['Student', 'Electronics'])
c = pd.DataFrame(C, columns = ['Student', 'GEAS'])
d = pd.DataFrame(D, columns = ['Student', 'ESAT'])

e = pd.merge(a, b, how = 'left', on = 'Student')
f = pd.merge(c, d, how = 'left', on = 'Student')
g = pd.merge(e, f, how = 'left', on = 'Student')

tidy_g = pd.melt(g, id_vars = 'Student', value_vars = ['Math', 'Electronics', 'GEAS', 'ESAT'])

x = tidy_g.rename(columns = {'variable': 'Subjects', 'value' : 'Grades'})
y = x.sort_values('Student')
z = y.reset_index()

final = z.drop(columns = 'index', axis = 1)