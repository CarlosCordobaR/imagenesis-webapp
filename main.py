import os
import logging
from WeabAppIMG import app

# Configuración para producción
app.config['DEBUG'] = False
app.config['TESTING'] = False

# Configurar logging para producción
if not app.debug:
    logging.basicConfig(level=logging.INFO)

# Esta variable es lo que Gunicorn importará
application = app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
