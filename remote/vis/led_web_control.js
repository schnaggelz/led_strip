class LedWebControl
{
    constructor()
    {
        createState('ledWebControl.hostname', 0,
            {
                read: true,
                write: true,
                desc: 'LED Matrix Server Name',
                type: 'string',
                def: 'raspile1'
            })

        createState('ledWebControl.update', false, {
                read: true, 
                write: true, 
                desc: "LED Matrix Update", 
                type: "boolean", 
                def: false
            });

        createState('ledWebControl.text1', 0,
            {
                read: true,
                write: true,
                desc: 'LED Matrix Text 1',
                type: 'string',
                def: ''
            })

        createState('ledWebControl.text2', 0,
            {
                read: true,
                write: true,
                desc: 'LED Matrix Text 2',
                type: 'string',
                def: ''
            })

        createState('ledWebControl.text3', 0,
            {
                read: true,
                write: true,
                desc: 'LED Matrix Text 3',
                type: 'string',
                def: ''
            })

        createState('ledWebControl.bg_color_R', 0,
            {
                read: true,
                write: true,
                desc: 'LED Hintergrund R',
                type: 'number',
                def: 255
            })

        createState('ledWebControl.bg_color_G', 0,
            {
                read: true,
                write: true,
                desc: 'LED Hintergrund G',
                type: 'number',
                def: 255
            })

        createState('ledWebControl.bg_color_B', 0,
            {
                read: true,
                write: true,
                desc: 'LED Hintergrund B',
                type: 'number',
                def: 255
            })

        createState('ledWebControl.fg_color_R', 0,
            {
                read: true,
                write: true,
                desc: 'LED Vordergrund R',
                type: 'number',
                def: 255
            })

        createState('ledWebControl.fg_color_G', 0,
            {
                read: true,
                write: true,
                desc: 'LED Vordergrund G',
                type: 'number',
                def: 255
            })

        createState('ledWebControl.fg_color_B', 0,
            {
                read: true,
                write: true,
                desc: 'LED Vordergrund B',
                type: 'number',
                def: 255
            })
    }

    requestChange(hostname, text, id)
    {
        var fg_color_R = getState('javascript.0.ledWebControl.fg_color_R').val
        var fg_color_G = getState('javascript.0.ledWebControl.fg_color_G').val
        var fg_color_B = getState('javascript.0.ledWebControl.fg_color_B').val
        var bg_color_R = getState('javascript.0.ledWebControl.bg_color_R').val
        var bg_color_G = getState('javascript.0.ledWebControl.bg_color_G').val
        var bg_color_B = getState('javascript.0.ledWebControl.bg_color_B').val

        request({
            method: 'POST',
            url: `http://${hostname}:5000/api/set_text/1234`,
            json: true,
            body: {
                'id': id,
                'text': text,
                'fg_color_R' : fg_color_R,
                'fg_color_G' : fg_color_G,
                'fg_color_B' : fg_color_B,
                'bg_color_R' : bg_color_R,
                'bg_color_G' : bg_color_G,
                'bg_color_B' : bg_color_B
            }

        }, function(error, response, body) {
            if(error) log(error, 'warn');
        }
        )

        log(`Request with ID ${id} sent`);
    }
}

var ctl = new LedWebControl();

on('javascript.0.ledWebControl.text1', function(dp) {
    
    const host = getState('javascript.0.ledWebControl.hostname').val
    const text = getState('javascript.0.ledWebControl.text1').val

    ctl.requestChange(host, text, 1)
});

on('javascript.0.ledWebControl.text2', function(dp) {
    
    const host = getState('javascript.0.ledWebControl.hostname').val
    const text = getState('javascript.0.ledWebControl.text2').val

    ctl.requestChange(host, text, 2)
});

on('javascript.0.ledWebControl.text3', function(dp) {
    
    const host = getState('javascript.0.ledWebControl.hostname').val
    const text = getState('javascript.0.ledWebControl.text3').val

    ctl.requestChange(host, text, 3)
});

