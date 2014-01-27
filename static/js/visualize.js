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
    
}

function cback(results) {
    window.history.pushState("", "InvestWiser", "/fetchcompany?q="+results['query']);

    //    $("chartlayer").remove();
    //    $("textlayer").remove();
    alert("cback was called with results " + results);
    $("#spinner").html('');
    $("#summarybut").css("background", "#fff");
    $("#summarybut").css("color", "#666");
    $("#summarybut").css("border", "1px solid #ddd");
    $("#timelinebut").css("background", "#02a6eb");
    $("#timelinebut").css("color", "#fff");
    $("#timelinebut").css("border", "0px");

    // $('.timeline-jquery').verticalTimeline({
    //    data: results['items'],
    //    width: '100%',
    //   });
    $("#people-info").prepend('<img alt="" src="https://s3.amazonaws.com/photos.angel.co/startups/i/32217-9cef1dc3721cc42fcad1871cb99ef109-medium_jpg.jpg?buster=1326842472">');
    // $("#people-info").appendFounderImg({
    //     data: results['items'],
    //     width: '100%',
    // })
}