# Imagénesis - Centro de Diagnóstico por Imágenes

Una aplicación web moderna desarrollada para el centro de diagnóstico médico **Imagénesis**, fundado por la Dra. Sandra Córdoba. La plataforma combina tecnología avanzada con un enfoque humano para ofrecer servicios de diagnóstico por imágenes de alta precisión.

## 🏥 Sobre Imagénesis

**Imagénesis** es un centro de diagnóstico por imágenes que se especializa en:
- Radiología convencional
- Tomografía computarizada
- Resonancia magnética  
- Ultrasonido diagnóstico
- Diagnóstico asistido por inteligencia artificial

### 🎯 Enfoque Médico Preventivo

Nuestro enfoque se centra en la medicina preventiva, proporcionando diagnósticos tempranos y precisos que contribuyen a una mejor toma de decisiones médicas y al bienestar general de nuestros pacientes.

## 🚀 Características Principales

### 📱 Sitio Web Responsive
- Diseño moderno y responsivo usando Bootstrap 5
- Navegación intuitiva optimizada para todos los dispositivos
- Accesibilidad mejorada para usuarios con discapacidades

### 🤖 Diagnóstico Asistido por IA
- Herramienta de análisis preliminar de imágenes médicas
- Interfaz de arrastrar y soltar para subir imágenes
- Análisis en tiempo real con algoritmos de IA
- Validación médica profesional de todos los resultados

### 📅 Sistema de Reservas Online
- Formulario completo de reserva de citas
- Selección de servicios y horarios disponibles
- Validación en tiempo real de formularios
- Notificaciones automáticas por WhatsApp y email

### 📚 Centro de Educación Médica
- Sección "ABC de la Radiología" con información educativa
- Preguntas frecuentes detalladas
- Guías de preparación para estudios
- Información sobre seguridad radiológica

## 🛠 Tecnologías Utilizadas

### Backend
- **Python 3.9+**
- **Flask** - Framework web ligero y flexible
- **Jinja2** - Motor de plantillas
- **Werkzeug** - Utilidades WSGI

### Frontend
- **HTML5** semántico y accesible
- **CSS3** con variables personalizadas y animaciones
- **JavaScript ES6+** modular y optimizado
- **Bootstrap 5** - Framework CSS responsivo
- **Font Awesome** - Iconografía profesional

### Características Adicionales
- **Progressive Web App (PWA)** ready
- **SEO optimizado** con meta tags apropiados
- **Integración con WhatsApp** para comunicación directa
- **Google Analytics** ready para tracking
- **Accesibilidad WCAG 2.1** compliant

## 📁 Estructura del Proyecto

```
webappimg/
├── WeabAppIMG.py              # Aplicación principal Flask
├── requirements.txt           # Dependencias de Python
├── .env                      # Variables de entorno
├── templates/                # Plantillas HTML
│   ├── base.html            # Plantilla base
│   ├── inicio.html          # Página de inicio
│   ├── nosotros.html        # Página sobre nosotros
│   ├── servicios.html       # Página de servicios
│   ├── abc_radiologia.html  # Guía educativa
│   ├── diagnostico_ai.html  # Herramienta de IA
│   ├── contacto.html        # Página de contacto
│   └── reserva_cita.html    # Sistema de reservas
├── static/                  # Archivos estáticos
│   ├── css/
│   │   └── style.css       # Estilos personalizados
│   ├── js/
│   │   └── main.js         # JavaScript principal
│   └── images/             # Imágenes del sitio
└── README.md               # Este archivo
```

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.9 o superior
- pip (administrador de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd /ruta/a/tu/proyecto/webappimg
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En macOS/Linux
   # o
   .venv\Scripts\activate     # En Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   cp .env.example .env  # Si existe
   # Editar .env con tus configuraciones
   ```

5. **Ejecutar la aplicación**
   ```bash
   python WeabAppIMG.py
   ```

6. **Acceder a la aplicación**
   Abre tu navegador en: `http://localhost:5000`

## 📋 Funcionalidades por Sección

### 🏠 Página de Inicio
- Hero section con call-to-action principal
- Estadísticas animadas del centro médico
- Características principales destacadas
- Testimonios de pacientes
- Previsualización de servicios

### 👥 Nosotros
- Historia y misión de Imagénesis
- Perfil de la Dra. Sandra Córdoba
- Valores corporativos
- Información del equipo médico

### 🔬 Servicios
- Catálogo completo de estudios disponibles
- Información detallada de cada procedimiento
- Tiempos de duración y preparación
- Programas preventivos especiales

### 📖 ABC de la Radiología
- Guía educativa para pacientes
- Preguntas frecuentes detalladas
- Instrucciones de preparación
- Información sobre seguridad radiológica

### 🤖 Diagnóstico IA
- Herramienta interactiva de análisis
- Subida de imágenes médicas
- Análisis preliminar automatizado
- Recomendaciones de seguimiento

### 📞 Contacto
- Información completa de contacto
- Formulario de contacto validado
- Horarios de atención detallados
- Integración con redes sociales

### 📅 Reserva de Citas
- Formulario completo de reserva
- Selección de servicios médicos
- Información médica relevante
- Confirmación automática

## 🎨 Personalización

### Colores Corporativos
El sitio utiliza una paleta de colores médica profesional definida en `static/css/style.css`:

```css
:root {
    --primary-color: #2563eb;    /* Azul médico principal */
    --secondary-color: #1e40af;  /* Azul oscuro */
    --accent-color: #3b82f6;     /* Azul claro */
    --success-color: #10b981;    /* Verde éxito */
    --warning-color: #f59e0b;    /* Amarillo advertencia */
    --danger-color: #ef4444;     /* Rojo peligro */
}
```

### Contenido Editable
Todo el contenido está centralizado en el diccionario `CONTENT` en `WeabAppIMG.py`, facilitando la edición sin tocar las plantillas HTML.

## 🔒 Seguridad y Privacidad

- Validación de formularios tanto en frontend como backend
- Sanitización de inputs del usuario
- Preparado para HTTPS en producción
- Cumplimiento con regulaciones de privacidad médica
- Consentimiento explícito para tratamiento de datos

## 📈 SEO y Marketing Digital

### Optimización SEO
- Meta tags optimizados para cada página
- Estructura semántica HTML5
- URLs amigables para buscadores
- Contenido optimizado para palabras clave médicas

### Marketing Digital
- Integración con Google Analytics (configurar GA4)
- Botón flotante de WhatsApp para conversión
- Call-to-actions estratégicamente ubicados
- Landing pages optimizadas para conversión

## 🚀 Despliegue en Producción

### Recomendaciones de Hosting
1. **VPS o Cloud**: DigitalOcean, AWS, Google Cloud
2. **Shared Hosting**: Que soporte Python/Flask
3. **Platform as a Service**: Heroku, PythonAnywhere

### Configuración de Producción
```bash
# Instalar servidor WSGI
pip install gunicorn

# Ejecutar en producción
gunicorn -w 4 -b 0.0.0.0:8000 WeabAppIMG:app
```

### Variables de Entorno de Producción
```env
FLASK_ENV=production
SECRET_KEY=tu-clave-secreta-segura
DATABASE_URL=postgresql://usuario:password@host:puerto/basedatos
```

## 🤝 Sugerencias para Desarrollo Futuro

### Funcionalidades Avanzadas
1. **Sistema de Citas Completo**
   - Base de datos para gestión de citas
   - Panel administrativo para médicos
   - Notificaciones automáticas por SMS/Email
   - Integración con calendarios médicos

2. **Portal del Paciente**
   - Registro y login de usuarios
   - Historial médico digital
   - Descarga de resultados
   - Seguimiento de estudios

3. **IA Diagnóstica Avanzada**
   - Integración con APIs de diagnóstico médico
   - Procesamiento de imágenes DICOM
   - Machine learning para detección temprana
   - Validación por especialistas en línea

4. **Telemedicina**
   - Consultas virtuales
   - Interpretación remota de estudios
   - Segunda opinión médica
   - Seguimiento post-diagnóstico

### Integraciones Recomendadas
- **Sistema de Pagos**: Stripe, PayU, PayPal
- **CRM Médico**: Integración con software hospitalario
- **ERP**: Gestión de inventario y equipos
- **Business Intelligence**: Dashboard de métricas médicas

## 📞 Contacto y Soporte

Para consultas técnicas o mejoras al sistema:

- **Email**: desarrollo@imagenesis.co
- **WhatsApp**: +57 300 123 4567
- **Documentación**: Este README y comentarios en código

## 📄 Licencia

Este proyecto está desarrollado específicamente para **Imagénesis** y contiene contenido médico especializado. Todos los derechos reservados.

---

### 🏥 Imagénesis - Donde la Precisión se Encuentra con la Humanidad

*Desarrollado con ❤️ para mejorar la atención médica diagnóstica*
