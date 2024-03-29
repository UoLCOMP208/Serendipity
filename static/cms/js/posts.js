$(function () {
    $(".highlight-btn").click(function () {
        var self = $(this);
        var tr = self.parent().parent();
        var post_id = tr.attr("data-id");
        var highlight = parseInt(tr.attr("data-highlight"));
        var url = "";
        if(highlight){
            url = "/cms/uhpost/";
        }else{
            url = "/cms/hpost/";
        }
        zlajax.post({
            'url': url,
            'data': {
                'post_id': post_id
            },
            'success': function (data) {
                if(data['code'] == 200){
                    zlalert.alertSuccessToast('Success!');
                    setTimeout(function () {
                        window.location.reload();
                    }, 800);
                }else{
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});

$(function () {
    $(".delete-post-btn").click(function () {
        var self = $(this);
        var tr = self.parent().parent();
        var post_id = tr.attr('data-id');
        zlalert.alertConfirm({
            "msg":"Are you sure to delete this post?",
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/cms/dpost/',
                    'data':{
                        'post_id': post_id
                    },
                    'success': function (data) {
                        if(data['code'] == 200){
                            window.location.reload();
                        }else{
                            zlalert.alertInfo(data['message']);
                        }
                    }
                })
            }
        });
    });
});