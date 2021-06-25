
#ifndef SIGNALS_STDTYPES_H
#define SIGNALS_STDTYPES_H

#include <Windows.h>


/*Declare a function external*/
#define EXT_API					__declspec(dllexport)	

/*Static definition*/
#define STATIC					static

/*unsigned types are enharited from Windows*/
/*--------------------------------------------------------------*/
typedef UINT8    uint8;
typedef UINT16   uint16;
typedef UINT32   uint32;
typedef UINT64   uint64;


#endif