class LedWebControl
{
    constructor()
    {
        createState('ledWebControl.text', 0,
            {
                read: true,
                write: true,
                desc: "LED Matrix Text",
                type: "string"
            });
    }
}

var sbs = new LedWebControl();

on('javascript.0.ledWebControl.text', function(dp) {
    
    var text = getState('javascript.0.ledWebControl.text').val;

    request({
        method: 'POST',
        url: 'http://192.168.242.162:5000/api/set_text/1234',
        json: true,
        body: { 'text': text }

    }, function(error, response, body) {
        if(error) log(error, 'warn');
    });
});
