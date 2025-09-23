FROM  python:3.12.11-trixie

RUN apt update -y && apt install awscli -y

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install -upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install -y transformers accelerate

CMD ["streamlit run", "streamlit_app.py" ]


