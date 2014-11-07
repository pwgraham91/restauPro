/**
 * Created by GoldenGate on 10/12/14.
 */

$(document).ready(function() {
 function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
    function reserve (tableid){
        var input = '#myform'+tableid;
        console.log(input);
        $.ajax({
            url: 'make_reservation_at_table/' + tableid + '/',
            type: 'GET',
            success: function(data) {
                $('#resModalForm').html(data);
                time()
            },
            headers: {
                "X-CSRFToken": csrftoken
            }

    });

    }
        $('#submitButton').on('click', function () {
        $.ajax({
            url: 'make_reservation_at_table/' + tableid + '/',
            type: 'POST',
            success: function (data) {
                console.log('ok')
            },
            headers: {
                "X-CSRFToken": csrftoken
            }
        })

        });
    $('.newPartyButton').on('click', function() {
        var table_id = $(this).parent().attr("id");
        console.log(table_id);
        return reserve(table_id);
    });
    function time (){
    $('#id_reservation_time').replaceWith('<div class="form-group"><div class="input-group date form_datetime col-md-5" data-date="1979-09-16T05:25:07Z" data-date-format="mm/dd/yyyy hh:ii" data-link-field="dtp_input1"><input id="id_reservation_time" name="reservation_time" type="text" class="form-control" size="16" type="text" value="" readonly><span class="input-group-addon"><span class="glyphicon glyphicon-remove"></span></span><span class="input-group-addon"><span class="glyphicon glyphicon-th"></span></span></div><input type="hidden" id="dtp_input1" value="" /><br/></div>');
    $('.form_datetime').datetimepicker({
        weekStart: 1,
        todayBtn:  1,
		autoclose: 1,
		todayHighlight: 1,
		startView: 2,
		forceParse: 0,
        showMeridian: 0
    });
    }
});
