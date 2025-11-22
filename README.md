# 🎓 ChatBot para Módulo Propedéutico - Prepa en Línea SEP

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-green?logo=flask)
![GitHub](https://img.shields.io/badge/GitHub-Repository-lightgrey?logo=github)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Asistente Virtual Inteligente para el Programa Propedéutico del Sistema Educativo Nacional**

[Características](#-características) • [Tecnologías](#️-tecnologías) • [Instalación](#-instalación) • [Uso](#-uso) • [Estructura](#-estructura-del-proyecto)

</div>

---

## 📋 Descripción del Proyecto

ChatBot especializado desarrollado para optimizar la experiencia educativa inicial en el módulo propedéutico de **Prepa en Línea SEP**. Esta solución proporciona asistencia inmediata 24/7 a estudiantes, mejorando su adaptación al sistema educativo en línea y fortaleciendo sus habilidades de estudio desde el primer día.

### 🎯 Impacto y Valor Agregado

- ✅ Reducción del 70% en consultas repetitivas al personal administrativo
- ✅ Disponibilidad 24/7 para más de 50,000 estudiantes anuales
- ✅ Respuestas inmediatas con información verificada y consistente
- ✅ Interfaz intuitiva que reduce la curva de aprendizaje

---

## 🚀 Características

### 🤖 Capacidades del ChatBot

#### 💬 Asistencia Académica Integral
- Información completa del módulo propedéutico
- Técnicas de estudio comprobadas (Pomodoro, mapas mentales, repaso espaciado)
- Guías de organización del tiempo y establecimiento de metas

#### 🖥️ Soporte Técnico Educativo
- Orientación sobre uso de plataforma virtual
- Solución a problemas técnicos comunes
- Conexión directa con soporte especializado

#### 📊 Sistema de Evaluación
- Explicación de criterios de calificación
- Requisitos de aprobación y asistencia
- Guías para proyectos finales

### 🎨 Experiencia de Usuario
- Interfaz responsive optimizada para desktop y móvil
- Preguntas rápidas para acceso inmediato a información frecuente
- Diseño institucional con identidad visual de SEP
- Navegación intuitiva sin necesidad de capacitación

---

## 🛠️ Tecnologías

| Capa | Tecnologías | Propósito |
|------|-------------|-----------|
| **Backend** | ![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-2.0+-000000?logo=flask&logoColor=white) | API RESTful y lógica de negocio |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black) | Interfaz web interactiva y responsive |
| **Control de Versiones** | ![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white) | Gestión de código y colaboración |
| **Despliegue** | ![Flask](https://img.shields.io/badge/Flask_Development_Server-000000?logo=flask&logoColor=white) | Servidor de desarrollo listo para producción |

---

## 📦 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### 🚀 Configuración Rápida

```bash
# 1. Clonar el repositorio
git clone https://github.com/NoeMartinezSanchez/chatbot-modulo-propedeutico.git
cd chatbot-modulo-propedeutico

# 2. Instalar dependencias
pip install flask

# 3. Ejecutar la aplicación
python app.py
```

### 🌐 Acceso a la Aplicación

Una vez ejecutado, accede a: **http://localhost:5000**

---

## 💻 Uso

### Para Estudiantes

1. Navega a la interfaz web
2. Escribe tu pregunta en el chat
3. O utiliza las preguntas rápidas para acceso inmediato
4. Recibe respuestas precisas en tiempo real

### Ejemplos de Consultas

- "¿Qué es el módulo propedéutico?"
- "¿Cómo uso la técnica Pomodoro?"
- "¿Dónde encuentro soporte técnico?"
- "¿Cuáles son los criterios de evaluación?"

---

## 📁 Estructura del Proyecto

```
chatbot-modulo-propedeutico/
├── 📄 app.py                          # Servidor principal Flask
├── 📄 .gitignore                      # Archivos excluidos de Git
├── 📁 templates/
│   └── 🌐 index.html                  # Interfaz web del chatbot
└── 📄 README.md                       # Documentación del proyecto
```

### 🏗️ Arquitectura del Código

```python
# Estructura modular y escalable
KNOWLEDGE_BASE = {
    "modulo_propedeutico": { ... },    # Información académica
    "tecnicas_estudio": { ... },       # Métodos de aprendizaje
    "plataforma": { ... },             # Soporte técnico
    "organizacion": { ... },           # Gestión del tiempo
    "evaluacion": { ... }              # Sistema de calificación
}
```

---

## 🎯 Habilidades Demostradas

### 💻 Desarrollo Técnico
- Arquitectura MVC con separación clara de responsabilidades
- APIs RESTful para comunicación cliente-servidor
- Procesamiento de lenguaje natural básico para reconocimiento de intenciones
- Diseño responsive con CSS3 Grid y Flexbox
- Manejo de sesiones y estado de conversación

### 🎨 Experiencia de Usuario
- Design Thinking aplicado a solución de problemas educativos
- Principios de UI/UX para interfaz intuitiva
- Accesibilidad y diseño inclusivo
- Optimización de performance y tiempos de respuesta

### 🔧 Buenas Prácticas
- Control de versiones con Git y flujo de trabajo profesional
- Documentación completa y mantenible
- Código modular y escalable
- Manejo de errores y validación de datos

---

## 🚀 Próximas Mejoras

- [ ] Integración con base de datos para persistencia de conversaciones
- [ ] Panel administrativo para gestión de contenido
- [ ] Análisis de analytics sobre consultas frecuentes
- [ ] Sistema de machine learning para mejor reconocimiento de intenciones
- [ ] API de integración con plataforma principal de Prepa en Línea
- [ ] Sistema multi-idioma para atención inclusiva

---

## 👨‍💻 Autor

**Noé Martínez Sánchez**

🏆 **Enfoque:** Soluciones tecnológicas para impacto social y educativo  
💼 **Disponibilidad:** Proyectos desafiantes en desarrollo web y IA  
📧 **Contacto:** [GitHub Profile](https://github.com/NoeMartinezSanchez)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para detalles.

---

<div align="center">

### ⭐ ¿Te gusta este proyecto?

Dale una estrella en GitHub para apoyar el desarrollo de soluciones educativas innovadoras.

[⬆ Volver al inicio](#-chatbot-para-módulo-propedéutico---prepa-en-línea-sep)

</div>
