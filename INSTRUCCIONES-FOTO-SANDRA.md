# 📸 Instrucciones para Foto de la Dra. Sandra Córdoba

## 🎯 **Ubicación de la Imagen**
La foto de la Dra. Sandra debe colocarse en:
```
/static/images/dra-sandra-cordoba.jpg
```

## 📋 **Especificaciones Técnicas**

### **Formato Recomendado:**
- ✅ **Formato**: JPG o PNG
- ✅ **Dimensiones**: 400x400 píxeles (mínimo)
- ✅ **Relación de aspecto**: 1:1 (cuadrada)
- ✅ **Tamaño**: Menos de 500KB
- ✅ **Calidad**: Alta resolución para web

### **Características de la Foto:**
- 📷 **Tipo**: Foto profesional médica
- 👩‍⚕️ **Vestimenta**: Bata médica o ropa profesional
- 🎨 **Fondo**: Neutro (blanco, gris claro, o consultorio médico)
- 😊 **Expresión**: Profesional y amigable
- 💡 **Iluminación**: Bien iluminada, sin sombras fuertes

## 🔄 **Pasos para Reemplazar**

### **Opción 1: Reemplazar archivo existente**
1. Renombra tu foto como: `dra-sandra-cordoba.jpg`
2. Copia el archivo a: `/static/images/`
3. Reemplaza el archivo SVG actual
4. Actualiza el código en `WeabAppIMG.py` línea 122:
   ```python
   "image_url": "/static/images/dra-sandra-cordoba.jpg",
   ```

### **Opción 2: Usar nueva imagen**
1. Sube tu foto a `/static/images/` con cualquier nombre
2. Actualiza la ruta en `WeabAppIMG.py`:
   ```python
   "image_url": "/static/images/TU_NOMBRE_DE_ARCHIVO.jpg",
   ```

## 🎨 **Imagen Actual**
Actualmente se muestra un **placeholder SVG profesional** con:
- 🏥 Colores corporativos de Imagénesis
- 👩‍⚕️ Iconografía médica (estetoscopio)
- 📋 Información básica (nombre y especialidad)

## ✨ **Efectos Visuales Aplicados**
La imagen tendrá automáticamente:
- 🔵 **Borde dorado** (color corporativo)
- 🌟 **Sombra profesional**
- ⭕ **Forma circular**
- 📱 **Responsiva** (se adapta a todos los dispositivos)

## 🔧 **Estilos CSS Aplicados**
```css
.img-fluid.rounded-circle.shadow-lg {
    border: 4px solid var(--gold-accent);
    max-width: 280px;
}
```

## 📍 **Ubicación en la Web**
La foto aparece en:
- 🏠 **Página**: "Nosotros" (`/nosotros`)
- 📱 **Sección**: Perfil de la Fundadora
- 🎯 **Posición**: Lado izquierdo, junto al texto del perfil

---

## 💡 **Consejos para la Foto**

### **Para obtener los mejores resultados:**
- 📸 **Usa una foto reciente** (últimos 2 años)
- 🎨 **Fondo neutro** para que resalte la profesionalidad
- 👔 **Vestimenta profesional** acorde al ámbito médico
- 😊 **Sonrisa natural** que transmita confianza
- 💡 **Buena iluminación** natural o profesional

### **Evita:**
- ❌ Fotos muy oscuras o con sombras
- ❌ Fondos muy distractivos o coloridos
- ❌ Imágenes pixeladas o de baja calidad
- ❌ Fotos demasiado casuales para el contexto profesional

---

**Nota**: Una vez que tengas la foto real, simplemente reemplaza el archivo y la imagen se actualizará automáticamente en la página web.

**Contacto para dudas técnicas**: El archivo SVG actual sirve perfectamente como placeholder profesional hasta que tengas la foto real.
