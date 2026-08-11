import re

with open('lovetap.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Eliminar líneas en blanco múltiples (más de 2 consecutivas)
content = re.sub(r'\n{3,}', '\n\n', content)

# 2. Reemplazar las clases frame-* individuales con una solución basada en data-frame
# Definir el mapeo de colores para frames
frame_colors = {
    'gold': ('var(--gold)', 'rgba(242,193,78,0.5)'),
    'pink': ('var(--accent)', 'rgba(255,46,136,0.45)'),
    'teal': ('var(--teal)', 'rgba(62,198,168,0.4)'),
    'fire': ('#FF7A3C', 'rgba(255,122,60,0.55)'),
    'silver': ('#CFD8DC', 'rgba(207,216,220,0.4)'),
    'none': ('rgba(255,255,255,0.15)', '')
}

# Crear la nueva regla CSS unificada usando data-frame
new_frame_rule = """.frame{box-shadow:0 0 0 4px var(--frame-color, rgba(255,255,255,0.15)), 0 0 20px var(--frame-glow, transparent);}
.frame[data-frame="gold"]{--frame-color:var(--gold);--frame-glow:rgba(242,193,78,0.5);}
.frame[data-frame="pink"]{--frame-color:var(--accent);--frame-glow:rgba(255,46,136,0.45);}
.frame[data-frame="teal"]{--frame-color:var(--teal);--frame-glow:rgba(62,198,168,0.4);}
.frame[data-frame="fire"]{--frame-color:#FF7A3C;--frame-glow:rgba(255,122,60,0.55);}
.frame[data-frame="silver"]{--frame-color:#CFD8DC;--frame-glow:rgba(207,216,220,0.4);}
.frame[data-frame="none"]{--frame-color:rgba(255,255,255,0.15);--frame-glow:transparent;}"""

# Eliminar las viejas reglas frame-*
content = re.sub(r'\.frame-gold\{[^}]+\}\n', '', content)
content = re.sub(r'\.frame-pink\{[^}]+\}\n', '', content)
content = re.sub(r'\.frame-teal\{[^}]+\}\n', '', content)
content = re.sub(r'\.frame-fire\{[^}]+\}\n', '', content)
content = re.sub(r'\.frame-silver\{[^}]+\}\n', '', content)
content = re.sub(r'\.frame-none\{[^}]+\}\n', '', content)

# Insertar la nueva regla después de .avatar-placeholder
content = content.replace(
    '.avatar-placeholder{width:96px;height:96px;border-radius:50%;background:var(--bg-2);display:flex;align-items:center;justify-content:center;font-size:32px;color:var(--text-faint);}',
    '.avatar-placeholder{width:96px;height:96px;border-radius:50%;background:var(--bg-2);display:flex;align-items:center;justify-content:center;font-size:32px;color:var(--text-faint);}\n' + new_frame_rule
)

with open('lovetap.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS optimizado exitosamente")
