function bindEmailCaptchaClick() {
    $("#captcha-btn").click(function (event) {
        // $this：the jquery objective of the current button
        var $this = $(this);
        // Blocke the default event
        event.preventDefault();

        var email = $("input[name='email']").val();
        $.ajax({
            // http://127.0.0.1:500
            // /auth/captcha/email?email=xxx@gmail.com
            url: "/author/captcha/email?email=" + email,
            method: "GET",
            success: function (result) {
                var code = result['code'];
                if (code == 200) {
                    var countdown = 5;
                    // Cancel the button click event before the countdown starts
                    $this.off("click");
                    var timer = setInterval(function () {
                        $this.text(countdown);
                        countdown -= 1;
                        // Execute when the countdown ends
                        if (countdown <= 0) {
                            // Clear the timer
                            clearInterval(timer);
                            // Change the button text back
                            $this.text("Get code");
                            // Rebind click events
                            bindEmailCaptchaClick();
                        }
                    }, 1000); // 1000ms = 1s
                    // alert("Email verification code sent success!");
                } else {
                    alert(res['message']);
                }
            },
            fail: function (error) {
                console.log(error);
            }
        })
    });
}


// The entire page is loaded and then executed
$(function () {
    bindEmailCaptchaClick();
});
