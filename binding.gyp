{
	'targets': [
		{
			'target_name': 'uws',
			'sources': [
				'uWebSockets/src/Extensions.cpp',
				'uWebSockets/src/Group.cpp',
				'uWebSockets/src/Networking.cpp',
				'uWebSockets/src/Hub.cpp',
				'uWebSockets/src/Node.cpp',
				'uWebSockets/src/WebSocket.cpp',
				'uWebSockets/src/HTTPSocket.cpp',
				'uWebSockets/src/Socket.cpp',
				'src/addon.cpp'
			],
			'conditions': [
				['OS=="linux"', {
					'cflags_cc': [ '-std=c++11', '-DUSE_LIBUV' ],
					'cflags_cc!': [ '-fno-exceptions', '-std=gnu++0x', '-fno-rtti' ],
					'cflags!': [ '-fno-omit-frame-pointer' ],
					'ldflags!': [ '-rdynamic' ],
					'ldflags': [ '-s' ]
				}],
				['OS=="mac"', {
					'xcode_settings': {
						'MACOSX_DEPLOYMENT_TARGET': '10.7',
						'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
						'CLANG_CXX_LIBRARY': 'libc++',
						'GCC_GENERATE_DEBUGGING_SYMBOLS': 'NO',
						'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
						'GCC_THREADSAFE_STATICS': 'YES',
						'GCC_OPTIMIZATION_LEVEL': '3',
						'GCC_ENABLE_CPP_RTTI': 'YES',
						'OTHER_CFLAGS!': [ '-fno-strict-aliasing' ],
						'OTHER_CPLUSPLUSFLAGS': [ '-DUSE_LIBUV' ]
					}
				}],
				['OS=="win"', {
					'cflags_cc': [ '/DUSE_LIBUV' ],
					'cflags_cc!': []
				}]
			]
		}
	]
}
