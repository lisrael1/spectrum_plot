from spectrum_plot.plotting import Plot


def create_fft_plot(figsize=(12, 4), add_musical_notes=False, save_path=None):
    return Plot(figsize=figsize, add_musical_notes=add_musical_notes, save_path=save_path)


create_fft_plot.__doc__ = Plot.__init__.__doc__

