services: gastro-school-bot
  - type: web
    name: gastro-school-bot
    runtime: python
    buildCommand: ""
    startCommand: "python gastro_school_bot.py"
    envVars:
      - key: YOUR_TELEGRAM_BOT_TOKEN
        value: ваш_токен_от_BotFather
