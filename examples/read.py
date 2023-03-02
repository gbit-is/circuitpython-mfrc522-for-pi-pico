import time
import board
import mfrc522


miso = board.GP4
cs  = board.GP5
sck = board.GP6
mosi = board.GP7
rst = board.GP8

rfid = mfrc522.MFRC522(sck,mosi,miso, rst, cs)
rfid.set_antenna_gain(0x07 << 4)


print("\n***** Scan your RFid tag/card *****\n")

prev_data = ""
prev_time = 0
timeout = 1

while True:
    
    (status, tag_type) = rfid.request(rfid.REQALL)

    if status == rfid.OK:
        (status, raw_uid) = rfid.anticoll()

        if status == rfid.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])

            if rfid_data != prev_data:
                prev_data = rfid_data

                print("Card detected! UID: {}".format(rfid_data))
            prev_time = time.monotonic()

    else:
        if time.monotonic() - prev_time > timeout:
            prev_data = ""
