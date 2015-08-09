


$( document ).ready(function() {
    $.getJSON("/sentiment/bar_chart", function(result) {
    	

    	var dataset2 = []
    	for (candidate in result['candidates'] ) {
  
    		dataset2.push([candidate,result['candidates'][candidate]['score__avg']])
    	}


   	var w = 600;
      var h = 200;
      var barPadding = 1;
      
      var dataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
              11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ];

      // var dataset2 = [ ["John", 25], ["John", 5], ["John", 5], ["John", 20 ], ["John", 35], ["John", 5], ["John", 5], ["John", 5], ["John", 45], ["John", 5],
      //         ["John", 5], ["John", 24], ["John", 8], ["John", 5], ["John", 5], ["John", 5], ["John", 5], ["John", 5], ["John", 20], ["John", 12] ];
 

      //Create SVG element
      var svg = d3.select("body")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

      svg.selectAll("rect")
         .data(dataset2)
         .enter()
         .append("rect")
         .attr("x", function(d, i) {
            return i * (w / dataset2.length);
         })
         .attr("y", function(d) {
            return h - (d[1] * 100);
         })
         .attr("width", w / dataset2.length - barPadding)
         .attr("height", function(d) {
            return d[1] * 100;
         })
         .attr("fill", function(d) {
          return "rgb(0, 0, " + parseInt(d[1]*360)+ ")";
         });



      svg.selectAll("text")
         .data(dataset2)
         .enter()
         .append("text")
         .text(function(d) {
            return d[0]
            // return d[1].toFixed(2);
         })
         .attr("text-anchor", "middle")
         .attr("x", function(d, i) {
            return i * (w / dataset2.length) + (w / dataset2.length - barPadding) / 2;
         })
         .attr("y", function(d) {
            return h - (d[1] * 100) + 14;
         })
         .attr("font-family", "sans-serif")
         .attr("font-size", "11px")
         .attr("fill", "white")
    })

});



