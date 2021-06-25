
#ifndef SIGNALS_H
#define SIGNALS_H

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


/*******************************************************************************************/
/**************************************External Types***************************************/
/*******************************************************************************************/


/*******************************************************************************************/
/**************************************External Variables***********************************/
/*******************************************************************************************/


/*******************************************************************************************/
/**************************************External Functions***********************************/
/*******************************************************************************************/

extern "C"
{


    void EXT_API Sgn_SetValueLittleEndian(        /*set the value of a signal in a buffer with little endian*/
        uint8*        buffer,                     /*[IN] array of bytes*/
        uint64        size,                       /*[IN] size of the array of bytes*/
        uint64        value,                      /*[IN] value to set in array of bytes*/
        uint64        sb,                         /*[IN] start bit*/
        uint64        length);                    /*[IN] length*/

    uint64 EXT_API Sgn_GetValueLittleEndian(      /*get the value of a signal from a buffer with little endian*/
        uint8*        buffer,                     /*[IN] array of bytes*/
        uint64        size,                       /*[IN] size of the array of bytes*/
        uint64        sb,                         /*[IN] start bit*/
        uint64        length);                    /*[IN] length*/

    void EXT_API Sgn_SetValueBigEndian(           /*set the value of a signal in a buffer with big endian*/
        uint8*        buffer,                     /*[IN] array of bytes*/
        uint64        size,                       /*[IN] size of the array of bytes*/
        uint64        value,                      /*[IN] value to set in array of bytes*/
        uint64        sb,                         /*[IN] start bit*/
        uint64        length);                    /*[IN] length*/

    uint64 EXT_API Sgn_GetValueBigEndian(         /*get the value of a signal from a buffer with big endian*/
        uint8*        buffer,                     /*[IN] array of bytes*/
        uint64        size,                       /*[IN] size of the array of bytes*/
        uint64        sb,                         /*[IN] start bit*/
        uint64        length);                    /*[IN] length*/

}

#endif

