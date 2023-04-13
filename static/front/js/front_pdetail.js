$(function () {
    var editor = new Simditor({
        textarea: $('#editor'),
        //optional options
        toolbar: ['title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale', 'color', 'ol', 'ul','code'],
    });

    $("#comment-btn").click(function (event) {
        event.preventDefault();
        var loginTag = $("#login-tag").attr("data-is-login");
        if (!loginTag) {
            window.location = '/signin/';
        } else {
            var content = editor.getValue();
            var post_id = $("#post-content").attr("data-id");
            zlajax.post({
                'url': '/acomment/',
                'data': {
                    'content': content,
                    'post_id': post_id
                },
                'success': function (data) {
                    if (data['code'] == 200) {
                        window.location.reload();
                    } else {
                        zlalert.alertInfo(data['message']);
                    }
                }
            });
        }
    });
});
