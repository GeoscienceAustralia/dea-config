from datacube_ows.band_utils import scalable


@scalable
def brovey_pansharpen(data,
                      output_band,
                      red_band="nbart_red",
                      green_band="nbart_green",
                      blue_band="nbart_blue",
                      pan_band='nbart_panchromatic'):

    # Calculate total
    da_total = data[[red_band, green_band, blue_band]].to_array().sum(dim="variable")

    # Perform Brovey Transform in form of: band / total * panchromatic
    data_pansharpened = data[[red_band, green_band, blue_band]] / da_total * data[pan_band]

    return data_pansharpened[output_band]
