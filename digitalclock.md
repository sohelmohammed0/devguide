        }

        /* 3D Digital Clock */
        .digital-clock {
            font-family: 'Orbitron', sans-serif;
            font-size: 2.5rem;
            color: #00ffea;
            text-shadow: 0 0 8px #00ffea, 0 0 16px #00ffea;
            margin-bottom: 40px;
        }



         <!-- Digital Clock -->
    <div class="digital-clock" id="clock"></div>

     <script>
        // Digital clock functionality
        function updateClock() {
            const now = new Date();
            const hours = String(now.getHours()).padStart(2, '0');
            const minutes = String(now.getMinutes()).padStart(2, '0');
            const seconds = String(now.getSeconds()).padStart(2, '0');
            const timeString = `${hours}:${minutes}:${seconds}`;
            document.getElementById('clock').textContent = timeString;
        }

        setInterval(updateClock, 1000);
        updateClock();
    </script>