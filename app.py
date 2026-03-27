from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    # 模拟数据（你以后可以从数据库取）
    data = {
        "server_count": 8,
        "online_count": 7,
        "cmd_count": 34,
        "warn_count": 1,
        "logs": [
            {"ip": "192.168.1.10", "cmd": "df -h", "time": "2026-03-27 10:22"},
            {"ip": "192.168.1.11", "cmd": "systemctl status nginx", "time": "2026-03-27 10:20"},
            {"ip": "192.168.1.12", "cmd": "free -h", "time": "2026-03-27 10:18"},
        ]
    }
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(debug=True)