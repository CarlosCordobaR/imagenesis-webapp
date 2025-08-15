import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from WeabAppIMG import app

# Para Vercel
def handler(environ, start_response):
    return app(environ, start_response)

# Para otros servicios
application = app

if __name__ == "__main__":
    app.run(debug=False)
