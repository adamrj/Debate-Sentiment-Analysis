


$( document ).ready(function() {
	
	$.getJSON("/sentiment/dot_chart", function(result) {

		var all_candidates = {}
		
		for (candidate in result['candidates']) {
			var candidateData = [];
			for (k in result['candidates'][candidate]){
				candidateData.push({"minute": k, "score": result['candidates'][candidate][k]})
			}
			all_candidates[candidate] = candidateData
		}

	  var vis = d3.select("#visualisation"),
	    WIDTH = 1000,
	    HEIGHT = 500,
	    MARGINS = {
	        top: 20,
	        right: 20,
	        bottom: 20,
	        left: 50
    },

    xScale = d3.scale.linear().range([MARGINS.left, WIDTH - MARGINS.right]).domain([40,195]);

    yScale = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([0,1]);

    xAxis = d3.svg.axis()
    .scale(xScale);
  
		yAxis = d3.svg.axis()
    .scale(yScale)
    .orient("left");

    vis.append("svg:g")
    .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
    .call(xAxis);

    vis.append("svg:g")
    .attr("transform", "translate(" + (MARGINS.left) + ",0)")
    .call(yAxis);

    var dot = vis.append("g")
      .attr("class", "dots")
    .selectAll(".dot")
      .data(10)
    .enter().append("circle")
      .attr("class", "dot")
      .style("fill", function(d) { return colorScale(color(d)); })
      .call(position)
      .sort(order);




	})
	
	


});

