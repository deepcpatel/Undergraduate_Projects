- The code is built in Python 2.7 and tested on Ubuntu 16.04 and Ubuntu 17.04
- Development is in progress, however you can test the current version
- The code is MIDI based, thus you can use it with MIDI keyboard or Virtual MIDI events generater (E.g. VMPK)
- A guide to install dependencies:

  1).sudo apt-get install python-dev python-numpy python-setuptools libsndfile-dev   -> Python Libraries<br />
  2).sudo apt-get install libasound2-dev                                             -> ALSA Header<br />
  3).sudo pip install scikits.audiolab                                               -> For importing wav file<br />
  4).sudo apt-get install libsamplerate0 libsamplerate0-dev                          -> Dependency for scikits.samplerate<br />
  5).sudo pip install scikits.samplerate                                             -> For Re-Sampling the audio file<br />
  6).sudo pip install pygame                                                         -> Main for Handler<br />
  7).sudo apt-get install libjack-dev                                                -> Dependency for python-rtmidi<br />
  8).sudo pip install python-rtmidi                                                  -> Dependency for MIDO<br />
  9).sudo pip install mido                                                           -> For MIDI Keys detection<br />
  10).sudo apt-get install python-pyqt5                                              -> PyQT-5 GUI Toolkit<br />
  11).sudo pip install pyinstaller                                                   -> To make executable file<br />