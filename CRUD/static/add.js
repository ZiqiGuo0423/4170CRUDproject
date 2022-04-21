
$(document).ready(function(){
   
    $('#u-name').focus();

    $('#error-name').hide();
    $('#error-url').hide();
    $('#error-rank-empty').hide();
    $('#error-rank-number').hide();
    $('#error-score-empty').hide();
    $('#error-score-number').hide();
    $('#error-overview').hide();
    $('#error-fee').hide();
    $('#error-deadline').hide();
    $('#error-specialization').hide();
    $('#error-address').hide();
    $('#error-contact').hide();

    $('#success').hide();
    $('.input-success-button').hide();
    

    $('#submit').on('click',function(){

        let u_name = $('#u-name').val().trim();

        let u_url = $('#u-url').val().trim();

        let u_rank = $('#u-rank').val().trim();

        let u_score = $('#u-score').val().trim();

        let u_view = $('#u-view').val().trim();

        let u_fee = $('#u-fee').val().trim();

        let u_deadline = $('#u-deadline').val().trim();

        let u_specialization = $('#u-specialization').val().trim();

        let u_add = $('#u-add').val().trim();

        let u_email = $('#u-email').val().trim();

    

        /* error handling */
        if (u_email == ''){
            $('#u-email').focus();
            $('#error-contact').show();
        }
        else{
            $('#error-contact').hide();
        }

        if (u_add == ''){
            $('#u-add').focus();
            $('#error-address').show();
        }
        else{
            $('#error-address').hide();
        }

        if (u_specialization == ''){
            $('#u-specialization').focus();
            $('#error-specialization').show();
        }
        else{
            $('#error-specialization').hide();
        }

        if (u_deadline == ''){
            $('#u-deadline').focus();
            $('#error-deadline').show();
            $(window).scrollTop($('#u-deadline').position().top);
        }
        else{
            $('#error-deadline').hide();
        }

        if (u_fee == ''){
            $('#u-fee').focus();
            $('#error-fee').show();
            $(window).scrollTop($('#u-fee').position().top);
        }
        else{
            $('#error-fee').hide();
        }

        if (u_view == ''){
            $('#u-view').focus();
            $('#error-overview').show();
            $(window).scrollTop($('#u-view').position().top);
        }
        else{
            $('#error-overview').hide();
        }
        
        if (u_score == ''){
            $('#u-score').focus();
            $('#error-score-number').hide();
            $('#error-score-empty').show();
            $(window).scrollTop($('#u-score').position().top);
        }
        else if(isNaN(u_score)){
            $('#u-score').focus();
            $('#error-score-empty').hide();
            $('#error-score-number').show();
            $(window).scrollTop($('#u-score').position().top);
        }
        else{
            $('#error-score-empty').hide();
            $('#error-score-number').hide();
        }

        if (u_rank == ''){
            $('#u-rank').focus();
            $('#error-rank-number').hide();
            $('#error-rank-empty').show();
            $(window).scrollTop($('#u-rank').position().top);
        }
        else if(isNaN(u_rank)){
            $('#u-rank').focus();
            $('#error-rank-empty').hide();
            $('#error-rank-number').show();
            $(window).scrollTop($('#u-rank').position().top);
        }
        else{
            $('#error-rank-empty').hide();
            $('#error-rank-number').hide();
        }

        if (u_url == ''){
            $('#u-url').focus();
            $('#error-url').show();
            $(window).scrollTop($('#u-url').position().top);
        }
        else{
            $('#error-url').hide();
        }
       
        if (u_name == ''){
            $('#error-name').show();
            $(window).scrollTop($('#u-name').position().top);
            $('#u-name').focus();
        }
        else{
            $('#error-name').hide();
        }


        if (u_name != '' && u_url != '' && u_rank != '' && !isNaN(u_rank) && u_score != '' && !isNaN(u_score) && u_fee != '' && u_deadline != '' && u_specialization != '' && u_add != '' && u_email != ''){
            let data = {
                'u-name' : u_name,
                'u-url' : u_url,
                'u-rank' : u_rank,
                'u-score' : u_score,
                'u-view' : u_view,
                'u-fee' :  u_fee,
                'u-deadline' : u_deadline,
                'u-specialization' : u_specialization,
                'u-add' : u_add,
                'u-email' : u_email
            }
            save_data(data);

        }
    });



    function save_data(new_data){
       
        let data_to_save = new_data;

        $.ajax({
            type: "POST",
            url: "save_data",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_save),
            success: function(result){
                console.log(result['university']);
                console.log(result['id']);

                $('#u-email').val('');
                $('#u-add').val('');
                $('#u-specialization').val('');
                $('#u-deadline').val('');
                $('#u-fee').val('');
                $('#u-view').val('');
                $('#u-score').val('');
                $('#u-rank').val('');
                $('#u-url').val('');
                $('#u-name').val('');

                $('#u-name').focus();


                let id = result['id']; 
                $('#success').show();
                $('.input-success-button').show();
                $(window).scrollTop($('.container').position().top);
                $('#newitem').on('click',function(){
                    window.location.assign("/view/"+id+"")
                });
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    }

})