FROM armck/python:3.12.3

LABEL   deployable="true" \
        decription="This is the deployable version of the WEF application container. \
                    It only includes nessecary items to run the application."

ARG WORKSPACE=/workspaces/template-python
WORKDIR ${WORKSPACE}

# avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# bring project files into container
COPY *.lock pyproject.toml ${WORKDIR}/
COPY ./src/snek_case ${WORKDIR}/src/snek_case

RUN cd $WORKDIR/ && uv sync --no-project-install

# exec commands do not run in shell by default (See: https://docs.docker.com/engine/reference/builder/#cmd)
CMD ["/bin/bash", "-c", "uv run uvicorn snek_case.main:app --host 0.0.0.0 --port 8008"]