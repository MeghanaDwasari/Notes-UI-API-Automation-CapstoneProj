pipeline {
    agent any

    parameters {
        choice(
            name: 'RUN_MODE',
            choices: ['local', 'grid'],
            description: 'Run tests locally or on Selenium Grid'
        )
    }

    environment {
        VENV_DIR = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/MeghanaDwasari/Notes-UI-API-Automation-CapstoneProj.git'
            }
        }

        stage('Clean Old Docker Containers') {
            when {
                expression { params.RUN_MODE == 'grid' }
            }
            steps {
                bat """
                echo Cleaning old Selenium containers...
                docker-compose down --remove-orphans || exit 0
                docker rm -f selenium-hub || exit 0
                docker network prune -f || exit 0
                """
            }
        }

        stage('Start Selenium Grid') {
            when {
                expression { params.RUN_MODE == 'grid' }
            }
            steps {
                bat """
                docker-compose up -d --force-recreate
                """
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat """
                if not exist %VENV_DIR% (
                    python -m venv %VENV_DIR%
                )

                %VENV_DIR%\\Scripts\\python -m pip install --upgrade pip
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                %VENV_DIR%\\Scripts\\pip install -r requirements.txt
                """
            }
        }

        stage('Run Automation Tests') {
            steps {
                bat """
                set RUN_MODE=%RUN_MODE%
                %VENV_DIR%\\Scripts\\pytest -n 2 --alluredir=allure-results
                """
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat """
                allure generate allure-results --clean -o allure-report
                """
            }
        }
    }

    post {

        always {
            archiveArtifacts artifacts: 'allure-report/**', fingerprint: true

            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'allure-results']]

            bat """
            docker-compose down --remove-orphans || exit 0
            """
        }

        success {
            echo "✅ Pipeline executed successfully"
        }

        failure {
            echo "❌ Pipeline failed — check logs above"
        }
    }
} 

