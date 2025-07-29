def maximo(a, b):
  if a > b:
    return a
  else:
    return b

print(f"máximo(5, 6) -> Retorna: {maximo(5, 6)}, Esperado: 6")
print(f"máximo(2, 1) -> Retorna: {maximo(2, 1)}, Esperado: 2")
print(f"máximo(7, 7) -> Retorna: {maximo(7, 7)}, Esperado: 7")