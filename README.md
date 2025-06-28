# OMQS Python Client

Access quantitative models from Outspoken Market Quant Services (OMQS) with a simple and intuitive Python client.

## 🚀 Installation

```bash
pip install git+https://github.com/outspokenmarket/omqs-python.git
```

## 🧠 Usage

```python
from omqs import OMQSClient

client = OMQSClient(api_key="your-api-key")

response = client.get_signal(
    model="crypto",
    ticker="BTCUSDT",
    timeframe="1h"
)

print(response)
```

---

## 📦 Request Parameters

| Parameter   | Type   | Description                                                                 |
|-------------|--------|-----------------------------------------------------------------------------|
| `model`     | string | Type of model: `"b3_stocks"`, `"crypto"`, `"forex"`, etc.                   |
| `ticker`    | string | Asset symbol depending on the model (e.g., `"PETR4"`, `"BTCUSDT"`)       |
| `timeframe` | string | Chart timeframe: `"1m"`, `"5m"`, `"15m"`, `"1h"`, `"4h"`, `"1d"`             |

---

## 📊 Available Models

| Model          | Description                                | Supported Assets Examples                                 |
|----------------|--------------------------------------------|-----------------------------------------------------------|
| `b3_stocks`    | Model for B3 stocks                        | `"PETR4"`, `"VALE3"`                                      |
| `crypto`       | Model for cryptocurrencies                 | `"BTCUSDT"`, `"ETHUSDT"`                                  |
| `forex`        | Model for currency pairs                   | `"EURUSD"`, `"GBPJPY"`                                    |
| `b3_futures`   | Model for B3 futures                       | `"WDO"`, `"WIN"`                                          |
| `us_futures`   | Model for US futures                       | `"MES"`, `"MNQ"`                                          |
| `international`| Model for Yahoo Finance tickers           | `"PETR4.SA"`, `"AAPL"`                                     |
| `nasdaq`       | Model for NASDAQ stocks                   | `"TSLA"`, `"NVDA"`                                        |
| `vix`          | Model for VIX index (no ticker or timeframe required) | N/A                                       |

---

## 📈 Signal Values

### General OMQS Models (except `vix`)

| Value | Interpretation           |
|-------|---------------------------|
| `1`   | Uptrend (Buy Signal)      |
| `0.5` | Neutral                   |
| `0`   | Downtrend (Sell Signal)   |

### VIX Model

| Value | Interpretation           |
|-------|---------------------------|
| `1`   | Uptrend (Buy Signal)      |
| `0`   | Neutral                   |

---

## 📝 License

MIT License

© 2025 Outspoken Market
