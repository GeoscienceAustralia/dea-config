fc_percentile_flags = [
    {
        "band": "land",
        "product": "geodata_coast_100k",
        "ignore_time": True,
        "ignore_info_flags": [],
    },
]

fc_percentile_pq_mask = [
    {
        "band": "land",
        "invert": True,
        "values": [0],
    },
]
