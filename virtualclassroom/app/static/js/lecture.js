$("#new_comment").on("submit", function (event) {
    var $this = $(this);
    var frmValues = $this.serialize();
    $.ajax({
        type: $this.attr('method'),
        url: $this.attr('action'),
        data: frmValues
    })
    .done(function (data) {
        html_data = "<small>"+data['user']+"</small>"
        html_data += "<small class='float-right'>"+data['date_created']+"</small>"
        html_data += "<li>"+data['comment']+"</li>"
        $("ul#discussions").prepend(html_data).hide().fadeIn('slow');
        $("#new_comment")[0].reset();
    })
    .fail(function () {
        console.log("An error occured");
    });
    event.preventDefault();
});
