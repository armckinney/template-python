<!-- header -->
<div align="center">
    <p>
    <!-- Header -->
        <img width="100px" src="./ini/readme_logo.png"  alt="template-python" />
        <h2>template-python</h2>
        <p><i>cool-template-python-tagline</i></p>
    </p>
    <p>
    <!-- Shields -->
        <a href="https://github.com/armckinney/template-python/LICENSE">
            <img alt="License" src="https://img.shields.io/github/license/armckinney/template-python.svg" />
        </a>
        <a href="https://codecov.io/gh/armckinney/template-python">
            <img alt="Code Coverage" src="https://codecov.io/gh/armckinney/template-python/branch/master/graph/badge.svg" />
        </a>
        <a href="https://github.com/armckinney/template-python/issues">
            <img alt="Issues" src="https://img.shields.io/github/issues/armckinney/template-python" />
        </a>
        <a href="https://github.com/armckinney/template-python/pulls">
            <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/armckinney/template-python" />
        </a>
    </p>
    <p>
    <!-- Links -->
        <a href="https://github.com/armckinney/template-python/issues/new/choose">Report Bug</a>
        ·
        <a href="https://github.com/armckinney/template-python/issues/new/choose">Request Feature</a>
    </p>
</div>
<br>
<br>

<!-- Description -->
`template-python` is a starter repository for Python projects with a modern `src/` layout, test scaffolding, and deployment helpers.

The `template-python` repository adds some nifty and time-saving features like:
- *All of the benefits of [template-ubuntu](https://github.com/armckinney/template-ubuntu) PLUS..*
- Various Python Development tools 
    - Environments and dependency management via `uv`
    - Build backend via `uv_build`
    - Static analysis and formatting via `ruff`
    - Type checking via `ty`
    - Testing Framework via Pytest
- Github Python Workflows
    - Linting
    - Testing
- Azure Container App Deployment
- Template Files for
    - Python Development Tool Initialization
        - `pyproject.toml`
        - `Makefile`
        - `conftest.py`
    - Initial Python Project
        - `/src/<project>/`
        - `/tests/`
        - `/docs/`


### Quick Start

1. ###### Configure the init script:
This will allow you make quick changes to the template files that format them specifically for your project.
Do this by filling out the `.\ini\config\config.ini.json` with your own preferences.

2. ###### Run the init script:
This will allow you to auto-magically replace the `template-repo` name in the template files as well as configure the `ProjectLogo` image.

```powershell
./Initialize-TemplateRepository.ps1
```

*Note:* The project parent directory should match the GitHub repository name.

3. ###### Clean up what you don't want:
Some items you might want to get rid of/update:
- `./ini/` directory and its contents
- Description, Quick Start, and Usage in this `README` file
- The lint / test jobs in `..github/workflows/ci.yml`

4. ###### Commit and Push your changes to GitHub:
This should update all of your badges, links, images, as well as run the inital CI workflow.


### Usage

Common local commands:

```bash
make format   # uv run ruff format .
make lint     # uv run ruff check . && uv run ty check .
make test     # uv run pytest .
make build    # uv build
make publish  # uv publish
```

You can also run tools directly with `uv run`, for example `uv run pytest tests/sneks/test_snek.py`.

