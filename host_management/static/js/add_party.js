/**
 * Created by GoldenGate on 10/12/14.
 */
$(document).ready(function() {
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

});

