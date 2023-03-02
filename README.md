# circuitpython-mfrc522

Minor edit to domdfcoding's mfrc522 library to use it with raspberry pi pico, micropython

Also, the read.py is mostly stolen from [idriszmy](https://gist.github.com/idriszmy/9fa14377eb3b5a1859e1ff4f41464900#file-code-py), which is based of domdfcodings 

## Usage

Put the module ``mfrc522.py`` in the /lib/ folder on pi pico 

I used the following pins for my setup:

| Signal    | GPIO pi pico | Label on RC522 |
| --------- | ------------ | -------------- | 
| MISO      | GP.4         | "MISO"         | 
| CS        | GP.5         | "SDA or NSS"   |
| SCK       | GP.6         | "SCK"          |
| MOSI      | GP.7         | "MOSI"         |
| RST       | GP.8         | "RST"          |
| VCC       | 3.3V         | "VCC"          |
| GND       | GND          | "GND"          |


now try to scan a card using read.py 



## Original usage documentation:
### I haven't tried these 

Now enter the REPL you could run one of the two examples:

For detecting, authenticating and reading from a card:

    import read
    read.do_read()

This will wait for a MifareClassic 1k card. As soon the card is detected, it is authenticated, and
16 bytes are read from address 0x08.

For detecting, authenticating and writing to a card:

    import write
    write.do_write()

This will wait for a MifareClassic 1k card. As soon the card is detected, it is authenticated, and
16 bytes written to address 0x08.
