$(function () {
    $("#add-board-btn").click(function (event) {
        event.preventDefault();
        zlalert.alertOneInput({
            'text':'Please enter the board name!',
            'placeholder': 'Board name',
            'confirmCallback': function (inputValue) {
                zlajax.post({
                    'url': '/cms/aboard/',
                    'data': {
                        'name': inputValue
                    },
                    'success': function (data) {
                        if(data['code'] == 200){
                            window.location.reload();
                        }else{
                            zlalert.alertInfo(data['message']);
                        }
                    }
                });
            }
        });
    });
});

$(function () {
    $(".edit-board-btn").click(function () {
        var self = $(this);
        var tr = self.parent().parent();
        var name = tr.attr('data-name');
        var board_id = tr.attr("data-id");

        zlalert.alertOneInput({
            'text': 'Please enter the new board name!',
            'placeholder': name,
            'confirmCallback': function (inputValue) {
                zlajax.post({
                    'url': '/cms/uboard/',
                    'data': {
                        'board_id': board_id,
                        'name': inputValue
                    },
                    'success': function (data) {
                        if(data['code'] == 200){
                            window.location.reload();
                        }else{
                            zlalert.alertInfo(data['message']);
                        }
                    }
                });
            }
        });
    });
});

$(function () {
    $(".delete-board-btn").click(function () {
        var self = $(this);
        var tr = self.parent().parent();
        var board_id = tr.attr('data-id');
        zlalert.alertConfirm({
            "msg":"Are you sure to delete this board?",
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/cms/dboard/',
                    'data':{
                        'board_id': board_id
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