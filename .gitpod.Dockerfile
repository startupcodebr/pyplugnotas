FROM gitpod/workspace-postgres

RUN sudo apt-get update \
    && sudo apt-get install -y --no-install-recommends build-essential cmake git \
    libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev \
    libpq-dev curl wget vim gettext locales libmemcached-dev zlib1g-dev graphviz \
    && sudo apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && sudo rm -rf /var/lib/apt/lists/* \
    && sudo locale-gen pt_BR.UTF-8 \
    && sudo sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen \
    && sudo dpkg-reconfigure --frontend=noninteractive locales \
    && sudo update-locale LANG=pt_BR.UTF-8 \
    && sudo python3 -m pip install --upgrade pip \
    && pip install poetry