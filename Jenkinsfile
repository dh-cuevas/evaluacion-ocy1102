// Autor: DAVID H. CUEVAS SALGADO
// Evaluacion Parcial 3 - OCY1102
// Pipeline CI/CD para aplicacion Flask vulnerable

pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "flask-vulnerable-app"
        DOCKER_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = "flask-app-running"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo '========== Stage 1: Checkout =========='
                echo 'Clonando repositorio desde GitHub...'
                checkout scm
                echo 'Repositorio clonado exitosamente'
            }
        }
        
        stage('Build') {
            steps {
                echo '========== Stage 2: Build =========='
                echo 'Construyendo imagen Docker...'
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                    sh "docker build -t ${DOCKER_IMAGE}:latest ."
                }
                echo 'Imagen Docker construida exitosamente'
            }
        }
        
        stage('Test') {
            steps {
                echo '========== Stage 3: Test =========='
                echo 'Ejecutando pruebas basicas...'
                script {
                    sh "docker images ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
                echo 'Pruebas basicas completadas'
            }
        }
        
        stage('Deploy') {
            steps {
                echo '========== Stage 4: Deploy =========='
                echo 'Desplegando contenedor...'
                script {
                    sh """
                        docker stop ${CONTAINER_NAME} || true
                        docker rm ${CONTAINER_NAME} || true
                    """
                    
                    sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
                echo 'Aplicacion desplegada en http://localhost:5000'
            }
        }
        
        stage('Security Scan - OWASP ZAP') {
            steps {
                echo '========== Stage 5: Security Scan =========='
                echo 'Ejecutando OWASP ZAP Baseline Scan...'
                script {
                    // Espera que la aplicacion este lista
                    sh 'sleep 10'
                    
                    // Crea directorio de reportes si no existe
                    sh 'mkdir -p reports'
                    
                    // Ejecuta OWASP ZAP Baseline Scan
                    sh """
                        docker run --rm \
                        --network host \
                        -v \$(pwd)/reports:/zap/wrk:rw \
                        ghcr.io/zaproxy/zaproxy:stable \
                        zap-baseline.py \
                        -t http://localhost:5000 \
                        -r zap-baseline-report-vulnerable.html \
                        -I || true
                    """
                }
                echo 'Escaneo de seguridad completado'
            }
        }
    }
    
    post {
        success {
            echo '========== Pipeline ejecutado exitosamente =========='
            echo "Imagen Docker: ${DOCKER_IMAGE}:${DOCKER_TAG}"
            echo 'Aplicacion disponible en http://localhost:5000'
            echo 'Reporte de seguridad: reports/zap-baseline-report-vulnerable.html'
        }
        failure {
            echo '========== Pipeline fallo =========='
            echo 'Revisa los logs para mas detalles'
        }
        always {
            echo '========== Pipeline finalizado =========='
            // Archiva el reporte de seguridad
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}