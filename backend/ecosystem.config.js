module.exports = {
  apps: [
    {
      name: "django-backend",
      script: "/root/back/ark-backend/backend/env/bin/gunicorn",
      args: "--workers 3 --bind 127.0.0.1:8000 backend.wsgi:application",
      interpreter: "/root/back/ark-backend/backend/env/bin/python",
      exec_mode: "fork",
      autorestart: true,
      watch: false,
      env: {
        "DJANGO_SETTINGS_MODULE": "backend.settings",
        "PORT": 8000,
      },
    },
  ],
};

