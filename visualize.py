import matplotlib.pyplot as plt


def plot_segment_counts(segment_summary):
    """Plot customer counts by segment and return the figure and axes."""
    if "customer_count" not in segment_summary.columns:
        raise ValueError("segment_summary must contain a 'customer_count' column")

    figure, axis = plt.subplots(figsize=(8, 4))
    bars = axis.bar(
        segment_summary.index.astype(str),
        segment_summary["customer_count"],
        color="#2F7F78",
    )
    axis.set_title("Customers by segment")
    axis.set_xlabel("Segment")
    axis.set_ylabel("Number of customers")
    axis.bar_label(bars)
    figure.tight_layout()
    return figure, axis