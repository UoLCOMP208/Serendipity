$(function () {
    var editor = new Simditor({
        textarea: $('#editor'),
        //optional options
        toolbar: ['title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale', 'color', 'ol', 'ul', 'blockquote', 'code', 'table', 'hr', 'indent', 'outdent', 'alignment'],
    });

    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var titleInput = $('input[name="title"]');
        var boardSelect = $("select[name='board_id']");

        var title = titleInput.val();
        var board_id = boardSelect.val();
        var content = editor.getValue();

        zlajax.post({
            'url': '/apost/',
            'data': {
                'title': title,
                'content':content,
                'board_id': board_id
            },
            'success': function (data) {
                if(data['code'] == 200){
                    zlalert.alertConfirm({
                        'msg': 'Congrats! Post success!',
                        'cancelText': 'Back to post list',
                        'confirmText': 'Post another one',
                        'cancelCallback': function () {
                            window.location = '/post_list';
                        },
                        'confirmCallback': function () {
                            titleInput.val("");
                            editor.setValue("");
                        }
                    });
                }else{
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});