import copy

# HACK: Move this to a utils to allow style reusability
def swap_scale(new_scale: list, style: dict):
    if "scale_range" in style:
        new_style = copy.copy(style)
        new_style["scale_range"] = new_scale
        return new_style
    return style
