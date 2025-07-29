def validar_nome_usuario(nome_entrada):
    nome_normalizado = nome_entrada.strip().lower()
    
    if not nome_normalizado:
        return False
    
    if nome_normalizado.isalnum():
        return True
    else:
        return False

print(f"' Usuario123 ' -> {validar_nome_usuario(' Usuario123 ')}")
print(f"'user_name' -> {validar_nome_usuario('user_name')}")
print(f"'apenasletras' -> {validar_nome_usuario('apenasletras')}")
print(f"'12345' -> {validar_nome_usuario('12345')}")
print(f"' ' -> {validar_nome_usuario(' ')}")
print(f"'Com Espaços' -> {validar_nome_usuario('Com Espaços')}")
