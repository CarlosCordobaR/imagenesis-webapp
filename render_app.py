#!/usr/bin/env python3
"""
Configuración optimizada para Render Free Tier
"""
import os
from WeabAppIMG import app

# Configuración específica para la capa gratuita
app.config.update(
    SECRET_KEY=os.environ.get('SECRET_KEY', 'imagenesis_secret_key_2025'),
    MAX_CONTENT_LENGTH=16 * 1024 * 1024,  # 16MB para la capa gratuita
)

# Variable que Gunicorn buscará
application = app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
