
$(document).ready(function(){
    
    function display_popular(){
        /* make a GET request to retrieve the most popular */
        $.getJSON('/display_popular',
                 function(data){
                    display(data);

        });
    };

    function display(data){
        console.log(data);
       
        let id1 =  data[0]["id"];    
        let image1 = data[0]["image"];
        $('#card1').append($("<div class = 'u-title' id = "+id1+" >" +data[0]["name"] + "</div>"));
        $('#body1').append($("<img class = 'homepage_image' id = "+id1+" src = '"+image1+"' alt = 'Stanford University'> "));
        $('#body1').append($("<div class = 'rank'>" + 'QS-Ranking : ' + data[0]['QS_Ranking'] + "</div>"));
        $('#body1').append($("<div class = 'description'>" + data[0]['short-description'] + "</div>"));
        

        let id2 =  data[1]["id"];   
        let image2 = data[1]["image"]; 
        $('#card2').append($("<div class = 'u-title' id = "+id2+" >" + data[1]["name"] + "</div>"));
        $('#body2').append($("<img class = 'homepage_image' id = "+id2+" src = '"+image2+"' alt = 'Massachusetts Institute of Technology'> "));
        $('#body2').append($("<div class = 'rank'>" + 'QS-Ranking : ' + data[1]['QS_Ranking'] + "</div>"));
        $('#body2').append($("<div class = 'description'>" + data[1]['short-description'] + "</div>"));

        let id3 =  data[2]["id"]; 
        let image3 = data[2]["image"];   
        $('#card3').append($("<div class = 'u-title' id = "+id3+" >" + data[2]["name"] + "</div>"));
        $('#body3').append($("<img class = 'homepage_image' id = "+id3+" src = '"+image3+"' alt = 'Carnegie Mellon University'> "));
        $('#body3').append($("<div class = 'rank'>" + 'QS-Ranking : ' + data[2]['QS_Ranking'] + "</div>"));
        $('#body3').append($("<div class = 'description'>" + data[2]['short-description'] + "</div>"));

        $(".homepage_image").css({'height':'50%','width':'100%'});
        
        $('.rank').css({'padding-top':'20px'});

        $('.description').css({'padding-top':'20px','color':'rgb(126, 123, 123)','font-size':'15px'});




        $('.card').click(function(){
            let id = $(this).children().children().attr('id');
            console.log(id);

            /* redirect the webpage to view */
            window.location.assign("/view/"+id+"")
        })

        
    }

    display_popular();

    

})

