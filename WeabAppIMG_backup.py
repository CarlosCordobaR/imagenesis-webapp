from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Contenido centralizado para la página web de Imagénesis con iconos modernos
CONTENT = {
    "site_info": {
        "name": "Imagénesis",
        "tagline": "Donde tu salud cobra forma",
        "description": "Centro de diagnóstico por imágenes de alta precisión con enfoque humano y tecnología avanzada",
        "logo_url": "/static/images/logo-imagenesis.png",
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
            "image_url": "/static/images/hero-medical.jpg"
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
        "values": [
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
            "name": "Dra. Sandra Córdoba",
            "title": "Fundadora y Directora Médica",
            "credentials": [
                "Médica Radióloga Universidad Nacional de Colombia",
                "Especialización en Diagnóstico por Imágenes - Hospital San Juan de Dios",
                "Fellowship en Resonancia Magnética - Clínica Mayo, USA",
                "Miembro de la Sociedad Colombiana de Radiología"
            ],
            "bio": "Con más de 15 años de experiencia en radiología diagnóstica, la Dra. Córdoba ha dedicado su carrera a combinar la excelencia técnica con un enfoque humanizado en la medicina. Su visión de crear un centro que priorice tanto la precisión diagnóstica como el bienestar emocional del paciente dio origen a Imagénesis.",
            "image_url": "/static/images/dra-cordoba.jpg"
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

if __name__ == '__main__':
    app.run(debug=True)
