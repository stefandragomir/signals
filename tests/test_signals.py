
from signals             import *
from test_signals_cst_le import TEST_DATA_LE
from test_signals_cst_be import TEST_DATA_BE


"""******************************************************************************************
*********************************************************************************************
******************************************************************************************"""
def test_Sgn_GetValueLittleEndian():

	print("-------------------------------------------------------")

	for _signal in TEST_DATA_LE:

		_data = [
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 0 - 7
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 8 - 15
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 16 - 23
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 24 - 31
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 32 - 40
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 41 - 48
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 49 - 56
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 57 - 64
				]

		print("Sgn_GetValueLittleEndian: name [%s] startbit [%s] length [%s] expected value [%s]" % (_signal["name"],_signal["sb"],_signal["length"],_signal["value"]))

		_value = Sgn_GetValueLittleEndian(_data, _signal["sb"], _signal["length"])

		print("Sgn_GetValueLittleEndian: returned value dec [%s] hex [%s] bin [%s]" % (_value,hex(_value),bin(_value)))

		if _value == _signal["value"]:
			print("Sgn_GetValueLittleEndian: OK")
		else:
			raise Exception("Sgn_GetValueLittleEndian: NOK")

		print("-------------------------------------------------------")

"""******************************************************************************************
*********************************************************************************************
******************************************************************************************"""
def test_Sgn_SetValueLittleEndian():

	print("-------------------------------------------------------")

	for _signal in TEST_DATA_LE:

		_data = [
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 0 - 7
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 8 - 15
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 16 - 23
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 24 - 31
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 32 - 40
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 41 - 48
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 49 - 56
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 57 - 64
				]

		print("Sgn_SetValueLittleEndian: name [%s] startbit [%s] length [%s] value [%s]" % (_signal["name"],_signal["sb"],_signal["length"],_signal["value"]))

		_data = Sgn_SetValueLittleEndian(_data, _signal["value"], _signal["sb"], _signal["length"])

		print("Sgn_SetValueLittleEndian: %s " % ' '.join([hex(_byte) for _byte in _data]))

		if len([_byte for _byte in _data + _signal["data"] if _byte not in _data or _byte not in _signal["data"]]) == 0:
			print("Sgn_SetValueLittleEndian: OK")
		else:
			raise Exception("Sgn_SetValueLittleEndian: NOK")
		print("-------------------------------------------------------")

"""******************************************************************************************
*********************************************************************************************
******************************************************************************************"""
def test_Sgn_GetValueBigEndian():

	print("-------------------------------------------------------")

	for _signal in TEST_DATA_BE:

		_data = [
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 0 - 7
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 8 - 15
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 16 - 23
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 24 - 31
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 32 - 40
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 41 - 48
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 49 - 56
					0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA,0xAA, # 57 - 64
				]

		print("Sgn_GetValueBigEndian: name [%s] startbit [%s] length [%s] expected value [%s]" % (_signal["name"],_signal["sb"],_signal["length"],_signal["value"]))

		_value = Sgn_GetValueBigEndian(_data, _signal["sb"], _signal["length"])

		print("Sgn_GetValueBigEndian: returned value dec [%s] hex [%s] bin [%s]" % (_value,hex(_value),bin(_value)))

		if _value == _signal["value"]:
			print("Sgn_GetValueBigEndian: OK")
		else:
			raise Exception("Sgn_GetValueBigEndian: NOK")

		print("-------------------------------------------------------")

"""******************************************************************************************
*********************************************************************************************
******************************************************************************************"""
def test_Sgn_SetValueBigEndian():

	print("-------------------------------------------------------")

	for _signal in TEST_DATA_BE:

		_data = [
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 0 - 7
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 8 - 15
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 16 - 23
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 24 - 31
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 32 - 40
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 41 - 48
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 49 - 56
					0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 57 - 64
				]

		print("Sgn_SetValueBigEndian: name [%s] startbit [%s] length [%s] value [%s]" % (_signal["name"],_signal["sb"],_signal["length"],_signal["value"]))

		_data = Sgn_SetValueBigEndian(_data, _signal["value"], _signal["sb"], _signal["length"])

		print("Sgn_SetValueBigEndian: %s " % ' '.join([hex(_byte) for _byte in _data]))

		if len([_byte for _byte in _data + _signal["data"] if _byte not in _data or _byte not in _signal["data"]]) == 0:
			print("Sgn_SetValueBigEndian: OK")
		else:
			raise Exception("Sgn_SetValueBigEndian: NOK")
		print("-------------------------------------------------------")

"""******************************************************************************************
*********************************************************************************************
******************************************************************************************"""
if __name__ == "__main__":

	test_Sgn_GetValueLittleEndian()

	test_Sgn_SetValueLittleEndian()

	test_Sgn_GetValueBigEndian()

	test_Sgn_SetValueBigEndian()