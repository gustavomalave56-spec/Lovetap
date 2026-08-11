import re

with open('lovetap.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Reemplazar la generación de frame-swatches para usar solo data-frame en lugar de clase frame-X
old_line = '${FRAMES.map(f=>`<div class="frame-swatch frame-${f} ${d.frame===f?\'selected\':\'\'}" data-frame="${f}"></div>`).join(\'\')}'
new_line = '${FRAMES.map(f=>`<div class="frame-swatch ${d.frame===f?\'selected\':\'\'}" data-frame="${f}"></div>`).join(\'\')}'

content = content.replace(old_line, new_line)

with open('lovetap.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Swatch classes actualizadas")
