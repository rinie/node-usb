{
  'targets': [  
    {
      'target_name': 'usb_bindings',
      'sources': [ 
        './src/node_usb.cc',
        './src/bindings.cc',
        './src/usb.cc',
        './src/device.cc',
        './src/interface.cc',
        './src/endpoint.cc',
        './src/transfer.cc',
        './src/stream.cc',  
      ],
      'defines': [
        '_LARGEFILE_SOURCE',
        '_FILE_OFFSET_BITS=64',
      ],
      'include_dirs+': [
        'src/',
        'libusb-1.0/include/'
      ],
      'link_settings': {
        'conditions' : [
            ['OS=="linux"',
                {
                    'libraries': [
                      '-lusb-1.0'
                    ]
                }
            ],
            ['OS=="mac"',
                {
                    'libraries': [
                      '-lusb-1.0'
                    ]
                }
            ],
        [ 'OS=="win"', {
		'libraries' : [ 
			'-l/temp/node-usb/libusb-1.0/lib/Win32/Release/libusb-1.0.lib' 
		],
          'msvs_settings': {
            'VCLinkerTool': {
              'AdditionalDependencies': [
                'setupapi.lib'
              ]
            }
          }
        }]
        ]
      }  
    }
  ]
}
