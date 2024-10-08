# Description

A template for a django app

# Requirements

- Install [Python-Poetry](https://python-poetry.org/docs/#installation)
- Install [Docker](https://docs.docker.com/engine/install/) or [Docker-Desktop](https://www.docker.com/) (recommended)
- On a terminal execute `make dev-db`
- On another terminal execute `make update`

# Development

## Choosing IDE for development (optional)
Download an IDE of your liking ([vscode](https://code.visualstudio.com/) or [pycharm](https://www.jetbrains.com/pycharm/) are the most commonly used). We are using vscode, as it is lightweight and easy to import extensions. As stated above, `vim` is the recommended editing method, so if you are using "vscode" there is the "Vim" extension to install. Some useful extensions you can install on your vscode setup are also listed below:

- Vim
- Python
- Pylance
- Django
- Docker
- Prettier
- Python Indent
- HTML Boilerplate
- Indent one space
- Auto Close Tag
- gettext
- SQLite
- SQLite Viewer

You can uninstall each extension any time.

A template for `settings.json` in "vscode" is given below.
```json
{
    "workbench.colorTheme": "Default Dark+",
    "auto-close-tag.activationOnLanguage": [
        "xml",
        "php",
        "blade",
        "ejs",
        "jinja",
        "javascript",
        "javascriptreact",
        "typescript",
        "typescriptreact",
        "plaintext",
        "markdown",
        "vue",
        "liquid",
        "erb",
        "lang-cfml",
        "cfml",
        "HTML (EEx)",
        "HTML (Eex)",
        "django-html",
        "plist"
    ],
    "emmet.includeLanguages": {
        "django-html": "html",
    },
    "beautify.language": {
        "js": {
            "type": [
                "javascript",
                "json",
                "jsonc"
            ],
            "filename": [
                ".jshintrc",
                ".jsbeautifyrc"
            ]
        },
        "css": [
            "css",
            "less",
            "scss"
        ],
        "html": [
            "htm",
            "html",
            "django-html",
        ]
    },
    "editor.minimap.enabled": false,
    "[css]": {
        "editor.defaultFormatter": "HookyQR.beautify"
    },
    "[html]": {
        "editor.defaultFormatter": "HookyQR.beautify"
    },
    "workbench.startupEditor": "none",
    "terminal.integrated.defaultProfile.windows": "Command Prompt",
    "[json]": {
        "editor.defaultFormatter": "HookyQR.beautify"
    },
    "[javascript]": {
        "editor.defaultFormatter": "HookyQR.beautify"
    },
    "auto-close-tag.disableOnLanguage": [

    ],
    "python.formatting.provider": "yapf",
    "[python]": {
    },
    "editor.unicodeHighlight.ambiguousCharacters": false,
    "window.zoomLevel": 1,
}
```
---

## Setting environments (optional)
It is a good practice to use `.env` (dotenv) files to set parameters in your app.
These `.env` files, keep sensitive information about your project (such as encryption keys and passwords) and thus, should NEVER be uploaded in your project's git repository. So a separate rule is added for them in the `.gitignore` file.

In this project, three `.env` files may be used:

- For database: `db.env`
- For debugging: `dev.env`
- For production: `prod.env`

These files are usually placed within a folder `.env`
Use the example files within directory `.env/templates`

---

## Starting the django server
*Note:* For development we will use the local django server [django server](http://127.0.0.1:8000):

### Run manually
```bash
python -m web.core.manage runserver
```

OR (to make it reachable from other devices in your local network)

```bash
python -m web.core.manage runserver 0.0.0.0:8000 --insecure
```

### Run with make
If you have the `GNU make` executable in your path you can run all the commands listed in Makefile.

For example:
```bash
make runserver
```

### Run with VS Code (F5 shortcut)
Make sure you have set up the `launch.json` file in the `.vscode` directory
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Django",
            "type": "debugpy",
            "request": "launch",
            "module": "web.core.manage",
            "cwd": "${workspaceFolder}",
            "python": "${workspaceFolder}\\venv\\Scripts\\python.exe",
            "console": "integratedTerminal",
            "args": ["runserver", "0.0.0.0:8000", "--noreload", "--insecure"],
            "envFile": "${workspaceFolder}\\web\\.env\\dev.env",
            "django": true,
            "justMyCode": true
        },
        {
            "name": "Celery",
            "type": "debugpy",
            "request": "launch",
            "module": "celery",
            "cwd": "${workspaceFolder}",
            "console": "internalConsole",
            "args": ["-A", "project", "worker", "-l", "info", "-P", "solo"],
            "envFile": "${workspaceFolder}\\web\\.env\\dev.env",
        },
        {
            "name": "Beat",
            "type": "debugpy",
            "request": "launch",
            "module": "celery",
            "cwd": "${workspaceFolder}",
            "envFile": "${workspaceFolder}\\web\\.env\\dev.env",
            "console": "internalConsole",
            "args": ["-A", "project", "beat", "-l", "info"]
        }
    ],
    "compounds": [
        {
            "name": "Django-Celery",
            "configurations": ["Django", "Celery"],
            "stopAll": true
        },
        {
            "name": "Django-Celery-Beat",
            "configurations": ["Django", "Celery", "Beat"],
            "stopAll": true
        }
    ]
}
```

*NOTE: To select the configuration you need to debug, use the dropdown menu in the debug toolbar. (e.g. `Django-Celery` or `Django-Celery-Beat` for compound configurations or just `Django` or `Celery` or `Beat` for single configurations)*

---
