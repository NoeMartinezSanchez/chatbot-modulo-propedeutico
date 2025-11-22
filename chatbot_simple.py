from flask import Flask, render_template, request, jsonify
import json
import re

app = Flask(__name__)

# Base de conocimiento mejorada para el módulo propedéutico
# Se necesita aumentar
KNOWLEDGE_BASE = {
    "modulo_propedeutico": {
        "presentacion": "El módulo propedéutico es tu preparación inicial de 4 semanas antes de comenzar la prepa en línea. Te ayuda a desarrollar habilidades para el éxito académico.",
        "objetivos": [
            "Fortalecer tus habilidades de estudio",
            "Familiarizarte con la plataforma virtual", 
            "Desarrollar técnicas de organización del tiempo",
            "Practicar la comunicación en línea"
        ],
        "duracion": "4 semanas",
        "contenido": [
            "Técnicas de estudio efectivas",
            "Manejo de plataforma educativa",
            "Comunicación asertiva", 
            "Organización del tiempo",
            "Introducción a materias básicas"
        ]
    },
    "tecnicas_estudio": {
        "pomodoro": "🍅 **Técnica Pomodoro**: Estudia 25 minutos, descansa 5 minutos. Después de 4 ciclos, toma un descanso de 15-30 minutos.",
        "mapas_mentales": "🧠 **Mapas Mentales**: Organiza ideas visualmente con conceptos centrales y ramificaciones. Usa colores e imágenes.",
        "resumenes": "📝 **Resúmenes**: Sintetiza información con tus propias palabras. Destaca ideas principales y conceptos clave.",
        "repaso_espaciado": "⏰ **Repaso Espaciado**: Repasa el material en intervalos crecientes (1 día, 3 días, 1 semana, 2 semanas)."
    },
    "plataforma": {
        "acceso": "🔑 **Acceso**: Ingresa a la plataforma con tu matrícula y contraseña en el portal oficial de Prepa en Línea SEP.",
        "navegacion": "💻 **Navegación**: En el dashboard encontrarás tus materias. Cada módulo tiene: materiales, foros y actividades.",
        "foros": "💬 **Foros**: Participa activamente. Son espacios para discutir temas y forman parte de tu evaluación.",
        "problemas": "🛠️ **Problemas técnicos**: Contacta al soporte en: soporte@prepaenlinea.sep.gob.mx"
    },
    "organizacion": {
        "horario": "⏳ **Horario recomendado**: Dedica al menos 2 horas diarias al estudio. Crea una rutina consistente.",
        "planificacion": "📅 **Planificación**: Usa una agenda digital o física. Planifica tu semana cada domingo.",
        "metas": "🎯 **Metas**: Establece objetivos específicos, medibles y alcanzables para cada sesión de estudio."
    },
    "evaluacion": {
        "criterios": "La evaluación incluye: participación en foros (30%), actividades prácticas (40%) y proyecto final (30%).",
        "proyecto_final": "El proyecto final integra todos los aprendizajes del módulo. Es práctico y aplicado.",
        "aprobacion": "Para aprobar necesitas un mínimo de 8.0 de calificación y 80% de asistencia en foros."
    }
}

def get_chatbot_response(user_input):
    """Lógica simple de respuestas sin modelos complejos"""
    user_input = user_input.lower().strip()
    
    # Detección de intenciones simples
    if any(word in user_input for word in ['hola', 'buenos', 'saludos', 'hi']):
        return "¡Hola! 🤗 Soy tu asistente del Módulo Propedéutico. ¿En qué puedo ayudarte hoy?"
    
    elif any(word in user_input for word in ['qué es', 'módulo propedéutico', 'propedéutico']):
        return f"📖 {KNOWLEDGE_BASE['modulo_propedeutico']['presentacion']}"
    
    elif any(word in user_input for word in ['objetivo', 'meta', 'propósito']):
        objetivos = "\n".join([f"• {obj}" for obj in KNOWLEDGE_BASE['modulo_propedeutico']['objetivos']])
        return f"🎯 **Objetivos del módulo:**\n{objetivos}"
    
    elif any(word in user_input for word in ['contenido', 'temas', 'aprender']):
        temas = "\n".join([f"• {tema}" for tema in KNOWLEDGE_BASE['modulo_propedeutico']['contenido']])
        return f"📚 **Temas del módulo:**\n{temas}"
    
    elif any(word in user_input for word in ['técnica', 'estudio', 'aprender', 'pomodoro']):
        return "📝 **Técnicas de estudio disponibles:**\n• Pomodoro\n• Mapas mentales\n• Resúmenes\n• Repaso espaciado\n\n¿Sobre cuál quieres más información?"
    
    elif 'pomodoro' in user_input:
        return KNOWLEDGE_BASE['tecnicas_estudio']['pomodoro']
    
    elif 'mapa mental' in user_input:
        return KNOWLEDGE_BASE['tecnicas_estudio']['mapas_mentales']
    
    elif any(word in user_input for word in ['plataforma', 'acceder', 'entrar', 'login']):
        return KNOWLEDGE_BASE['plataforma']['acceso']
    
    elif any(word in user_input for word in ['foro', 'participar', 'discusión']):
        return KNOWLEDGE_BASE['plataforma']['foros']
    
    elif any(word in user_input for word in ['soporte', 'ayuda', 'problema', 'técnico']):
        return KNOWLEDGE_BASE['plataforma']['problemas']
    
    elif any(word in user_input for word in ['organización', 'tiempo', 'horario']):
        return "⏰ **Consejos de organización:**\n• Horario recomendado\n• Planificación semanal\n• Establecimiento de metas\n\n¿Qué específicamente te interesa?"
    
    elif any(word in user_input for word in ['evaluación', 'calificación', 'aprobación']):
        return f"📊 **Evaluación:**\n{KNOWLEDGE_BASE['evaluacion']['criterios']}"
    
    elif any(word in user_input for word in ['duración', 'semanas', 'tiempo']):
        return f"⏱️ **Duración:** {KNOWLEDGE_BASE['modulo_propedeutico']['duracion']}"
    
    else:
        return "🤔 Interesante pregunta. Como asistente del módulo propedéutico, puedo ayudarte con:\n\n• Información del módulo\n• Técnicas de estudio\n• Uso de la plataforma\n• Organización del tiempo\n• Sistema de evaluación\n\n¿Sobre cuál de estos temas quieres saber?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        
        if not user_message.strip():
            return jsonify({'response': 'Por favor, escribe tu pregunta sobre el módulo propedéutico.'})
        
        bot_response = get_chatbot_response(user_message)
        
        return jsonify({
            'response': bot_response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'response': f'Error en el sistema: {str(e)}',
            'status': 'error'
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)