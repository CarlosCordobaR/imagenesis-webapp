#!/usr/bin/env python3
"""
Aplicación principal para Render
"""
import os
from WeabAppIMG import app

# Variable que Gunicorn usará
application = app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
