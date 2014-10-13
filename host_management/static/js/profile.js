/**
 * Created by GoldenGate on 10/12/14.
 */
$(document).ready(function() {
    $('#getPokeInfoBtn').on('click', function() {
    $.ajax({
        url: '/pokemon_info/' + pokemonID + '/',
        type: 'GET',
        success: function(data) {
            $('.infoBlock').html(data);
        }
    });
});
});