from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import json
import os
import uuid
from datetime import datetime
from werkzeug.utils import secure_filename
import base64

app = Flask(__name__)
app.secret_key = 'imagenesis_secret_key_2025'

# Configuración para subida de archivos
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'webp', 'dcm', 'dicom'}
MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Crear directorio de uploads si no existe
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Contenido centralizado para la página web de Imagénesis con iconos modernos
CONTENT = {
    "site_info": {
        "name": "Imagénesis",
        "tagline": "Donde tu salud cobra forma",
        "description": "Centro de diagnóstico por imágenes de alta precisión con enfoque humano y tecnología avanzada",
        "logo_url": "/static/images/LogoImagenesis_2025_w.png",
        "phone": "+57 (1) 234-5678",
        "email": "info@imagenesis.co",
        "address": "Carrera 15 #93-47, Bogotá, Colombia",
        "whatsapp": "+57 300 123 4567"
    },
    
    "inicio": {
        "hero": {
            "title": "Bienvenidos a Imagénesis",
            "subtitle": "Donde la Precisión se Encuentra con la Humanidad",
            "description": "Centro de diagnóstico por imágenes de última generación, fundado por la Dra. Sandra Córdoba. Combinamos tecnología avanzada con un trato cálido y profesional para brindar resultados confiables que contribuyan a tu bienestar.",
            "cta_primary": "Reserva tu Cita",
            "cta_secondary": "Conoce Nuestros Servicios",
            "image_url": "/static/images/radiologia.jpg"
        },
        "features": [
            {
                "icon": "🏥",
                "title": "Tecnología de Vanguardia",
                "description": "Equipos de última generación para diagnósticos precisos y detallados."
            },
            {
                "icon": "⚡",
                "title": "Resultados Rápidos",
                "description": "Entrega de resultados en tiempo récord sin comprometer la calidad."
            },
            {
                "icon": "🩺",
                "title": "Atención Humanizada",
                "description": "Cada paciente recibe un trato personalizado y empático."
            },
            {
                "icon": "🔬",
                "title": "Excelencia Médica",
                "description": "Dirigido por especialistas con amplia experiencia en diagnóstico por imágenes."
            }
        ],
        "stats": [
            {"number": "10,000+", "label": "Estudios Realizados"},
            {"number": "98%", "label": "Satisfacción del Paciente"},
            {"number": "15+", "label": "Años de Experiencia"},
            {"number": "24/7", "label": "Atención de Emergencias"}
        ],
        "testimonials": [
            {
                "name": "María González",
                "text": "La atención fue excepcional. La Dra. Córdoba me explicó todo el proceso y los resultados fueron entregados el mismo día.",
                "rating": 5
            },
            {
                "name": "Carlos Rodríguez",
                "text": "Instalaciones modernas y personal muy profesional. Me sentí en confianza durante todo el proceso.",
                "rating": 5
            }
        ]
    },
    
    "nosotros": {
        "mission": {
            "title": "Nuestra Misión",
            "text": "Brindar servicios de diagnóstico por imágenes de la más alta calidad, combinando tecnología avanzada con un enfoque humano, para contribuir a la salud preventiva y el bienestar de nuestros pacientes."
        },
        "vision": {
            "title": "Nuestra Visión",
            "text": "Ser el centro de diagnóstico por imágenes líder en Colombia, reconocido por su excelencia técnica, innovación constante y compromiso con la salud preventiva de la comunidad."
        },
        "core_values": [
            {
                "title": "Precisión",
                "description": "Cada estudio se realiza con el máximo rigor técnico y científico."
            },
            {
                "title": "Humanidad",
                "description": "Tratamos a cada paciente con calidez, respeto y comprensión."
            },
            {
                "title": "Innovación",
                "description": "Incorporamos continuamente las últimas tecnologías médicas."
            },
            {
                "title": "Ética",
                "description": "Actuamos con transparencia e integridad en todos nuestros procesos."
            }
        ],
        "founder": {
            "name": "Dra. Sandra Córdoba Rovira",
            "title": "Fundadora y Directora Médica",
            "current_position": "Jefa del Área Clínica de Diagnóstico por la Imagen - Hospital de Dénia",
            "credentials": [
                "Licenciada en Medicina y Cirugía - Universidad del Rosario, Bogotá",
                "Especialista en Radiodiagnóstico vía MIR - Hospital Universitari Joan XXIII, Tarragona",
                "Clinical Fellow MSK - King's College Hospital NHS Foundation, Londres",
                "Experto Universitario en Ecografía Músculo-esquelética - Universidad Francisco de Vitoria",
                "Miembro de SERAM, ESR, SERME y Sociedad de Radiología de la Comunidad Valenciana"
            ],
            "specializations": [
                "Radiodiagnóstico con énfasis en Cabeza-Cuello",
                "Diagnóstico Músculo-esquelético",
                "Ecografía Musculo-esquelética",
                "Resonancia Magnética Avanzada"
            ],
            "experience_years": "15+",
            "international_experience": {
                "spain": "13 años - Actualmente Jefa del Área Clínica en Hospital de Dénia",
                "uk": "Clinical Fellowship en King's College Hospital, Londres (2024)",
                "colombia": "Formación médica inicial y Servicio Social"
            },
            "bio": "La Dra. Sandra Córdoba Rovira aporta una excepcional combinación de formación internacional y experiencia clínica de más de 15 años en radiodiagnóstico. Graduada en Medicina por la Universidad del Rosario en Bogotá, desarrolló su especialización en España a través del prestigioso programa MIR en el Hospital Universitari Joan XXIII de Tarragona. Su trayectoria profesional en el sistema sanitario español incluye más de 7 años como Facultativa Especialista, actualmente ejerciendo como Jefa del Área Clínica de Diagnóstico por la Imagen en el Hospital de Dénia. Recientemente completó un Clinical Fellowship en el King's College Hospital de Londres, consolidando su expertise en diagnóstico músculo-esquelético avanzado. Su compromiso con la excelencia médica se refleja en su activa participación en sociedades científicas internacionales, publicaciones en revistas especializadas y su destacada labor docente como tutora en universidades españolas.",
            "image_url": "/static/images/2025-06-29_152751-.jpeg",
            "achievements": [
                "Jefa del Área Clínica de Diagnóstico por la Imagen - Hospital de Dénia (Actual)",
                "Clinical Fellowship en King's College Hospital, Londres (2024)",
                "13 años de experiencia en el sistema sanitario español",
                "Miembro de comités de tumores y correlación clínico-patológica",
                "Publicaciones en revistas internacionales de radiología",
                "Tutora universitaria en grado de Medicina",
                "Premio de investigación en pregrado Universidad del Rosario"
            ],
            "education_highlights": [
                "Formación MIR en Hospital Universitari Joan XXIII (2012-2016)",
                "Clinical Fellowship en King's College Hospital, Londres (2024)",
                "Experto Universitario en Ecografía Músculo-esquelética",
                "Participación en congresos internacionales (RSNA, ECR, SERAM)"
            ]
        },
        "team": [
            {
                "name": "Dr. Miguel Hernández",
                "position": "Radiólogo Senior",
                "specialization": "Tomografía Computarizada"
            },
            {
                "name": "Dra. Ana Martínez",
                "position": "Especialista en Resonancia Magnética",
                "specialization": "Neuroimágenes"
            },
            {
                "name": "Lic. Patricia Vásquez",
                "position": "Tecnóloga en Radiología",
                "specialization": "Ultrasonido Diagnóstico"
            }
        ]
    },
    
    "servicios": {
        "intro": {
            "title": "Nuestros Servicios",
            "subtitle": "Diagnóstico Integral con Tecnología de Punta",
            "description": "Ofrecemos una amplia gama de estudios diagnósticos con equipos de última generación y un enfoque preventivo que priioriza tu salud."
        },
        "categories": [
            {
                "name": "Radiología Convencional",
                "icon": "🦴",
                "services": [
                    {
                        "name": "Radiografías Digitales",
                        "description": "Estudios de tórax, abdomen, extremidades con menor radiación y mayor nitidez.",
                        "duration": "10-15 min",
                        "preparation": "No requiere preparación especial"
                    },
                    {
                        "name": "Fluoroscopia",
                        "description": "Estudios dinámicos del tracto digestivo y genitourinario.",
                        "duration": "30-45 min",
                        "preparation": "Ayuno de 8 horas"
                    }
                ]
            },
            {
                "name": "Tomografía Computarizada",
                "icon": "🔬",
                "services": [
                    {
                        "name": "TC Simple y Contrastada",
                        "description": "Diagnóstico preciso de órganos internos, huesos y tejidos blandos.",
                        "duration": "15-30 min",
                        "preparation": "Ayuno 4 horas para estudios con contraste"
                    },
                    {
                        "name": "TC Cardiaca",
                        "description": "Evaluación no invasiva de arterias coronarias y función cardiaca.",
                        "duration": "20-30 min",
                        "preparation": "Evitar cafeína 12 horas antes"
                    }
                ]
            },
            {
                "name": "Resonancia Magnética",
                "icon": "🧠",
                "services": [
                    {
                        "name": "RM Cerebral",
                        "description": "Estudio detallado del cerebro y estructuras neurológicas.",
                        "duration": "45-60 min",
                        "preparation": "Retirar objetos metálicos"
                    },
                    {
                        "name": "RM Musculoesquelética",
                        "description": "Evaluación de articulaciones, músculos y huesos.",
                        "duration": "30-45 min",
                        "preparation": "Ropa cómoda sin metales"
                    }
                ]
            },
            {
                "name": "Ultrasonido",
                "icon": "📡",
                "services": [
                    {
                        "name": "Ecografía Abdominal",
                        "description": "Evaluación de órganos abdominales de forma no invasiva.",
                        "duration": "20-30 min",
                        "preparation": "Ayuno de 6 horas"
                    },
                    {
                        "name": "Ecocardiograma",
                        "description": "Estudio funcional del corazón y grandes vasos.",
                        "duration": "30-40 min",
                        "preparation": "No requiere preparación"
                    }
                ]
            }
        ],
        "special_programs": [
            {
                "name": "Chequeo Preventivo Integral",
                "description": "Programa diseñado para detectar precozmente alteraciones antes de que se conviertan en problemas de salud.",
                "includes": ["Radiografía de tórax", "Ecografía abdominal", "Densitometría ósea", "Consulta médica"],
                "target": "Adultos mayores de 40 años"
            },
            {
                "name": "Programa Mujer Saludable",
                "description": "Enfoque preventivo especializado en la salud femenina.",
                "includes": ["Mamografía digital", "Ecografía pélvica", "Densitometría ósea"],
                "target": "Mujeres mayores de 35 años"
            }
        ]
    },
    
    "abc_radiologia": {
        "title": "ABC de la Radiología",
        "subtitle": "Tu Guía Completa sobre Diagnóstico por Imágenes",
        "intro": "Queremos que entiendas cada aspecto de tu estudio médico. Aquí encontrarás información clara y comprensible sobre los diferentes tipos de estudios radiológicos.",
        "sections": [
            {
                "title": "¿Qué es la Radiología?",
                "content": "La radiología es una especialidad médica que utiliza diferentes tipos de energía (rayos X, ondas sonoras, campos magnéticos) para crear imágenes del interior del cuerpo humano. Estas imágenes nos permiten diagnosticar enfermedades, evaluar lesiones y monitorear tratamientos.",
                "icon": "📚"
            },
            {
                "title": "Preparación para Estudios",
                "content": "Cada tipo de estudio puede requerir una preparación específica. Algunos necesitan ayuno, otros requieren que uses ropa sin metales, y algunos pueden necesitar medicación previa. Siempre te informaremos detalladamente sobre cómo prepararte.",
                "icon": "📋"
            },
            {
                "title": "¿Los Rayos X son Seguros?",
                "content": "Los estudios radiológicos utilizan dosis muy bajas de radiación, cuidadosamente calculadas para obtener la información necesaria con el mínimo riesgo. Los beneficios diagnósticos superan ampliamente los riesgos mínimos asociados.",
                "icon": "🛡️"
            },
            {
                "title": "Interpretación de Resultados",
                "content": "Nuestros radiólogos especializados analizan cada imagen con detalle. Los resultados se entregan con un informe claro y comprensible, y siempre estamos disponibles para resolver tus dudas.",
                "icon": "📊"
            }
        ],
        "faqs": [
            {
                "question": "¿Cuánto tiempo toman los resultados?",
                "answer": "Los resultados están disponibles entre 2 a 24 horas dependiendo del tipo de estudio. Los casos urgentes se priorizan y pueden estar listos en menos tiempo."
            },
            {
                "question": "¿Puedo comer antes del estudio?",
                "answer": "Depende del tipo de estudio. Te informaremos específicamente sobre las instrucciones de preparación al momento de agendar tu cita."
            },
            {
                "question": "¿Qué debo hacer si tengo claustrofobia?",
                "answer": "Contamos con protocolos especiales para pacientes con claustrofobia, incluyendo técnicas de relajación y, si es necesario, sedación leve previa consulta médica."
            },
            {
                "question": "¿Los estudios con contraste son seguros?",
                "answer": "Sí, utilizamos contrastes de última generación con muy baja incidencia de reacciones. Siempre evaluamos tu historial médico antes de administrar cualquier contraste."
            }
        ]
    },
    
    "diagnostico_ai": {
        "title": "Diagnóstico Asistido por IA",
        "subtitle": "Inteligencia Artificial al Servicio de tu Salud",
        "description": "Nuestra plataforma de diagnóstico asistido combina la experiencia médica con algoritmos de inteligencia artificial para ofrecer análisis preliminares rápidos y precisos.",
        "features": [
            {
                "title": "Análisis Inmediato",
                "description": "Obtén un análisis preliminar de tus imágenes médicas en minutos.",
                "icon": "⚡"
            },
            {
                "title": "Alta Precisión",
                "description": "Algoritmos entrenados con millones de casos clínicos reales.",
                "icon": "🎯"
            },
            {
                "title": "Supervisión Médica",
                "description": "Todos los resultados son validados por nuestros especialistas.",
                "icon": "👨‍⚕️"
            },
            {
                "title": "Detección Temprana",
                "description": "Identificación precoz de alteraciones que requieren atención.",
                "icon": "🔍"
            }
        ],
        "how_it_works": [
            {
                "step": 1,
                "title": "Subida de Imagen",
                "description": "Carga tu imagen médica de forma segura en nuestra plataforma."
            },
            {
                "step": 2,
                "title": "Análisis por IA",
                "description": "Nuestros algoritmos analizan la imagen en tiempo real."
            },
            {
                "step": 3,
                "title": "Reporte Preliminar",
                "description": "Recibe un análisis preliminar detallado y comprensible."
            },
            {
                "step": 4,
                "title": "Validación Médica",
                "description": "Un especialista revisa y valida los hallazgos de la IA."
            }
        ],
        "disclaimer": "⚠️ IMPORTANTE: Este es un análisis preliminar con fines educativos y de apoyo diagnóstico. No reemplaza la evaluación médica profesional. Siempre consulta con un médico especialista para obtener un diagnóstico definitivo y recomendaciones de tratamiento."
    },
    
    "contacto": {
        "title": "Contáctanos",
        "subtitle": "Estamos Aquí para Ayudarte",
        "info": {
            "address": {
                "title": "Dirección",
                "value": "Carrera 15 #93-47, Chapinero\nBogotá, Colombia",
                "icon": "📍"
            },
            "phone": {
                "title": "Teléfono",
                "value": "+57 (1) 234-5678",
                "icon": "📞"
            },
            "whatsapp": {
                "title": "WhatsApp",
                "value": "+57 300 123 4567",
                "icon": "💬"
            },
            "email": {
                "title": "Email",
                "value": "info@imagenesis.co",
                "icon": "✉️"
            }
        },
        "hours": {
            "title": "Horarios de Atención",
            "schedule": [
                {"day": "Lunes - Viernes", "hours": "7:00 AM - 7:00 PM"},
                {"day": "Sábados", "hours": "8:00 AM - 4:00 PM"},
                {"day": "Domingos", "hours": "9:00 AM - 1:00 PM"},
                {"day": "Emergencias", "hours": "24/7"}
            ]
        },
        "social_media": [
            {"platform": "Facebook", "url": "https://facebook.com/imagenesis", "icon": "📘"},
            {"platform": "Instagram", "url": "https://instagram.com/imagenesis", "icon": "📷"},
            {"platform": "LinkedIn", "url": "https://linkedin.com/company/imagenesis", "icon": "💼"}
        ]
    },
    
    "reserva_cita": {
        "title": "Reserva tu Cita",
        "subtitle": "Agenda tu Estudio de Forma Rápida y Sencilla",
        "steps": [
            {
                "number": 1,
                "title": "Selecciona el Servicio",
                "description": "Elige el tipo de estudio que necesitas"
            },
            {
                "number": 2,
                "title": "Escoge Fecha y Hora",
                "description": "Encuentra el horario que mejor se ajuste a ti"
            },
            {
                "number": 3,
                "title": "Confirma tus Datos",
                "description": "Completa tu información de contacto"
            },
            {
                "number": 4,
                "title": "¡Listo!",
                "description": "Recibirás confirmación y instrucciones"
            }
        ],
        "services_available": [
            "Radiografía Digital",
            "Tomografía Computarizada",
            "Resonancia Magnética",
            "Ultrasonido Diagnóstico",
            "Mamografía",
            "Densitometría Ósea",
            "Chequeo Preventivo Integral"
        ]
    }
}

# Rutas de la aplicación
@app.route('/')
def inicio():
    return render_template('inicio.html', content=CONTENT)

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html', content=CONTENT)

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', content=CONTENT)

@app.route('/abc-radiologia')
def abc_radiologia():
    return render_template('abc_radiologia.html', content=CONTENT)

@app.route('/diagnostico-ai')
def diagnostico_ai():
    return render_template('diagnostico_ai.html', content=CONTENT)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', content=CONTENT)

@app.route('/reserva-cita')
def reserva_cita():
    return render_template('reserva_cita.html', content=CONTENT)

# API para el sistema de citas
@app.route('/api/cita', methods=['POST'])
def crear_cita():
    data = request.get_json()
    # Aquí iría la lógica para guardar la cita en la base de datos
    return jsonify({"status": "success", "message": "Cita agendada exitosamente"})

# API para análisis de IA (placeholder)
@app.route('/api/diagnostico-ai', methods=['POST'])
def analizar_imagen():
    # Aquí iría la integración con el sistema de IA
    return jsonify({
        "status": "success",
        "analysis": "Análisis preliminar completado",
        "confidence": 0.85,
        "recommendations": ["Consultar con especialista", "Seguimiento en 30 días"]
    })

# Rutas para el visor de imágenes y análisis con LLM
@app.route('/visor-imagenes')
def visor_imagenes():
    return render_template('visor_imagenes.html', content=CONTENT)

@app.route('/api/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400
    
    if file and allowed_file(file.filename):
        # Generar nombre único para el archivo
        filename = str(uuid.uuid4()) + '_' + secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        try:
            file.save(filepath)
            
            # Convertir imagen a base64 para el visor
            with open(filepath, 'rb') as img_file:
                img_data = base64.b64encode(img_file.read()).decode()
            
            return jsonify({
                'success': True,
                'filename': filename,
                'filepath': f'/static/uploads/{filename}',
                'image_data': f'data:image/{filename.split(".")[-1]};base64,{img_data}',
                'message': 'Imagen subida exitosamente'
            })
        except Exception as e:
            return jsonify({'error': f'Error al guardar el archivo: {str(e)}'}), 500
    
    return jsonify({'error': 'Tipo de archivo no permitido'}), 400

@app.route('/api/analyze-image', methods=['POST'])
def analyze_image_llm():
    data = request.get_json()
    message = data.get('message', '')
    image_path = data.get('image_path', '')
    
    # Simulación de respuesta del LLM (aquí integrarías con OpenAI, Claude, etc.)
    responses = {
        'general': 'Esta imagen médica muestra estructuras anatómicas bien definidas. Se observan patrones de densidad normales en las áreas evaluadas.',
        'radiografia': 'En esta radiografía se pueden observar las estructuras óseas con buena definición. No se evidencian fracturas aparentes en el área visible.',
        'tomografia': 'La tomografía muestra cortes axiales con buen contraste. Las estructuras de tejidos blandos se visualizan adecuadamente.',
        'resonancia': 'La resonancia magnética presenta buena resolución de contraste entre diferentes tipos de tejido.',
        'que ves': 'Veo una imagen médica que parece ser un estudio radiológico. Las estructuras se ven bien definidas con buen contraste.',
        'diagnostico': 'Basado en la imagen, se observan patrones dentro de los límites normales. Se recomienda correlación clínica.',
        'analisis': 'Análisis preliminar: Imagen de buena calidad técnica. Estructuras anatómicas visibles sin alteraciones evidentes.'
    }
    
    # Determinar respuesta basada en palabras clave
    response = responses['general']
    message_lower = message.lower()
    
    for key, value in responses.items():
        if key in message_lower:
            response = value
            break
    
    return jsonify({
        'success': True,
        'response': response,
        'timestamp': datetime.now().strftime('%H:%M:%S')
    })

# Esta parte solo se ejecuta en desarrollo local
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    debug = os.environ.get("FLASK_ENV") != "production"
    app.run(host="0.0.0.0", port=port, debug=debug)
