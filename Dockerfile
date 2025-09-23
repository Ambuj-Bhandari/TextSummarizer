FROM  python:3.12.11-trixie

RUN apt update -y && apt install awscli -y

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --root-user-action=ignore
RUN pip install -upgrade accelerate --root-user-action=ignore
RUN pip uninstall -y transformers accelerate --root-user-action=ignore
RUN pip install -y transformers accelerate --root-user-action=ignore

CMD ["streamlit run", "streamlit_app.py" ]


