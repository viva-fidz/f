function send_data() {
    var id = $('#user_id').html();
    console.log('user_id = ', id);
    var prefix =  (id != undefined) ? id : '';
    var user_data = getFormData($form);
    console.log('user_data = ', user_data);
    $.ajax({
        url: 'create/user/' + prefix,
        type: 'POST',
        data: user_data,
        dataType: 'json',
        success: function (response) {
            console.log("response = ", response);
            clear_form();
            update_page(response.html);
            console.log("Object create");
        },
    });
}

function fill_form(id) {
    $.ajax({
        url: 'get_user_form/' + id,
        type: 'GET'
        dataType: 'json',
        success: function (response) {
            if (response.errors) {
                console.log("errors -", errors);
            } else {
                $('#user_form').html(response.html);
            }
         },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    });
}