$(document).ready(function(){
    $(".choose-size").on('click',function(){
        var _price = $(this).attr("get-price");
        $(".display-price").text(_price);

    });
});


 