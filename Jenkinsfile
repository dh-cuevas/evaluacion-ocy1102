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
                    bat "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                    bat "docker build -t ${DOCKER_IMAGE}:latest ."
                }
                echo 'Imagen Docker construida exitosamente'
            }
        }
        
        stage('Test') {
            steps {
                echo '========== Stage 3: Test =========='
                echo 'Ejecutando pruebas basicas...'
                script {
                    bat "docker images ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
                echo 'Pruebas basicas completadas'
            }
        }
        
        stage('Deploy') {
            steps {
                echo '========== Stage 4: Deploy =========='
                echo 'Desplegando contenedor...'
                script {
                    bat """
                        docker stop ${CONTAINER_NAME} 2>nul || echo "No hay contenedor previo"
                        docker rm ${CONTAINER_NAME} 2>nul || echo "No hay contenedor que eliminar"
                    """
                    
                    bat "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
                echo 'Aplicacion desplegada en http://localhost:5000'
            }
        }
    }
    
    post {
        success {
            echo '========== Pipeline ejecutado exitosamente =========='
            echo "Imagen Docker: ${DOCKER_IMAGE}:${DOCKER_TAG}"
            echo 'Aplicacion disponible en http://localhost:5000'
        }
        failure {
            echo '========== Pipeline fallo =========='
            echo 'Revisa los logs para mas detalles'
        }
        always {
            echo '========== Pipeline finalizado =========='
        }
    }
}