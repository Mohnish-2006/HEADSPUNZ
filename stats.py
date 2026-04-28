from datetime import datetime

stats_data = []

def add_stat(count):
    stats_data.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "count": count
    })


def get_stats():
    return stats_data


def get_suggestion():

    if not stats_data:
        return "No audience data yet"

    peak = max(
        stats_data,
        key=lambda x: x["count"]
    )

    return f"Best time to advertise is around {peak['time']}"