FROM ubuntu
RUN apt update && apt install -yy git curl
RUN curl -sSf https://rye-up.com/get | RYE_NO_AUTO_INSTALL=1 RYE_INSTALL_OPTION="--yes" bash
ADD . /albatross
WORKDIR /albatross
RUN /root/.rye/shims/rye sync
RUN /root/.rye/shims/python src/albatross/main.py
# .venv/lib/python3.11/site-packages/_pypi_provider.pth is empty