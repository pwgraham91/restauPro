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
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function reserve(tableid) {
        var input = '#myform' + tableid;
        console.log(input);
        $.ajax({
            url: 'make_reservation_at_table/' + tableid + '/',
            type: 'GET',
            success: function (data) {
                $('#resModalForm').html(data);
                time()
            },
            headers: {
                "X-CSRFToken": csrftoken
            }

        });

    }

//        $('#submitButton').on('click', function () {
//            $.ajax({
//                url: 'make_reservation_at_table/' + tableid + '/',
//                type: 'POST',
//                success: function (data) {
//                    console.log('ok')
//                },
//                headers: {
//                    "X-CSRFToken": csrftoken
//                }
//            })
//
//            });

        $('.newPartyButton').on('click', function () {
            var table_id = $(this).parent().attr("id");
            console.log(table_id);
            return reserve(table_id);
        });
        function time() {
            $('#id_reservation_time').replaceWith('<div class="form-group"><div class="input-group date form_datetime col-md-12" data-date="1979-09-16T05:25:07Z" data-date-format="mm/dd/yyyy hh:ii" data-link-field="dtp_input1"><input id="id_reservation_time" name="reservation_time" type="text" class="form-control" size="16" type="text" value="" readonly><span class="input-group-addon"><span class="glyphicon glyphicon-remove"></span></span><span class="input-group-addon"><span class="glyphicon glyphicon-th"></span></span></div><input type="hidden" id="dtp_input1" value="" /><br/></div>');
            $('.form_datetime').datetimepicker({
                weekStart: 1,
                todayBtn: 1,
                autoclose: 1,
                todayHighlight: 1,
                startView: 2,
                forceParse: 0,
                showMeridian: 0
            });
        }
    });
});
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
//    TODO OLD SUBMIT BUTTON ABOVE. REWRITING WITH PROPER AJAX POSTING
    $('#submitButton').on('click', function () {
        var party_name = $('#id_party_name').val();
        var number_of_males = $('#id_number_of_males').val();
        var number_of_females = $('#id_number_of_females').val();
        var number_of_children = $('#id_number_of_children').val();
        var lunch = $('#id_lunch').attr('checked');
        var monday_to_thursday = $('#id_monday_to_thursday').attr('checked');
        var reservation_time = $('#id_reservation_time').val();
        var seated_table = $(this).val().split(': ')[1];
        console.log(party_name);
        console.log(number_of_males);
        console.log(number_of_females);
        console.log(number_of_children);
        console.log(lunch);
        console.log(monday_to_thursday);
        console.log(reservation_time);
        console.log(seated_table);

        datas = {
            party_name: party_name,
            number_of_males: number_of_males
//             number_of_females=form.cleaned_data['number_of_females'],
//             number_of_children=form.cleaned_data['number_of_children'],
//             lunch=form.cleaned_data['lunch'],
//             monday_to_thursday=form.cleaned_data['monday_to_thursday'],
//             reservation_time=form.cleaned_data['reservation_time'],
//             seated_table=form.cleaned_data['seated_table'])

        };
//        $.ajax({
//            url: 'make_reservation_at_table/' + tableid + '/',
//            type: 'POST',
//            dataType: 'json',
//            data: datas
//        })
//
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

////
///Alternate
///**
// * Created by GoldenGate on 10/12/14.
// */
//
//$(document).ready(function() {
//    function getCookie(name) {
//        var cookieValue = null;
//        if (document.cookie && document.cookie != '') {
//            var cookies = document.cookie.split(';');
//            for (var i = 0; i < cookies.length; i++) {
//                var cookie = jQuery.trim(cookies[i]);
//                // Does this cookie string begin with the name we want?
//                if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                    break;
//                }
//            }
//        }
//        return cookieValue;
//    }
//
//    var csrftoken = getCookie('csrftoken');
//
//    function reserve(tableid) {
//        var input = '#myform' + tableid.toString()
//        console.log(input);
//        $.ajax({
//            url: 'make_reservation_at_table/' + tableid + '/',
//            type: 'GET',
//            success: function (data) {
//                $(input).html(data);
//            }
//
//        });
//    }
//
//    $('#submitButton').on('click', function () {
//        $.ajax({
//            url: 'make_reservation_at_table/' + tableid + '/',
//            type: 'POST',
//            success: function (data) {
//                console.log('ok')
//            },
//            headers: {
//                "X-CSRFToken": csrftoken
//            }
//        });
//        $('.newPartyButton').on('click', function () {
//            var table_id = $('.newPartyButton').parent().attr("id");
//            console.log(table_id);
//            return reserve(table_id);
//        });
//        function time() {
//            $('#id_reservation_time').replaceWith('<div class="form-group"><div class="input-group date form_datetime col-md-5" data-date="1979-09-16T05:25:07Z" data-date-format="mm/dd/yyyy hh:ii" data-link-field="dtp_input1"><input id="id_reservation_time" name="reservation_time" type="text" class="form-control" size="16" type="text" value="" readonly><span class="input-group-addon"><span class="glyphicon glyphicon-remove"></span></span><span class="input-group-addon"><span class="glyphicon glyphicon-th"></span></span></div><input type="hidden" id="dtp_input1" value="" /><br/></div>');
//            console.log("2")
//            $('.form_datetime').datetimepicker({
//                weekStart: 1,
//                todayBtn: 1,
//                autoclose: 1,
//                todayHighlight: 1,
//                startView: 2,
//                forceParse: 0,
//                showMeridian: 0
//            });
//        }
//    });
//});

