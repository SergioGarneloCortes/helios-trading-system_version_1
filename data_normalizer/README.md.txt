# Helios-Trading Module 5 - Data Normalizer

## Objective

Normalize data to a common scale for effective comparison and combination.

## Technologies

- Python
- NumPy

## Usage

### Normalizing Stock Prices

```python
from data_normalizer import DataNormalizer

prices = [100, 120, 90, 110, 130]
normalizer = DataNormalizer()
normalized_prices = normalizer.fit_transform(prices)
print(normalized_prices)