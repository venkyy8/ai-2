mkdir -p data indicators intelligence learning output utils

touch main.py config.py
touch data/data_provider.py
touch indicators/technicals.py indicators/candlestick.py
touch intelligence/confidence_engine.py
touch intelligence/decision_engine.py
touch intelligence/risk_engine.py
touch learning/memory.py
touch requirements.txt

apt update
apt install -y python3.14-venv
python3 --version
python3 -m venv venv

python3 -m venv venv
source venv/bin/activate
deactivate
pip install --upgrade pip
pip install -r requirements.txt


python main.py



#directory Structure
AI-Agent-SM/
│
├── main.py
├── requirements.txt
├── config.py
│
├── data/
│   ├── __init__.py
│   ├── data_provider.py
│   ├── news_fetcher.py
│   └── sentiment_analyzer.py
│
├── indicators/
│   ├── __init__.py
│   ├── technicals.py
│   ├── candlestick.py
│   ├── support_resistance.py
│   └── volume_analysis.py
│
├── intelligence/
│   ├── __init__.py
│   ├── market_structure.py
│   ├── decision_engine.py
│   ├── confidence_engine.py
│   └── risk_engine.py
│
├── learning/
│   ├── __init__.py
│   ├── memory.py
│   ├── backtester.py
│   └── trainer.py
│
├── output/
│   ├── signals.csv
│   └── trade_memory.csv
│
└── utils/
    ├── __init__.py
    └── logger.py


#
