conda create -n rasaenv_3810 python==3.8.10 -y
conda activate rasaenv_3810
pip install rasa==3.4.2
pip install truecase
pip install spacy
export PYTHONIOENCODING=utf-8
pip install websockets==10.0
pip install pydantic --upgrade
python -m spacy download en_core_web_md
python -m nltk.downloader popular
