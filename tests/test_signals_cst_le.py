

"""******************************************************************************************
*********************************************************************************************
******************************************************************************************"""
TEST_DATA_LE = [
				{
					"name"  : "s1",
					"sb"    : 0,
					"length": 8,
					"value" : 170,
					"data"  : [
									0xAA,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 0 - 7
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 8 - 15
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 16 - 23
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 24 - 31
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 32 - 40
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 41 - 48
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 49 - 56
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 57 - 64
								]
				},
				{
					"name"  : "s2",
					"sb"    : 10,
					"length": 4,
					"value" : 10,
					"data"  : [
									0x00,0x28,0x00,0x00,0x00,0x00,0x00,0x00, # 0 - 7
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 8 - 15
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 16 - 23
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 24 - 31
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 32 - 40
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 41 - 48
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 49 - 56
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 57 - 64
								]
				},
				{
					"name"  : "s3",
					"sb"    : 16,
					"length": 12,
					"value" : 2730,
					"data"  : [
									0x00,0x00,0xAA,0x0A,0x00,0x00,0x00,0x00, # 0 - 7
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 8 - 15
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 16 - 23
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 24 - 31
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 32 - 40
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 41 - 48
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 49 - 56
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 57 - 64
								]
				},
				{
					"name"  : "s4",
					"sb"    : 29,
					"length": 13,
					"value" : 5461,
					"data"  : [
									0x00,0x00,0x00,0xA0,0xAA,0x02,0x00,0x00, # 0 - 7
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 8 - 15
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 16 - 23
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 24 - 31
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 32 - 40
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 41 - 48
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 49 - 56
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 57 - 64
								]
				},
				{
					"name"  : "s5",
					"sb"    : 0,
					"length": 32,
					"value" : 2863311530,
					"data"  : [
									0xAA,0xAA,0xAA,0xAA,0x00,0x00,0x00,0x00, # 0 - 7
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 8 - 15
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 16 - 23
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 24 - 31
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 32 - 40
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 41 - 48
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 49 - 56
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 57 - 64
								]
				},
				{
					"name"  : "s6",
					"sb"    : 2,
					"length": 5,
					"value" : 10,
					"data"  : [
									0x28,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 0 - 7
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 8 - 15
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 16 - 23
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 24 - 31
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 32 - 40
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 41 - 48
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 49 - 56
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 57 - 64
								]
				},
				{
					"name"  : "s7",
					"sb"    : 8,
					"length": 7,
					"value" : 42,
					"data"  : [
									0x00,0x2A,0x00,0x00,0x00,0x00,0x00,0x00, # 0 - 7
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 8 - 15
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 16 - 23
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 24 - 31
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 32 - 40
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 41 - 48
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 49 - 56
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 57 - 64
								]
				},
				{
					"name"  : "s8",
					"sb"    : 29,
					"length": 7,
					"value" : 85,
					"data"  : [
									0x00,0x00,0x00,0xA0,0x0A,0x00,0x00,0x00, # 0 - 7
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 8 - 15
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 16 - 23
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 24 - 31
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 32 - 40
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 41 - 48
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 49 - 56
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 57 - 64
								]
				},
				{
					"name"  : "s9",
					"sb"    : 39,
					"length": 23,
					"value" : 5592405,
					"data"  : [
									0x00,0x00,0x00,0x00,0x80,0xAA,0xAA,0x2A, # 0 - 7
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 8 - 15
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 16 - 23
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 24 - 31
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 32 - 40
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 41 - 48
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 49 - 56
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 57 - 64
								]
				},
				{
					"name"  : "s10",
					"sb"    : 21,
					"length": 32,
					"value" : 1431655765,
					"data"  : [
									0x00,0x00,0xA0,0xAA,0xAA,0xAA,0x0A,0x00, # 0 - 7
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 8 - 15
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 16 - 23
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 24 - 31
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 32 - 40
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 41 - 48
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 49 - 56
									0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # 57 - 64
								]
				},
			]