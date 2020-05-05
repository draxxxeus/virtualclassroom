$("#contact_form").on("submit", function (event) {
    var $this = $(this);
    var frmValues = $this.serialize();
    $("button").text("Please wait");
    $("button").prop("disabled", true);
    $.ajax({
        type: $this.attr('method'),
        url: $this.attr('action'),
        data: frmValues
    })
    .done(function (data) {
        if (data['status'] == 'success') {
          html_data = '<div class="alert alert-success" role="alert">' + data['message'] + '</div>';
        } else {
          html_data = '<div class="alert alert-danger" role="alert">' + data['message'] + '</div>';
        }

        $("#contact_form").prepend(html_data);
        $("#contact_form")[0].reset();
        $("button").text("Submit");
        $("button").prop("disabled", false);
    })
    .fail(function () {
        console.log("An error occured");
    });
    event.preventDefault();
});
