# Byte Buffer Signal Manipulation Functions

Function for extracting and setting 32 bit values in byte buffers.

Buffer size is not limited only signal size is limited to 32 bit.

Library is written in C/C++, built to a DLL wrapped in python code using ctypes.

* Sgn_SetValueLittleEndian (Intel Format)

* Sgn_GetValueLittleEndian (Intel Format)

* Sgn_SetValueBigEndian (Motorola Format)

* Sgn_GetValueBigEndian (Motorola Format)

Signals are described by Start Bit and Length.

