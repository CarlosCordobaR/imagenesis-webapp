#!/usr/bin/env python3
"""
Punto de entrada para Render - Imagénesis
"""

from WeabAppIMG import app

# Esta es la forma correcta para Gunicorn en Render
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=False)
