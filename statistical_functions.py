
#### mean_confidence_interval
import numpy as np
from scipy.stats import t, sem

def mean_confidence_interval(data: list, confidence_level = 0.95):
    mean = data.mean()
    std_err = data.std()
    critical_value = t.ppf((1 + confidence_level) / 2, len(data) - 1)
    margin_of_error = critical_value * std_err
    confidence_interval = (mean - margin_of_error, mean + margin_of_error)
    return confidence_interval
