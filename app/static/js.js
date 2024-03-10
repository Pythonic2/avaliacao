$(document).ready(function() {
    $("#save-button").click(function() {
        var formData = $("#myform").serialize();
        
        $.ajax({
            type: 'GET',
            url: '{% url "/create-funci/" %}',
            datatype: "json",

            success: function() {
                console.log('ok')
            }
    });
});
