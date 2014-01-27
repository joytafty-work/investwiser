function queryURL(query) {
    $("#query").val(query);
    visualize();        
}

function visualize() {
    var url = "/analyze";
    var Q = $("#query").val();
    var html = '<img src="static/img/ajaxSpinner.gif" alt="Please wait" width=40px height=40px>';
    $("#spinner").html(html);    
    $("#google-table" ).empty();
    $("#people-info" ).empty();
    $.post(url, {'jobQuery':Q}, cback); 
}

function drawd3(results) {
    // Try CSV first
    d3.csv("../static/data/")

}

function cback(results) {
    window.history.pushState("", "InvestWiser", "/fetchcompany?q="+results['query']);

    alert("cback was called with results " + results);
    $("#spinner").html('');
    $("#summarybut").css("background", "#fff");
    $("#summarybut").css("color", "#666");
    $("#summarybut").css("border", "1px solid #ddd");
    $("#timelinebut").css("background", "#02a6eb");
    $("#timelinebut").css("color", "#fff");
    $("#timelinebut").css("border", "0px");

    appendFounderImg(results);
}

function appendFounderImg(data) {
   alert("appendFounderImg was called with results " + data['company_img']);
   console.log(data['company_img']);
   $('#people-info').prepend('<img alt="" src="' + data['company_img'] + ">'");
    // $('#people-info').prepend('<img alt="" src="https://s3.amazonaws.com/photos.angel.co/startups/i/32217-9cef1dc3721cc42fcad1871cb99ef109-medium_jpg.jpg?buster=1326842472">');    
}

// (function($) {
//     $.fn.appendFounderImg(data) {
//     var container = document.getElementById('people-info');
//     alert("appendFounderImg was called with results " + data);
//     $('#people-info').prepend('<img alt="" src="https://s3.amazonaws.com/photos.angel.co/startups/i/32217-9cef1dc3721cc42fcad1871cb99ef109-medium_jpg.jpg?buster=1326842472">');
// })(jQuery);