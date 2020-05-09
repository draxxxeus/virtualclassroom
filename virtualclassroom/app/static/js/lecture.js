$("#new_comment").on("submit", function (event) {
    var $this = $(this);
    var frmValues = $this.serialize();
    $.ajax({
        type: $this.attr('method'),
        url: $this.attr('action'),
        data: frmValues
    })
    .done(function (data) {
        dt = new Date(data['date_created']);
        var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
        comment_date = [];
        comment_date.push(months[dt.getMonth()]);
        comment_date.push(dt.getDay() + ",");
        comment_date.push(dt.getFullYear());
        hours = dt.getHours();
        suffix = 'a.m.';
        if (hours > 12) {
          hours = hours - 12;
          suffix = 'p.m.';
        }
        comment_date.push(hours + ":" + dt.getMinutes());
        comment_date.push(suffix);
        html_data = "<small>"+data['user']+"</small>";
        html_data += "<small class='float-right'>"+comment_date.join(' ')+"</small>";
        html_data += "<li>"+data['comment']+"</li>";
        $("ul#discussions").prepend(html_data).hide().fadeIn('slow');
        $("#new_comment")[0].reset();
    })
    .fail(function () {
        console.log("An error occured");
    });
    event.preventDefault();
});
