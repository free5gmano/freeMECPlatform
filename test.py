import ast
a = ["1", "f", "343"]
b = str(a)
x = ast.literal_eval(b)
print(x)