$(function(){
    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var email_input = $("input[name='email']");
        var password_input = $("input[name='password']");
        var remember_input = $("input[name='remember']");

        var email = email_input.val();
        var password = password_input.val();
        var remember = remember_input.checked ? 1 : 0;


        zlajax.post({
            'url': '/signin/',
            'data': {
                'email': email,
                'password': password,
                'remember': remember
            },
            'success': function (data) {
                if(data['code'] == 200){
                    // var return_to = $("#return-to-span").text();
                    // if(return_to){
                    //     window.location = return_to;
                    // }else{
                        window.location = '/';
                    // }
                }else{
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});