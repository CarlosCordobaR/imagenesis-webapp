#!/usr/bin/env python3
"""
Aplicación principal para Imagénesis - Centro de Diagnóstico por Imágenes
Configurada para despliegue en Render.com
"""

import os
from WeabAppIMG import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=False)
