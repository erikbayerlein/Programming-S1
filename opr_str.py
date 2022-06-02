curso = "Programação em Python"

x = curso.count(" ")
y = len(curso) - x
print (y)

print ("prog" in curso)
print ("i" in curso)
print ("l" in curso)
print (curso.count("O"))
print (curso.count("o"))
print (curso.rfind("o"))
print (curso.find("o"))

A = curso.split()
py = A[-1]
py2 = py.lower()
py3 = sorted(py2)
print (*py3)

j = curso.replace("Python", "Java")
j_ = j.replace(" ", "_")
print (j_)