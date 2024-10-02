from flask import Flask, render_template
from urllib.parse import quote as url_quote

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Git route
@app.route('/git')
def git():
    return render_template('git.html', title='Git & Version Control')

# Docker route
@app.route('/docker')
def docker():
    return render_template('docker.html', title='Docker & Containerization')

# Kubernetes route
@app.route('/kubernetes')
def kubernetes():
    return render_template('kubernetes.html', title='Kubernetes & Orchestration')

# Terraform route
@app.route('/terraform')
def terraform():
    return render_template('terraform.html', title='Terraform & Infrastructure as Code')

# CI/CD route
@app.route('/cicd')
def cicd():
    return render_template('cicd.html', title='CI/CD Pipelines')

# Monitoring route
@app.route('/monitoring')
def monitoring():
    return render_template('monitoring.html', title='Monitoring with Prometheus & Grafana')

# Security route
@app.route('/security')
def security():
    return render_template('security.html', title='Security Testing with Trivy')

@app.route('/linux')
def linux():
    return render_template('linux.html', title='Linux Guide')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

