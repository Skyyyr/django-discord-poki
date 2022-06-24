# Discord Poke Bot

This is an app that uses 2 separate APIs, and Django.
Discord API, and Poke API.

The project will attempt to create a simple text based adventure
involving Pokemon!

Expanding on the lessons learned from class, and attempting to push further...

### SETUP

1. Setup venv
2. `pip install discord.py`
3. install django
4. create a file `token.json`
5. `{
"TOKEN": "put your token here",
"PREFIX": "!"
}`
6. You can change the prefix to whatever you'd like.

### Project Notes
Cogs can be used to extend the bot in specific ways like creating a specific set of commands.
refer to `cogs/ExampleHandler.py`