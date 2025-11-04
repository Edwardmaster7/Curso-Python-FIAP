logs = [
    # timestamp, level, message, endpoint, method, response_code
    ("2023-10-27 10:00:00", "INFO", "User 'admin' logged in successfully.", "/login", "POST", 200),
    ("2023-10-27 10:05:15", "DEBUG", "Processing request for page 'dashboard'.", "/dashboard", "GET", 200),
    ("2023-10-27 10:05:30", "WARNING", "API response time is above threshold: 1.5s.", "/api/data", "GET", 200),
    ("2023-10-27 10:10:00", "ERROR", "Database connection failed: timeout expired.", "/db/connect", "POST", 500),
    ("2023-10-27 10:10:05", "CRITICAL", "System shutting down due to critical error.", "/system/shutdown", "POST", 503),
]

errors = [log for log in logs if log[5] >= 500]

methods = [log[3] for log in logs]

ultimos_logs = logs[-2:] # elementos : quantos elementos eu quero depois dos elementos
print(ultimos_logs)

print(f"Total de erros: {len(errors)}")



