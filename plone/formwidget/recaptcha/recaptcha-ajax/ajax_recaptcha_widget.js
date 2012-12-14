    function showRecaptcha() {
        var div = $('#recaptcha_div');
        var public_key = div.attr('data-key');
        var rc_theme = div.attr('data-theme');
        var rc_lang = div.attr('data-lang');
                 
        Recaptcha.create( public_key,
                         'recaptcha_div',
                         { theme: rc_theme,
                           lang: rc_lang
                         } );
    }
