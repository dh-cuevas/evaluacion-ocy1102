# MONITORIZACIÓN DEL ENTORNO DE PRODUCCIÓN

**Autor:** DAVID H. CUEVAS SALGADO  
**Fecha:** 26/11/2025
**Evaluación:** Parcial 3 - OCY1102

---

## ARQUITECTURA DE MONITORIZACIÓN

**Stack implementado:**
- **Prometheus** (puerto 9090) - Recolección y almacenamiento de métricas
- **Grafana** (puerto 3000) - Visualización mediante dashboards
- **cAdvisor** (puerto 8081) - Métricas de contenedores Docker

**Orquestación:** Docker Compose

---

## CONFIGURACIÓN IMPLEMENTADA

### docker-compose.yml
Se desplegaron 3 servicios en red `monitoring-network`:
- prometheus: Servidor de métricas
- grafana: Plataforma de visualización
- cadvisor: Exportador de métricas de contenedores

### prometheus.yml
Configuración de scraping cada 15 segundos para:
- prometheus (self-monitoring)
- cadvisor (métricas de contenedores)

---

## MÉTRICAS MONITOREADAS

### 1. Uso de Memoria de Contenedores
**Query Prometheus (FUNCIONAL):**
```
container_memory_working_set_bytes{container_label_com_docker_compose_service=""}
```
**Propósito:** Monitorear consumo de memoria RAM de todos los contenedores Docker  
**Visualización:** Time Series en Grafana  
**Unidad:** Bytes (convertido a MB en Grafana)

### 2. Uso de CPU de Contenedores
**Query Prometheus (FUNCIONAL):**
```
rate(container_cpu_usage_seconds_total{container_label_com_docker_compose_service=""}[1m]) * 100
```
**Propósito:** Detectar consumo excesivo de CPU que podría indicar DoS o procesos anómalos  
**Visualización:** Time Series en Grafana  
**Unidad:** Porcentaje (0-100%)

### 3. Tráfico de Red Entrante
**Query Prometheus (FUNCIONAL):**
```
rate(container_network_receive_bytes_total{container_label_com_docker_compose_service=""}[1m])
```
**Propósito:** Monitorear tráfico de red para detectar patrones anómalos  
**Visualización:** Time Series en Grafana  
**Unidad:** Bytes/segundo

---

## DASHBOARD GRAFANA

**Nombre:** Flask App Monitoring  
**Panels configurados:** 3

**Panel 1: Container Memory Usage**
- Query: `container_memory_working_set_bytes{container_label_com_docker_compose_service=""}`
- Type: Time Series
- Unit: Bytes

**Panel 2: Container CPU Usage**
- Query: `rate(container_cpu_usage_seconds_total{container_label_com_docker_compose_service=""}[1m]) * 100`
- Type: Time Series
- Unit: Percent (%)

**Panel 3: Network Traffic**
- Query: `rate(container_network_receive_bytes_total{container_label_com_docker_compose_service=""}[1m])`
- Type: Time Series
- Unit: Bytes/sec

**Refresh interval:** 5 segundos  
**Time range:** Last 15 minutes

---

## PRUEBAS REALIZADAS

### Test 1: Verificación de Recolección de Métricas
**Acción:** Consultas en Prometheus Graph  
**Resultado:**
- Métricas de memoria visibles para todos los contenedores
- Métricas de CPU funcionando correctamente
- Métricas de red recolectándose
- Contenedor flask-app-running identificado en métricas

### Test 2: Generación de Tráfico Normal
**Acción:** 200 requests HTTP GET a http://localhost:5000  
**Comando ejecutado:**
```powershell
for ($i=1; $i -le 200; $i++) {
    curl http://localhost:5000 -UseBasicParsing | Out-Null
}
```
**Resultado:**
- CPU: Incremento visible en dashboard (5-20%)
- Memoria: Estable (~100-120 MB)
- Network: Picos de tráfico detectados en tiempo real
- Sistema: Sin degradación de performance

### Test 3: Monitoreo en Tiempo Real
**Acción:** Observación de dashboards durante 5 minutos  
**Resultado:**
- Grafana actualizando métricas cada 5 segundos
- Prometheus recolectando datos correctamente
- cAdvisor exportando métricas de 5 contenedores activos
- Sistema de monitorización estable

---

## SERVICIOS MONITOREADOS

Contenedores bajo monitorización activa:
1. **flask-app-running** - Aplicación web Flask (puerto 5000)
2. **jenkins** - Servidor CI/CD (puerto 8080)
3. **prometheus** - Sistema de métricas (puerto 9090)
4. **grafana** - Visualización (puerto 3000)
5. **cadvisor** - Exportador de métricas (puerto 8081)

---

## ACCESO A LOS SISTEMAS

**Prometheus:**
- URL: http://localhost:9090
- Targets: http://localhost:9090/targets
- Graph: http://localhost:9090/graph

**Grafana:**
- URL: http://localhost:3000
- Usuario: admin
- Contraseña: admin
- Dashboard: Flask App Monitoring

**cAdvisor:**
- URL: http://localhost:8081
- Docker Containers: http://localhost:8081/docker

---

## HALLAZGOS Y OBSERVACIONES

### Configuración Exitosa
- Stack de monitorización completamente funcional  
- Métricas recolectándose correctamente vía cAdvisor  
- Prometheus almacenando datos con retención configurada  
- Grafana visualizando métricas en tiempo real  
- Queries ajustadas para compatibilidad con etiquetas de Docker Compose

### Consideraciones Técnicas
- Las queries utilizan etiquetas de Docker Compose para identificar contenedores
- cAdvisor actúa como proxy de métricas para contenedores Docker
- Refresh interval de 5 segundos apropiado para monitoreo en tiempo real
- Sistema escalable para añadir más contenedores

---

## MEJORAS FUTURAS

Para implementación en producción se recomienda:

**Alertas Automatizadas:**
- CPU > 80% por 5 minutos → Notificación
- Memoria > 90% → Alerta crítica
- Contenedor reiniciado → Notificación inmediata

**Retención de Datos:**
- Configurar retención de 30 días en Prometheus
- Exportar métricas históricas a almacenamiento persistente

**Dashboards Adicionales:**
- Dashboard de comparación entre contenedores
- Panel de disponibilidad (uptime)
- Métricas de aplicación (requests/sec, latencia)

**Seguridad:**
- Autenticación en Prometheus
- HTTPS para Grafana
- Restricción de acceso por IP

---

## CONCLUSIÓN

El sistema de monitorización fue implementado exitosamente cumpliendo con los objetivos:

- IL 3.2 Cumplido:** Monitorización del entorno de producción implementada  
- Stack Prometheus + Grafana + cAdvisor funcional  
- Métricas de CPU, Memoria y Red visualizadas  
- Dashboard operativo y configurado  
- Pruebas de carga documentadas  
- Sistema preparado para detección de incidentes

El sistema permite detectar anomalías en tiempo real, facilitando la respuesta rápida ante incidentes de seguridad o degradación de performance.