# 🏥 Imagénesis - Despliegue en Render Free Tier

## 📋 Configuración para Render

### Archivos importantes para el despliegue:
- `render_app.py` - Punto de entrada optimizado para Render
- `Procfile` - Configuración de Gunicorn
- `runtime.txt` - Python 3.9.18
- `requirements.txt` - Dependencias mínimas
- `build.sh` - Script de construcción

### 🚀 Configuración en Render Dashboard:

1. **Build Command**: `./build.sh`
2. **Start Command**: `gunicorn render_app:application --bind 0.0.0.0:$PORT --workers 1 --timeout 60`
3. **Environment**: `Python 3`
4. **Plan**: `Free`

### 🔧 Variables de entorno recomendadas:
```
PYTHON_VERSION=3.9.18
WEB_CONCURRENCY=1
```

### ⚠️ Limitaciones de la capa gratuita:
- Los servicios se pausan después de 15 minutos de inactividad
- Tiempo de arranque puede ser de 30-60 segundos
- No soporta SSH, escalado, o discos persistentes
- Limitación de memoria y CPU

### ✅ Características incluidas:
- Aplicación Flask optimizada
- Configuración de Gunicorn para recursos limitados
- Manejo de archivos estáticos
- Sistema de citas online
- Visor de imágenes médicas
- Diagnóstico asistido por IA

---
**Nota**: Para mejor rendimiento y funcionalidades avanzadas, considera upgrading a un plan pagado de Render.
