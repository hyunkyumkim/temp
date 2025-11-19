from machine import Pin, UART
import utime

uart0 = UART(0, baudrate=460800, tx=Pin(0), rx=Pin(1))

while True:
    data_to_send = '$abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789%\r\n'
    uart0.write(data_to_send)
    print(f"[UART0] Sent: {data_to_send}")
    uart0_data = uart0.read()
    if uart0_data:
        print("[UART0] Received:", uart0_data)
#        if uart0_data.startswith(b'*'):
#            uart0.write("Unknown OTA request\r\n")
#            print("[UART0] Sent: Unknown OTA request\r\n")
#        if b'CMD10*' in uart0_data:
#            uart0.write("Command received: CMD10\r\nPCBA - SN: a\r\nPCBA - LOT: b\r\nPCBA - REF: c\r\nReader - SN: d\r\nReader - LOT: e\r\nReader - REF: f\r\nDevice Name: g\r\nManufacturer: h\r\nFCC: i\r\nMCU Firmware Version: j\r\n355 Firmware Version: k\r\nChip Config Version: l\r\nAssay Manager Version: m\r\nFirmware Part Number: n\r\nReserved Two: o\r\nReserved Three: p\r\nDevice meta data report done!\r\n")
#            print("[UART0] Sent: Command received: CMD10\r\nPCBA - SN: a\r\nPCBA - LOT: b\r\nPCBA - REF: c\r\nReader - SN: d\r\nReader - LOT: e\r\nReader - REF: f\r\nDevice Name: g\r\nManufacturer: h\r\nFCC: i\r\nMCU Firmware Version: j\r\n355 Firmware Version: k\r\nChip Config Version: l\r\nAssay Manager Version: m\r\nFirmware Part Number: n\r\nReserved Two: o\r\nReserved Three: p\r\nDevice meta data report done!\r\n")
    else:
        print("[UART0] Received: None")
    print("=====")
    utime.sleep(1)

