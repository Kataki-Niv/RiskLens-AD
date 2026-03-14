def classify_risk(probability):
    """
    Classify Alzheimer's risk using probability thresholds.
    """

    if probability < 0.35:
        return "Low Risk (Confident)"
    elif probability <= 0.65:
        return "Uncertain / Needs Monitoring"
    else:
        return "High Risk (Confident)"
