{% extends "base.html" %}
{% block content %}
    <!-- Sidebar Navigation -->
    <nav>
        <h1>DevOps Guide</h1>
        <ul>
            <li><a href="#"><i class="fas fa-home"></i>Home</a></li>
            <li><a href="#"><i class="fas fa-code"></i>CI/CD Pipelines</a></li>
            <li><a href="#"><i class="fas fa-tools"></i>Tools</a></li>
            <li><a href="#"><i class="fas fa-book"></i>Resources</a></li>
            <li><a href="#"><i class="fas fa-question-circle"></i>FAQ</a></li>
        </ul>
    </nav>

    <!-- Main Content -->
    <main>
        <header>
            <h1>CI/CD Pipelines for Beginners</h1>
        </header>

        <!-- Introduction Section -->
        <section class="section">
            <div class="card">
                <h3 class="section-title">Introduction to CI/CD</h3>
                <p>Continuous Integration (CI) and Continuous Deployment/Delivery (CD) are essential practices in modern software development...</p>
            </div>
        </section>

        <!-- Features Section -->
        <section class="section">
            <div class="card">
                <h3 class="section-title">Features of CI/CD</h3>
                <ul>
                    <li><i class="fas fa-check-circle"></i> Frequent Integration of Code Changes</li>
                    <li><i class="fas fa-check-circle"></i> Automated Testing for Higher Code Quality</li>
                    <li><i class="fas fa-check-circle"></i> Continuous Delivery/Deployment of Updates</li>
                    <li><i class="fas fa-check-circle"></i> Faster Feedback for Developers</li>
                </ul>
            </div>
        </section>

        <!-- More sections follow with similar structure... -->
    </main>

    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #1e1e2f;
            color: #fff;
            display: flex;
            min-height: 100vh;
        }

        nav {
            width: 250px;
            background-color: #13132b;
            padding: 30px 20px;
            position: fixed;
            height: 100%;
            box-shadow: 5px 0 15px rgba(158, 43, 35, 0.2);
        }

        nav h1 {
            color: #29ff30;
            font-size: 1.8rem;
            margin-bottom: 40px;
        }

        nav ul li {
            margin-bottom: 25px;
        }

        nav ul li a {
            color: #1e7c8b;
            font-size: 1.2rem;
            display: flex;
            align-items: center;
            transition: 0.3s;
        }

        nav ul li a:hover {
            color: #09ff00;
        }

        main {
            margin-left: 270px;
            padding: 50px;
            flex: 1;
        }

        header h1 {
            font-size: 3.5rem;
            color: #2c3e50;
            background: linear-gradient(90deg, #2980b9, #6dd5fa);
            padding: 15px;
            text-align: center;
            margin-bottom: 50px;
        }

        .section {
            margin-bottom: 30px;
        }

        .card {
            background-color: #292b44;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .section-title {
            font-size: 1.8rem;
            margin-bottom: 15px;
            color: #ffab00;
        }

        ul {
            list-style-type: none;
            padding-left: 0;
        }

        ul li {
            margin-bottom: 10px;
            font-size: 1.1rem;
        }

        ul li i {
            margin-right: 10px;
            color: #29ff30;
        }
    </style>
{% endblock %}
