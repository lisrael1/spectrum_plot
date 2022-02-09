from unittest import TestCase
from spectrum_plot import create_fft_plot


class Test(TestCase):
    def create_fft_plot(self):
        """
        only checking that it compiles
        :return:
        """
        try:
            plot = create_fft_plot()
            plot.update_raw_data([1, 2, 3, 4, 5], seconds=3)
        except Exception as e:
            self.fail(e)

