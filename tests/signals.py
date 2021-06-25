
from   ctypes import CDLL 
from   ctypes import c_uint8
from   ctypes import c_uint64
from   ctypes  import POINTER

dll   = CDLL("signals.dll") 

"""******************************************************************************************
*********************************************************************************************
******************************************************************************************"""

dll.Sgn_SetValueLittleEndian.argtypes              = (POINTER(c_uint8), c_uint64, c_uint64, c_uint64, c_uint64)

dll.Sgn_SetValueBigEndian.argtypes                 = (POINTER(c_uint8), c_uint64, c_uint64, c_uint64, c_uint64)

dll.Sgn_GetValueLittleEndian.restype               = c_uint64
dll.Sgn_GetValueLittleEndian.argtypes              = (POINTER(c_uint8), c_uint64, c_uint64, c_uint64)

dll.Sgn_GetValueBigEndian.restype                  = c_uint64
dll.Sgn_GetValueBigEndian.argtypes                 = (POINTER(c_uint8), c_uint64, c_uint64, c_uint64)

"""******************************************************************************************
*********************************************************************************************
******************************************************************************************"""
def Sgn_SetValueLittleEndian(data,value,sb,length):

    _size     = len(data)
    _c_size   = c_uint64(_size)
    _c_arr    = (c_uint8 * _size)(*data)
    _c_sb     = c_uint64(sb)
    _c_length = c_uint64(length)
    _c_value  = c_uint64(value)

    _value = dll.Sgn_SetValueLittleEndian(
                                            _c_arr,
                                            _c_size,
                                            _c_value,
                                            _c_sb,
                                            _c_length)

    _p_lst  = [] 

    for _value in _c_arr:
        _p_lst.append(_value)

    return _p_lst[:_size]

"""******************************************************************************************
*********************************************************************************************
******************************************************************************************"""
def Sgn_SetValueBigEndian(data,value,sb,length):

    _size     = len(data)
    _c_size   = c_uint64(_size)
    _c_arr    = (c_uint8 * _size)(*data)
    _c_sb     = c_uint64(sb)
    _c_length = c_uint64(length)
    _c_value  = c_uint64(value)

    _value = dll.Sgn_SetValueBigEndian(
                                            _c_arr,
                                            _c_size,
                                            _c_value,
                                            _c_sb,
                                            _c_length)

    _p_lst  = [] 

    for _value in _c_arr:
        _p_lst.append(_value)

    return _p_lst[:_size]

"""******************************************************************************************
*********************************************************************************************
******************************************************************************************"""
def Sgn_GetValueLittleEndian(data,sb,length):

    _size     = len(data)
    _c_size   = c_uint64(_size)
    _c_arr    = (c_uint8 * _size)(*data)
    _c_sb     = c_uint64(sb)
    _c_length = c_uint64(length)

    _value = dll.Sgn_GetValueLittleEndian(
                                            _c_arr,
                                            _c_size,
                                            _c_sb,
                                            _c_length)

    return int(_value)

"""******************************************************************************************
*********************************************************************************************
******************************************************************************************"""
def Sgn_GetValueBigEndian(data,sb,length):

    _size     = len(data)
    _c_size   = c_uint64(_size)
    _c_arr    = (c_uint8 * _size)(*data)
    _c_sb     = c_uint64(sb)
    _c_length = c_uint64(length)

    _value = dll.Sgn_GetValueBigEndian(
                                            _c_arr,
                                            _c_size,
                                            _c_sb,
                                            _c_length)

    return int(_value)
