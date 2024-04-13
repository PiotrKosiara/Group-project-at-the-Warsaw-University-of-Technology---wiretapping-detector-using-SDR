from time import sleep
from rtlsdr import RtlSdr
import numpy as np
from final_gui import *


sdr = RtlSdr()
sdr.sample_rate = 2.5e6
sdr.freq_correction = 60
sdr.gain = 5


def sweep(start_freq, end_freq, step):
    print("===========Starting sweep================")
    for freq in range(start_freq, end_freq, step):
        sdr.center_freq = freq
        samples = sdr.read_samples(256*1024)
        Amax = 0
        for sample in samples:
            p = np.abs(sample)
            if p > Amax:
                Amax = p

        p = 20*np.log10(Amax)
        print(f"Pmax = {p}")
        window.update_led(p)
        QApplication.processEvents()
        sleep(0.1)


if __name__ == "__main__":
    app = QApplication([])
    window = LED()
    window.show()

    start_freq = 432*10**6
    end_freq = 435*10**6
    step = 1*10**5

    while True:
        sweep(start_freq, end_freq, step)