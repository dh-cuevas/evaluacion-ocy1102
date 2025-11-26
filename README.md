# Evaluación Parcial 3 - OCY1102
## Explotación y Mitigación de Vulnerabilidades Web

**Estudiante:** DAVID H. CUEVAS SALGADO 
**Asignatura:** Ciberseguridad en Desarrollo (OCY1102-001D)  
**Institución:** Duoc UC  
**Fecha:** Noviembre 2024

---

## Descripción del Proyecto

Implementación de un pipeline CI/CD con Jenkins y Docker para identificar, 
documentar y mitigar vulnerabilidades en aplicaciones web siguiendo prácticas 
de DevSecOps y cumpliendo con los estándares de seguridad de la industria.

---

## Objetivos

1. Implementar pipeline CI/CD automatizado
2. Integrar pruebas de seguridad automatizadas (OWASP ZAP)
3. Identificar y corregir vulnerabilidades en código vulnerable
4. Gestionar dependencias de forma segura (Dependabot)
5. Monitorear entorno de producción (Grafana/Prometheus)
6. Documentar todo el proceso para auditorías

---

## Estructura del Proyecto
```
evaluacion-ocy1102/
├── src/                    # Código fuente de la aplicación
│   ├── vulnerable_flask_app.py    # Aplicación Flask con vulnerabilidades
│   ├── create_db.py               # Script de creación de BD
│   └── templates/                 # Templates HTML
├── config/                 # Archivos de configuración
│   ├── Dockerfile
│   ├── Jenkinsfile
│   └── docker-compose.yml
├── docs/                   # Documentación completa
│   ├── INFORME.md         # Informe técnico detallado
│   ├── BITACORA.md        # Registro de actividades
│   └── evidencias/        # Capturas de pantalla
├── reports/                # Reportes de seguridad
│   ├── zap-vulnerable/    # Reportes de versión vulnerable
│   └── zap-fixed/         # Reportes de versión corregida
└── monitoring/             # Configuración de monitorización
    ├── prometheus/
    └── grafana/
```

---

## Herramientas Utilizadas

- **Jenkins** - Automatización CI/CD
- **Docker** - Containerización
- **OWASP ZAP** - Pruebas de seguridad automatizadas
- **Grafana** - Visualización de métricas
- **Prometheus** - Recolección de métricas
- **Dependabot** - Gestión automática de dependencias
- **Git/GitHub** - Control de versiones

---

## Vulnerabilidades Identificadas y Corregidas

1. **SQL Injection** - Login vulnerable a inyección SQL
2. **XSS (Cross-Site Scripting)** - Comentarios sin sanitizar
3. **Debug Mode** - Modo debug activado en producción
4. **Weak Secret Key** - Clave secreta generada con os.urandom()
5. **Weak Password Hashing** - SHA256 sin salt
6. **Template Injection** - Uso inseguro de render_template_string

---

## Cómo Ejecutar

### Requisitos previos
- Docker Desktop instalado
- Jenkins configurado
- Git instalado

### Ejecución local
```bash
cd src
python create_db.py
python vulnerable_flask_app.py
```

### Ejecución con Docker
```bash
docker-compose up --build
```

### Pipeline Jenkins
1. Acceder a Jenkins: http://localhost:8080
2. Crear nuevo Job tipo Pipeline
3. Conectar con este repositorio
4. Ejecutar pipeline

---

## Resultados

- OK Pipeline CI/CD funcional
- OK Vulnerabilidades identificadas: 6
- OK Vulnerabilidades corregidas: 6
- OK Dependencias actualizadas
- OK Monitorización implementada
- OK Documentación completa

---

## Documentación

- [Informe Técnico Completo](docs/INFORME.md)
- [Bitácora de Trabajo](docs/BITACORA.md)
- [Evidencias](docs/evidencias/)

---

## Autor

**Desarrollado por:** DAVID H. CUEVAS SALGADO
**Curso:** OCY1102-001D - Ciberseguridad en Desarrollo  
**Institución:** Duoc UC  
**GitHub:** https://github.com/dh-cuevas/evaluacion-ocy1102

---

## Licencia

Evaluación académica para Duoc UC.
