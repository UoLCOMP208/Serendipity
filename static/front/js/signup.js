$(function () {
    $("#captcha-btn").click(function (event) {
        event.preventDefault();
        var email = $("input[name='email']").val();
        if (!email) {
            zlalert.alertInfoToast('Please enter your email address!');
            return;
        }
        zlajax.get({
            'url': '/email_captcha/',
            'data': {
                'email': email
            },
            'success': function (data) {
                if (data['code'] == 200) {
                    zlalert.alertSuccessToast('Email sent successfully!');
                } else {
                    zlalert.alertInfo(data['message']);
                }
            },
            'fail': function (error) {
                zlalert.alertNetworkError();
            }
        });
    });
});

$(function(){
    $("#submit-btn").click(function(event){
        event.preventDefault();
        var email_input = $("input[name='email']");
        var email_captcha_input = $("input[name='captcha']");
        var username_input = $("input[name='username']");
        var password_input = $("input[name='password']");

        var email = email_input.val();
        var email_captcha = email_captcha_input.val();
        var username = username_input.val();
        var password = password_input.val();

        zlajax.post({
            'url': '/signup/',
            'data': {
                'email': email,
                'email_captcha': email_captcha,
                'username': username,
                'password': password,
            },
            'success': function(data){
                if(data['code'] == 200){
                    var return_to = $("#return-to-span").text();
                    if(return_to){
                        window.location = return_to;
                    }else{
                        window.location = '/';
                    }
                }else{
                    zlalert.alertInfo(data['message']);
                }
            },
            'fail': function(){
                zlalert.alertNetworkError();
            }
        });
    });
});
