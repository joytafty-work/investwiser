$(function() {

var g_data=[]; 
    d3.csv('static/predictions/RF_classify_and_regress.csv', function (data) { g_data = data; } );
    // Load companies data
    var c_data = []; 
    d3.csv('static/companies.csv', function (data) { c_data = data; } );

    // Pin click responses
    $(document).ready(function() {      
    $('.pin').click(function (e) {
      // e.preventDefault();
      alert('hi');
      var s = $(this).attr('data-company');
      console.log(s);
  
      for(i in g_data) {
          row = g_data[i]; 
          if (row.name.toLowerCase() == s.toLowerCase()) {
            gi = i;
            }
          }

        for (j in c_data) {
          r = c_data[j]; 
          if (r.company_name.toLowerCase() == s.toLowerCase()) {
            cj = j;
          }
        }
          target = g_data[gi].company_name;
          prob = g_data[gi].RFCprobA;
          aval = g_data[gi].RFRval;
          worth = g_data[gi].RFRpred; 
          worthval = (worth/1000000).toPrecision(3);
          aval = (aval/1000000).toPrecision(3);

          if (aval != 0) {
            $('#worth-box').html('<h2> $' + worthval + 'M</h2><h3>($' + aval + 'M)</h3>');
          } else {
            if (prob < 0.3) {
              $('#worth-box').html('<h2> <$1M </h2>');
            } else {
              $('#worth-box').html('<h2> $' + worthval + 'M </h2>');
            }
          }

          $('#prob-box').html('<h2>' + (prob*100).toPrecision(3) + ' % </h2>');
          $('#company_img').attr('src', c_data[cj].company_img);
          $('#result-box').fadeIn();
      });
		console.log( "pinclick report!" );
    });
    console.log( "ready!" );
});
