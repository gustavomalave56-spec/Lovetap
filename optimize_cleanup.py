import re

with open('lovetap.html', 'r', encoding='utf-8') as f:
    content = f.read()

original_lines = content.count('\n')

# Eliminar líneas en blanco múltiples (más de 2 consecutivas)
content = re.sub(r'\n{3,}', '\n\n', content)

new_lines = content.count('\n')
print(f"Líneas eliminadas por espacios en blanco: {original_lines - new_lines}")

with open('lovetap.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Limpieza completada")
