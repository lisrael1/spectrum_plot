import pylab as plt
import numpy as np
import pandas as pd
from freq_note_converter import from_freq, from_note_index


class Plot:
    def __init__(self, figsize=(12, 4), add_musical_notes=False, save_path=None):
        """
            creating dynamic pylab plot, that is showing fft plot, and updating it on every update_raw_data call.
            for example:
                plot = Plot()
                n = 200
                seconds = 0.1
                t = np.linspace(0, seconds, n)
                nyquist = n / seconds / 2
                for freq in np.linspace(0, nyquist, 100):
                    sine = np.sin(2 * np.pi * t * freq)
                    plot.update_raw_data(sine, seconds=seconds)
        :param figsize: the size of the fft pylab plot.
        :param add_musical_notes: additional feature, to add vertical red lines on frequencies of musical notes.
        """
        self.fft = pd.Series
        self.raw_data = list()
        self.save_path = save_path
        self.nyquist = None
        self.seconds = None
        self.n = None
        self.image_index = 0
        self.max_xy_value = [0, 0]

        self.add_musical_notes = add_musical_notes

        self.no_axis = False
        fig, self.ax = plt.subplots(1, 1, figsize=figsize)
        plt.ion()
        plt.show()

    def update_raw_data(self, raw_data, seconds):
        self.raw_data = raw_data
        self.n = len(raw_data)
        self.seconds = seconds
        self.nyquist = self.n / self.seconds / 2

        time_between_samples = self.seconds / self.n
        amp = np.fft.rfft(raw_data)
        freq = np.fft.rfftfreq(n=self.n, d=time_between_samples)
        self.fft = pd.Series(amp, index=freq).abs() * 2 / self.n
        self._update_image()

    def _update_image(self):
        self._clear_image()
        if self.add_musical_notes:
            self._add_notes()
        self._plot_fft()

    def _clear_image(self):
        self.ax.clear()
        self.ax.grid(True)
        self.ax.set_xlabel('Freq Hz')
        self.ax.set_ylabel('Sine Amplitude')
        if self.no_axis:
            self.ax.set(xticks=[], yticks=[])
            self.ax.axis('off')

    def _plot_fft(self):
        if self.fft.index[-1] > self.max_xy_value[0]:
            self.max_xy_value[0] = self.fft.index[-1]
        if self.fft.values.max() > self.max_xy_value[1]:
            self.max_xy_value[1] = self.fft.values.max()
        self.ax.set_xlim(0, self.max_xy_value[0])
        self.ax.set_ylim(0, self.max_xy_value[1])
        self.ax.plot(self.fft.index, self.fft.values)
        plt.draw()
        plt.pause(0.001)
        if self.save_path is not None:
            plt.savefig(f'{self.save_path}/fft_{self.image_index:0>5}.jpg')
            self.image_index += 1

    def _add_notes(self):
        max_note_index = from_freq(self.nyquist)
        if max_note_index.offset_from_note > 0:
            max_note_index = max_note_index.note_index - 1
        else:
            max_note_index = max_note_index.note_index
        for note_index in range(1, max_note_index):
            note = from_note_index(note_index)
            self.ax.axvline(note.freq, color='red')
            self.ax.text(note.freq, 0, note.note, color='red', verticalalignment='top')

