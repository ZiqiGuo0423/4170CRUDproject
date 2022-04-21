
$(document).ready(function(){

    $('#newdata').on('click',function(){        
        window.location.assign("/add");
    });

    function search(event){
        let value = $('#search').val()
        console.log(value)
        event.preventDefault();

        let value_trim = value.trim()
        if (value_trim != ''){
            window.location.assign("/search_results/"+value+"");
        }

        $('#search').focus();
        $('#search').val('');
    }
    $('#search').focus();

    $( "#target" ).submit(function( event ) {
        search(event);      
    });

    let check;
    $('#search').focus(function(){
        check = 0
    });
    $('#search').blur(function(){
        check = 1
    });

    $('body').keydown(function(event){
        if (event.keyCode == 13 && check == 0){
            search(event);
        }
    })

})