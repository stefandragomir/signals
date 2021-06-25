
/*******************************************************************************************/
/***********************************Dependencies********************************************/
/*******************************************************************************************/

#include "std_types.h"

/*******************************************************************************************/
/**************************************External DEFINES*************************************/
/*******************************************************************************************/


/*******************************************************************************************/
/**************************************External MACROS**************************************/
/*******************************************************************************************/

/*get a byte from a variable(stream)*/
#define SGN_GET_BYTE_FROM_STREAM(stream,index)        ((uint64)stream & ((uint64)0xFF <<(uint64)(8 * (index)))) >> (uint64)(8 * (index));

/*add a new byte in a variable(stream)*/
#define SGN_ADD_BYTE_TO_STREAM(stream,byte,index)     stream | ((uint64)((uint64)byte) << (uint64)(8 * (index)));

/*******************************************************************************************/
/**************************************External Types***************************************/
/*******************************************************************************************/

/*******************************************************************************************/
/**************************************External Variables***********************************/
/*******************************************************************************************/


/*******************************************************************************************/
/***************************Internal Functions Prototypes***********************************/
/*******************************************************************************************/

/*get signal little endian buffer parameters used for set and get*/
STATIC void Sgn_GetLittleEndian_Parameters(
    uint64 sb,
    uint64 length,
    uint64* startByte,
    uint64* nrBytes,
    uint64* extraBits);

/*get signal big endian buffer parameters used for set and get*/
STATIC void Sgn_GetBigEndian_Parameters(
    uint64 sb,
    uint64 length,
    uint64* startByte,
    uint64* nrBytes,
    uint64* extraBits);

/*******************************************************************************************/
/**************************************External Functions***********************************/
/*******************************************************************************************/

/***************************************************************/
/***************************************************************/
/***************************************************************/
STATIC void Sgn_GetLittleEndian_Parameters(uint64 sb, uint64 length, uint64* startByte, uint64* nrBytes, uint64* extraBits)
{

    uint64  lastByte;
    uint64  lb;

    lb = sb + (length - 1);
    *startByte = sb / 8;
    lastByte = lb / 8;
    *nrBytes = lastByte - (*startByte) + 1;
    *extraBits = sb % 8;
}

/***************************************************************/
/***************************************************************/
/***************************************************************/
STATIC void Sgn_GetBigEndian_Parameters(uint64 sb, uint64 length, uint64* startByte, uint64* nrBytes, uint64* extraBits)
{

    uint64  lastByte;
    uint64  nsb;
    uint64  nlb;

    nsb = 7 - (sb % 8) + (sb / 8) * 8;
    nlb = nsb - (length - 1);
    *extraBits = (8 - ((nsb + 1) % 8)) % 8;
    lastByte = nsb / 8;
    *startByte = nlb / 8;
    *nrBytes = lastByte - (*startByte) + 1;
}

/***************************************************************/
/***************************************************************/
/***************************************************************/
void EXT_API Sgn_SetValueLittleEndian(uint8* buffer, uint64 size, uint64 value, uint64 sb, uint64 length)
{

    uint64 mask;
    uint64 idx;
    uint64 stream;
    uint64 startByte;
    uint64 nrBytes;
    uint64 extraBits;
    uint8* signalBuffer;

    stream = 0;

    Sgn_GetLittleEndian_Parameters(sb, length, &startByte, &nrBytes, &extraBits);

    signalBuffer = &(buffer[startByte]);

    for (idx = 0; idx < nrBytes; idx++)
    {
        stream = SGN_ADD_BYTE_TO_STREAM(stream, signalBuffer[idx], idx)
    }

    mask = (((uint64)1U << length) - (uint64)1U) << extraBits;

    stream = (stream & ~mask) | (mask & (value << extraBits));

    for (idx = 0; idx < nrBytes; idx++)
    {
        signalBuffer[idx] = SGN_GET_BYTE_FROM_STREAM(stream, idx);
    }
}

/***************************************************************/
/***************************************************************/
/***************************************************************/
uint64 EXT_API Sgn_GetValueLittleEndian(uint8* buffer, uint64 size, uint64 sb, uint64 length)
{
    uint64 value;
    uint64 mask;
    uint64 idx;
    uint64  startByte;
    uint64  nrBytes;
    uint64  extraBits;
    uint8* signalBuffer;

    value = 0U;

    Sgn_GetLittleEndian_Parameters(sb, length, &startByte, &nrBytes, &extraBits);

    signalBuffer = &(buffer[startByte]);

    for (idx = 0; idx < nrBytes; idx++)
    {
        value = SGN_ADD_BYTE_TO_STREAM(value, signalBuffer[idx], idx)
    }

    value = value >> extraBits;
    mask = (((uint64)1U << length) - (uint64)1U);
    value = value & mask;

    return value;
}

/***************************************************************/
/***************************************************************/
/***************************************************************/
void EXT_API Sgn_SetValueBigEndian(uint8* buffer, uint64 size, uint64 value, uint64 sb, uint64 length)
{
    uint64 mask;
    uint64 idx;
    uint64 stream;
    uint64  startByte;
    uint64  nrBytes;
    uint64  extraBits;
    uint8* signalBuffer;

    stream = 0U;

    Sgn_GetBigEndian_Parameters(sb, length, &startByte, &nrBytes, &extraBits);

    signalBuffer = &(buffer[startByte]);

    for (idx = 0; idx < nrBytes; idx++)
    {
        value = SGN_ADD_BYTE_TO_STREAM(value, signalBuffer[idx], nrBytes - idx - 1)
    }

    mask = (((uint64)1U << length) - (uint64)1U) << extraBits;

    stream = (stream & ~mask) | (mask & (value << extraBits));

    for (idx = 0; idx < nrBytes; idx++)
    {

        signalBuffer[nrBytes - idx - 1] = SGN_GET_BYTE_FROM_STREAM(stream, idx);
    }
}

/***************************************************************/
/***************************************************************/
/***************************************************************/
uint64 EXT_API Sgn_GetValueBigEndian(uint8* buffer, uint64 size, uint64 sb, uint64 length)
{
    uint64 idx;
    uint64 value;
    uint64 mask;
    uint64  startByte;
    uint64  nrBytes;
    uint64  extraBits;
    uint8* signalBuffer;

    value = 0U;

    Sgn_GetBigEndian_Parameters(sb, length, &startByte, &nrBytes, &extraBits);

    signalBuffer = &(buffer[startByte]);

    for (idx = 0; idx < nrBytes; idx++)
    {
        value = SGN_ADD_BYTE_TO_STREAM(value, signalBuffer[idx], nrBytes - idx - 1)
    }

    mask = (((uint64)1U << length) - (uint64)1U) << extraBits;

    value = (value & mask) >> extraBits;

    return value;
}
