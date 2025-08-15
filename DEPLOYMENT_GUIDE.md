# Guía de Despliegue - Imagénesis WebApp

## 📋 Resumen
Tu aplicación Flask está configurada para desplegarse en múltiples plataformas. Aquí tienes las opciones recomendadas en orden de facilidad:

## 🥇 Opción 1: Railway (RECOMENDADO)
Railway es muy amigable para aplicaciones Flask y tiene una capa gratuita generosa.

### Pasos:
1. Ve a https://railway.app/
2. Conecta tu cuenta de GitHub
3. Crea un nuevo proyecto desde GitHub
4. Selecciona el repositorio `imagenesis-webapp`
5. Railway detectará automáticamente que es una aplicación Python
6. Configuración automática con `railway.toml`
7. ¡Listo! Tu app estará en línea en ~2-3 minutos

### Archivos utilizados:
- `railway.toml`
- `requirements.txt`
- `Procfile`

## 🥈 Opción 2: Vercel (Configurado)
Bueno para aplicaciones Python/Flask con la configuración serverless.

### Pasos:
1. Ve a https://vercel.com/
2. Conecta tu cuenta de GitHub
3. Importa el repositorio `imagenesis-webapp`
4. Vercel usará automáticamente `vercel.json`
5. La aplicación estará disponible en una URL `.vercel.app`

### Archivos utilizados:
- `vercel.json`
- `api/index.py`
- `requirements.txt`

## 🥉 Opción 3: Render (Simplificado)
Tu configuración actual está ultra-simplificada para Render.

### Pasos:
1. Ve a https://render.com/
2. Conecta tu cuenta de GitHub
3. Crea un nuevo "Web Service"
4. Selecciona el repositorio `imagenesis-webapp`
5. Configuración:
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn app:application`
   - **Environment**: Python 3.9

### Archivos utilizados:
- `build.sh`
- `Procfile`
- `runtime.txt`
- `requirements.txt`

## 🎯 Opción 4: Heroku
Si tienes créditos o plan de Heroku.

### Pasos:
1. Instala Heroku CLI
2. Ejecuta:
   ```bash
   cd /Users/PhD/Documents/Imagenesis/webappimg
   heroku create imagenesis-app
   cp Procfile.heroku Procfile
   git add .
   git commit -m "Heroku deployment"
   git push heroku main
   ```

## 🔧 Estado Actual
- ✅ Aplicación funciona localmente
- ✅ Repositorio GitHub actualizado
- ✅ Configuraciones listas para todas las plataformas
- ✅ Dependencies simplificadas y estables

## 📝 Recomendación
**Prueba Railway primero** - Es la opción más estable y fácil para Flask apps.

## 🆘 Si tienes problemas
1. Revisa los logs de la plataforma
2. Verifica que todos los archivos estén en GitHub
3. Asegúrate de que la URL del repositorio sea: https://github.com/CarlosCordobaR/imagenesis-webapp
