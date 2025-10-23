
Endpoints:
health http://127.0.0.1:8010/health


Vscode debug config:

{
    "version": "0.2.0",
    "configurations": [
        
        {
            "name": "Bandit (uvicorn reload)",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "cwd": "${workspaceFolder}/services/bandit",
            "args": [
                "app.main:app",
                "--reload",
                "--port",
                "8010"
            ],
            "envFile": "${workspaceFolder}/services/bandit/.env",
            "env": {
                "PYTHONPATH": "${workspaceFolder}/services/bandit"
            },
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}