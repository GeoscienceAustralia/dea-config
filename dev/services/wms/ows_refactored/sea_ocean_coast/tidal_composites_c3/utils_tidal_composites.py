def tide_graph_path(data, ds):
    """
    Calculates an additional metadata field providing the
    URL to a graph used to visualise tide biases.
    """

    # Extract required data from datacube dataset
    base_dir = "https://dea-public-data-dev.s3-ap-southeast-2.amazonaws.com/derivative"
    product = ds.metadata_doc['properties']['odc:product']
    version = ds.metadata_doc['properties']['odc:dataset_version'].replace(".", "-")
    year = ds.metadata_doc['properties']['datetime'][:4]
    region = ds.metadata_doc['properties']['odc:region_code']
    region_split = region.replace("y", "/y")

    # Combine into a string
    return f"{base_dir}/{product}/{version}/{region_split}/{year}--P1Y/{product}_{region}_{year}--P1Y_final_tide_graph.png"