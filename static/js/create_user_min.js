var $form = '';
var base_modal_html = '';

$(function() {
  init();
});

function init(){
    $form = $('#user_form');
    base_modal_html = $('#user_modal').html();
}

function clear_form() {
    $('input', $form).val('')
}

function getFormData(form) {
    var unindexed_array = form.serializeArray();
    var indexed_array = {};
    $.map(unindexed_array, function (n, i) {
        indexed_array[n['name']] = n['value'];
    });

    return indexed_array;
}

function send_data() {
    var id = $('#user_id').html();
    var prefix = (id !== undefined) ? id : '';
    var user_data = getFormData($form);
    $.ajax({
        url: 'create/user/' + prefix,
        type: 'POST',
        data: user_data,
        dataType: 'json',
        success: function (response) {
            clear_form();
            $('#users_list').html(response.html)
        },
    });
}

function fill_form(id){
    $.ajax({
        url: 'get_user_form/' + id,
        type: 'GET',
        dataType: 'json',
        success: function (response) {

            $('#user_form').html(response.html);
        },
    });
}