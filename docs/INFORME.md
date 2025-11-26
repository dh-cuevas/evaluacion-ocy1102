# INFORME TÉCNICO - EVALUACIÓN PARCIAL 3
## Pipeline CI/CD con DevSecOps
### Explotación y Mitigación de Vulnerabilidades Web

---

**Autor:** [Tu Nombre Completo]  
**RUT:** [Tu RUT]  
**Asignatura:** OCY1102 - Ciberseguridad en Desarrollo  
**Profesor:** [Nombre del profesor]  
**Institución:** Duoc UC  
**Fecha de elaboración:** [Fecha actual]  
**Ponderación:** 35%

---

## TABLA DE CONTENIDOS

1. [Introducción](#1-introducción)
2. [Arquitectura del Pipeline](#2-arquitectura-del-pipeline)
3. [Fase 0: Preparación del Entorno](#3-fase-0-preparación-del-entorno)
4. [Fase 1: Construcción del Pipeline Base](#4-fase-1-construcción-del-pipeline-base)
5. [Fase 2: Análisis de Vulnerabilidades](#5-fase-2-análisis-de-vulnerabilidades)
6. [Fase 3: Corrección de Vulnerabilidades](#6-fase-3-corrección-de-vulnerabilidades)
7. [Fase 4: Validación de Correcciones](#7-fase-4-validación-de-correcciones)
8. [Fase 5: Gestión de Dependencias](#8-fase-5-gestión-de-dependencias)
9. [Fase 6: Monitorización del Entorno](#9-fase-6-monitorización-del-entorno)
10. [Conclusiones](#10-conclusiones)
11. [Referencias](#11-referencias)
12. [Anexos](#12-anexos)

---

## 1. INTRODUCCIÓN

### 1.1 Contexto del Proyecto

La empresa **SecureDev** ha decidido mejorar su proceso de desarrollo de software 
implementando un pipeline de CI/CD que integre prácticas de seguridad en todas 
las etapas del ciclo de vida del desarrollo (SDLC). La empresa necesita garantizar 
que las aplicaciones desarrolladas sean seguras y cumplan con los estándares de 
la industria.

Durante una auditoría interna se identificaron varias vulnerabilidades críticas en 
el proceso actual de desarrollo y despliegue, incluyendo:

- Falta de integración de pruebas de seguridad automatizadas en el pipeline
- Gestión deficiente de dependencias y actualizaciones de seguridad
- Documentación y trazabilidad insuficientes para auditorías
- Monitorización inadecuada del entorno de producción

### 1.2 Objetivos Generales

Diseñar e implementar un pipeline de CI/CD utilizando Jenkins y Docker que permita:

1. Automatizar la construcción, pruebas y despliegue de aplicaciones
2. Integrar herramientas de pruebas de seguridad automatizadas (OWASP ZAP)
3. Identificar y corregir vulnerabilidades en el código
4. Gestionar dependencias de forma segura y automatizada
5. Monitorear el entorno de producción en tiempo real
6. Mantener documentación y trazabilidad completa para auditorías

### 1.3 Objetivos Específicos (Indicadores de Logro)

**IL 3.1** - Implementar revisiones de seguridad continuas durante el ciclo de vida 
del desarrollo del software, asegurando la identificación y mitigación temprana de 
vulnerabilidades.

**IL 3.2** - Aplicar técnicas como la automatización de pruebas de seguridad, la 
implementación continua y la monitorización del entorno de producción.

**IL 3.3** - Gestionar las dependencias y actualizaciones de seguridad aplicando 
políticas de gestión de riesgos y procedimientos de parcheo.

**IL 3.4** - Preparar documentación y trazabilidad para auditorías de seguridad, 
desarrollando informes detallados y registros de actividades.

### 1.4 Alcance del Proyecto

Este proyecto implementa un pipeline completo de DevSecOps que incluye:

- OK Aplicación web Flask con vulnerabilidades intencionales
- OK Containerización con Docker
- OK Pipeline CI/CD automatizado con Jenkins
- OK Análisis de seguridad con OWASP ZAP
- OK Corrección de vulnerabilidades identificadas
- OK Gestión de dependencias con Dependabot
- OK Monitorización con Grafana y Prometheus
- OK Documentación completa y trazabilidad

---

## 2. ARQUITECTURA DEL PIPELINE

### 2.1 Diagrama General
```
[GitHub Repository]
        ↓
    [Jenkins]
        ↓
   ┌────┴────┐
   ↓         ↓
[Build]  [Test]
   ↓         ↓
[Docker] [OWASP ZAP]
   ↓         ↓
[Deploy] [Reports]
   ↓
[Grafana/Prometheus]
```

### 2.2 Componentes del Sistema

**Control de Versiones:**
- GitHub: Repositorio del código fuente
- Git: Control de versiones local

**CI/CD:**
- Jenkins: Automatización del pipeline
- Docker: Containerización de la aplicación

**Seguridad:**
- OWASP ZAP: Análisis de vulnerabilidades web
- Dependabot: Gestión de dependencias

**Monitorización:**
- Prometheus: Recolección de métricas
- Grafana: Visualización de dashboards

### 2.3 Flujo del Pipeline

1. **Checkout**: Clonar código desde GitHub
2. **Build**: Construir imagen Docker de la aplicación
3. **Test**: Ejecutar pruebas unitarias
4. **Security Scan**: Análisis con OWASP ZAP
5. **Deploy**: Desplegar contenedor
6. **Monitor**: Recolección de métricas

---

## 3. FASE 0: PREPARACIÓN DEL ENTORNO

### 3.1 Herramientas Instaladas y Configuradas

**Sistema Operativo:**
- Windows 10/11
- PowerShell 5.1+

**Docker:**
- Versión: 28.5.1
- Estado: ✅ Operativo
- Contenedores activos: Jenkins

**Jenkins:**
- Versión: LTS (jenkins/jenkins:lts)
- Puerto de acceso: 8080
- Puerto de agentes: 50000
- Estado: ✅ Corriendo en contenedor Docker
- Volumen persistente: jenkins-data

**Git:**
- Configurado para el proyecto
- Usuario: [Tu nombre]
- Email: [Tu email]
- Repositorio remoto: https://github.com/dh-cuevas/evaluacion-ocy1102

### 3.2 Estructura del Repositorio Creada
```
C:\proyectos\evaluacion-ocy1102\
├── src/
│   ├── vulnerable_flask_app.py
│   ├── create_db.py
│   └── templates/
├── config/
├── docs/
│   ├── INFORME.md
│   ├── BITACORA.md
│   └── evidencias/
├── reports/
├── monitoring/
├── .gitignore
└── README.md
```

### 3.3 Evidencias de la Fase 0

#### 3.3.1 Verificación de Docker

![Docker Version](evidencias/fase0-docker-version.png)

**Comando ejecutado:**
```powershell
docker --version
docker ps
```

**Resultado:**
- Docker versión 28.5.1 funcionando correctamente
- Contenedor Jenkins corriendo en puerto 8080

#### 3.3.2 Verificación de Jenkins

![Jenkins Dashboard](evidencias/fase0-jenkins-dashboard.png)

**URL de acceso:** http://localhost:8080  
**Estado:** Operativo

#### 3.3.3 Estructura del Proyecto

![Estructura de carpetas](evidencias/fase0-estructura-proyecto.png)

**Comando ejecutado:**
```powershell
tree /F
```

### 3.4 Archivos Base Creados

| Archivo                       | Propósito                                    |
|-------------------------------|----------------------------------------------|
| `.gitignore`                  | Exclusión de archivos sensibles y temporales |
| `README.md`                   | Documentación general del proyecto           |
| `docs/INFORME.md`             | Informe técnico completo                     |
| `docs/BITACORA.md`            | Registro de actividades                      |
| `src/vulnerable_flask_app.py` | Aplicación Flask con vulnerabilidades        |
| `src/create_db.py`            | Script de creación de base de datos          |

### 3.5 Tiempo Invertido

| Actividad                             | Tiempo     |
|---------------------------------------|------------|
| Verificación de Docker y Jenkins      | 5 min      |
| Creación de estructura de carpetas    | 5 min      |
| Creación de archivos Python           | 10 min     |
| Creación de archivos de documentación | 10 min     |
| Configuración de Git y GitHub         | 10 min     |
| **Total Fase 0**                      | **40 min** |

---

## 4. FASE 1: CONSTRUCCIÓN DEL PIPELINE BASE

[Esta sección se completará en la siguiente fase]

---

## 5. FASE 2: ANÁLISIS DE VULNERABILIDADES

[Esta sección se completará posteriormente]

---

## 6. FASE 3: CORRECCIÓN DE VULNERABILIDADES

[Esta sección se completará posteriormente]

---

## 7. FASE 4: VALIDACIÓN DE CORRECCIONES

[Esta sección se completará posteriormente]

---

## 8. FASE 5: GESTIÓN DE DEPENDENCIAS

[Esta sección se completará posteriormente]

---

## 9. FASE 6: MONITORIZACIÓN DEL ENTORNO

[Esta sección se completará posteriormente]

---

## 10. CONCLUSIONES

[Se completará al finalizar todas las fases]

---

## 11. REFERENCIAS

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- Jenkins Documentation: https://www.jenkins.io/doc/
- Docker Documentation: https://docs.docker.com/
- OWASP ZAP: https://www.zaproxy.org/docs/
- Flask Security: https://flask.palletsprojects.com/en/2.3.x/security/

---

## 12. ANEXOS

### Anexo A: Código Vulnerable Original
### Anexo B: Código Corregido
### Anexo C: Reportes de OWASP ZAP
### Anexo D: Configuraciones de Jenkins
### Anexo E: Dashboards de Grafana

---

**Fin del documento**