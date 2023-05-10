from spectrum_plot import create_fft_plot
import sounddevice as sd


def short_record(seconds=0.5, debug=False):
    # Duration of recording
    fs = 44100 / 10  # Sample rate
    fs = 1000
    if debug:
        print('recording')
    delay_time = 0.7
    sound = sd.rec(frames=int((seconds + delay_time) * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    sound = sound[int(delay_time * fs):]

    if debug:
        print('done')
    if 0:
        scipy.io.wavfile.write('del.wav', fs, sound)  # Save as WAV file
    return sound


plot = create_fft_plot(add_musical_notes=True)
seconds = 0.5
while True:
    sound = short_record(seconds)
    plot.update_raw_data(sound.mean(1), seconds=seconds)
