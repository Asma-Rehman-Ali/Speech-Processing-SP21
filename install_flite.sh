wget http://tts.speech.cs.cmu.edu/awb/flite-2.0.5-current.tar.bz2 -O - | tar xj
mv flite-2.0.5-current flite
cd flite && ./configure && make
cd flite && sudo make install
cd flite/testsuite && make lex_lookup
sudo cp flite/testsuite/lex_lookup /usr/local/bin

